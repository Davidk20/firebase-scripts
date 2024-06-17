import sys
from pathlib import Path
from firebase_admin import credentials, firestore, initialize_app
from dotenv import load_dotenv

from utils.terminal import TColors


class FirebaseService:

    def __init__(self, emulator: bool, service_key_path: str) -> None:
        if not Path(service_key_path).exists():
            print(f"{TColors.FAIL}ERROR - Service Key cannot be found{TColors.ENDC}")
            sys.exit(1)

        cred = credentials.Certificate(service_key_path)
        initialize_app(cred)
        self.db = firestore.client()
        if emulator:
            load_dotenv()

    def upload(self, docs, collection: str):
        """Upload the data to Firebase."""
        for doc in docs:
            self.db.collection(collection).add(doc)

        print(f"{TColors.OKGREEN}{collection} data successfully uploaded to Firestore.{TColors.ENDC}")
