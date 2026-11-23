"""Connection to the Camunda 8 cluster.

The settings come from the file .env (see .env.example). The variable names are
the names that Camunda Console gives when you create an API client.
"""

import os

from dotenv import load_dotenv
from pyzeebe import create_insecure_channel, create_oauth2_client_credentials_channel

load_dotenv()

# newer Console versions (8.6 and later) give ZEEBE_GRPC_ADDRESS, pyzeebe reads ZEEBE_ADDRESS
if not os.getenv("ZEEBE_ADDRESS") and os.getenv("ZEEBE_GRPC_ADDRESS"):
    os.environ["ZEEBE_ADDRESS"] = os.environ["ZEEBE_GRPC_ADDRESS"]
if os.getenv("ZEEBE_ADDRESS", "").startswith(("grpcs://", "https://")):
    os.environ["ZEEBE_ADDRESS"] = os.environ["ZEEBE_ADDRESS"].split("://", 1)[1].rstrip("/")


def create_channel():
    """Create the gRPC channel. Call this inside the running event loop."""
    if os.getenv("ZEEBE_LOCAL", "").strip() == "1":
        # local Camunda 8 Run or Docker Compose, without authentication
        return create_insecure_channel(grpc_address=os.getenv("ZEEBE_ADDRESS", "localhost:26500"))

    missing = [name for name in ("ZEEBE_ADDRESS", "ZEEBE_CLIENT_ID", "ZEEBE_CLIENT_SECRET")
               if not (os.getenv(name) or os.getenv(name.replace("ZEEBE_", "CAMUNDA_")))]
    if missing:
        raise SystemExit(f"Missing settings in .env: {', '.join(missing)}. See .env.example.")

    return create_oauth2_client_credentials_channel(
        authorization_server=os.getenv("CAMUNDA_OAUTH_URL") or os.getenv("ZEEBE_AUTHORIZATION_SERVER_URL")
        or "https://login.cloud.camunda.io/oauth/token",
        audience=os.getenv("CAMUNDA_TOKEN_AUDIENCE") or os.getenv("ZEEBE_TOKEN_AUDIENCE") or "zeebe.camunda.io",
    )
