"""Connection to the Camunda 8 cluster.

The settings come from the file .env (see .env.example). The variable names are
the names that Camunda Console gives when you create an API client.
"""

import os
from functools import partial

import grpc
from dotenv import load_dotenv
from oauthlib.oauth2 import BackendApplicationClient
from pyzeebe import create_insecure_channel
from pyzeebe.channel.channel_options import get_channel_options
from pyzeebe.credentials.oauth import OAuth2MetadataPlugin
from requests_oauthlib import OAuth2Session

load_dotenv()

# newer Console versions (8.6 and later) give ZEEBE_GRPC_ADDRESS, pyzeebe reads ZEEBE_ADDRESS
if not os.getenv("ZEEBE_ADDRESS") and os.getenv("ZEEBE_GRPC_ADDRESS"):
    os.environ["ZEEBE_ADDRESS"] = os.environ["ZEEBE_GRPC_ADDRESS"]
if os.getenv("ZEEBE_ADDRESS", "").startswith(("grpcs://", "https://")):
    os.environ["ZEEBE_ADDRESS"] = os.environ["ZEEBE_ADDRESS"].split("://", 1)[1].rstrip("/")


def setting(name: str, default: str = "") -> str:
    """Read ZEEBE_<name>, or CAMUNDA_<name> as Console 8.6 and later calls it."""
    return os.getenv(f"ZEEBE_{name}") or os.getenv(f"CAMUNDA_{name}") or default


def create_channel():
    """Create the gRPC channel. Call this inside the running event loop."""
    if os.getenv("ZEEBE_LOCAL", "").strip() == "1":
        # local Camunda 8 Run or Docker Compose, without authentication
        return create_insecure_channel(grpc_address=os.getenv("ZEEBE_ADDRESS", "localhost:26500"))

    missing = [f"ZEEBE_{name}" for name in ("ADDRESS", "CLIENT_ID", "CLIENT_SECRET") if not setting(name)]
    if missing:
        raise SystemExit(f"Missing settings in .env: {', '.join(missing)}. See .env.example.")

    client_id = setting("CLIENT_ID")
    token_url = (os.getenv("CAMUNDA_OAUTH_URL") or setting("AUTHORIZATION_SERVER_URL")
                 or "https://login.cloud.camunda.io/oauth/token")

    # the camunda saas login wants the client id and secret in the form body.
    # pyzeebe 4.7 sends them as a basic auth header, and the login answers 400, so build the channel here
    session = OAuth2Session(client=BackendApplicationClient(client_id=client_id))
    fetch_token = partial(session.fetch_token, token_url=token_url, client_id=client_id,
                          client_secret=setting("CLIENT_SECRET"), include_client_id=True,
                          audience=setting("TOKEN_AUDIENCE", "zeebe.camunda.io"))
    call_credentials = grpc.metadata_call_credentials(OAuth2MetadataPlugin(session, fetch_token))
    credentials = grpc.composite_channel_credentials(grpc.ssl_channel_credentials(), call_credentials)
    return grpc.aio.secure_channel(os.environ["ZEEBE_ADDRESS"], credentials, options=get_channel_options())
