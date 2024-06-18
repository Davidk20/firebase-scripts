import csv
import json

from utils.terminal import TColors


def check_duplicates(docs) -> bool:
    """
    Check whether any the list of docs contains any duplicate records.

    Parameters
    ----------
    `docs`
        A JSON object containing the docs

    Returns
    -------
        `True` if the list contains duplicates
    """
    temp_docs = []
    for doc in docs:
        if doc in temp_docs:
            print(f"{TColors.FAIL}doc: {doc} already present in list.{TColors.ENDC}")
            return True
        temp_docs.append(doc)
    print(f"{TColors.OKGREEN}No Duplicates found.{TColors.ENDC}")
    return False


def validate(docs, allow_duplicates: bool) -> bool:
    """
    Runs all validation checks.

    Parameters
    ----------
    `docs`
        A JSON object containing the docs

    `allow_duplicates` : `bool`
        `True` if the validation should allow duplicates.

    Returns
    -------
        `True` if the JSON docs are valid.
    """
    if not allow_duplicates and check_duplicates(docs):
        print(f"{TColors.FAIL}Docs are invalid.{TColors.ENDC}")
        return False

    print(f"{TColors.OKGREEN}Docs are valid.{TColors.ENDC}")
    return True


def csv_to_json(csv_path: str):
    """
    Convert a CSV file to a JSON object.

    The first line of the CSV must contain the headers.

    Parameters
    ----------
    `csv_path` : `str`
        The path to the csv file.

    Returns
    -------
        A list of JSON objects generated from the CSV file.
    """
    json_data = []
    with open(csv_path, mode="r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for key, col in row.items():
                if col.lower() == "true":
                    row[key] = True
                elif col.lower() == "false":
                    row[key] = False
            json_data.append(row)
    return json_data


def pretty_print(data):
    """Print the JSON object formatted for user view."""
    print(json.dumps(data, indent=4))
