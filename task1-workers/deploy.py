"""Deploy process_order and process_payment, with their four forms, in one deployment.

By default the files come from the branch origin/main (run "git fetch" first), so the
local branch does not matter. Use --dir to deploy the files of a folder instead.

    python deploy.py
    python deploy.py --dir ../task1-bpmn/operational
"""

import argparse
import asyncio
import subprocess
import tempfile
from pathlib import Path

from pyzeebe import ZeebeClient

from connection import create_channel

RESOURCES = [
    "process-order.bpmn", "form-review-order.form", "form-amend-order.form",
    "process-payment.bpmn", "payment-details.form", "retry-or-cancel.form",
]
REPO = Path(__file__).resolve().parent.parent
FOLDER = "task1-bpmn/operational"


def export_from_git(ref: str, target: Path) -> None:
    for name in RESOURCES:
        data = subprocess.run(["git", "-C", str(REPO), "show", f"{ref}:{FOLDER}/{name}"],
                              capture_output=True, check=True).stdout
        (target / name).write_bytes(data)


async def main(args) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        if args.dir:
            folder = Path(args.dir)
        else:
            folder = Path(tmp)
            export_from_git(args.ref, folder)
            print(f"Files taken from {args.ref}:{FOLDER}")
        client = ZeebeClient(create_channel())
        response = await client.deploy_resource(*[folder / name for name in RESOURCES])

    print(f"Deployment key {response.key}")
    for item in response.deployments:
        name = getattr(item, "bpmn_process_id", None) or getattr(item, "form_id", None) or item
        print(f"  {type(item).__name__:<16} {name:<20} version {getattr(item, 'version', '?')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ref", default="origin/main", help="git ref to take the files from (default origin/main)")
    parser.add_argument("--dir", help="folder with the files, instead of a git ref")
    asyncio.run(main(parser.parse_args()))
