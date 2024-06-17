import json

from utils.terminal import TColors


def check_duplicates(docs) -> None:
    temp_docs = []
    for doc in docs:
        if doc in temp_docs:
            print(f"doc: {doc} already present in list")
        temp_docs.append(doc)
    print("No Duplicates found")


def validate(docs, duplicates: bool) -> bool:
    if not duplicates:
        check_duplicates(docs)
    print(f"{TColors.OKGREEN}Docs are valid.{TColors.ENDC}")
    return True


if __name__ == "__main__":
    with open("assets/prompts.json") as json_data:
        docs = json.load(json_data)
        check_duplicates(docs)
