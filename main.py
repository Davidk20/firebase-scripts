import argparse
import json
import sys
import firebase_scripts
from utils.json import validate


class ArgParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f"\nError: {message}\n\n")
        self.print_help()
        sys.exit(2)


def main():
    parser = ArgParser(
        prog="main.py",
        description="""
        A set of utility scripts to quickly interact with Firebase Firestore databases.
        """,
    )

    parser.add_argument(
        "run_config",
        choices=["validate", "upload"],
        help="""
        validate = Validate the JSON,
        upload = Write the JSON to firestore,
        """,
    )

    parser.add_argument(
        "-d",
        "--duplicate",
        action="store_true",
        default=0,
        help="Allow duplicate entries",
    )

    parser.add_argument(
        "-f", "--file", type=str, help="The file path to the JSON data."
    )

    parser.add_argument(
        "-k",
        "--key",
        type=str,
        help="Path to the Firebase Service Key.",
        default="service_key.json",
    )

    upload_options = parser.add_argument_group("Upload Options")

    upload_options.add_argument(
        "-e",
        "--emulator",
        action="store_true",
        default=0,
        help="Use Firebase Emulator",
    )

    parser.add_argument(
        "-c", "--collection", type=str, help="The collection to upload the data to."
    )

    args = parser.parse_args()

    with open(args.file) as json_data:
        docs = json.load(json_data)

        match args.run_config:
            case "validate":
                validate(docs, args.duplicate)
            case "upload":
                firebase = firebase_scripts.FirebaseService(args.emulator, args.key)
                firebase.upload(docs, args.collection)


if __name__ == "__main__":
    main()
