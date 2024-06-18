<div align="center">
<H1>firebase-scripts</h1>

<img src="https://img.shields.io/badge/firebase-%23039BE5.svg?style=for-the-badge&logo=firebase" alt="firebase logo"/>
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python logo"/>

A set of utility scripts to quickly interact with Firebase Firestore databases.
</div>

## Key Features

- Validate JSON files
- Convert CSV files to JSON objects
- Upload JSON files as docs to Firebase

## Setup

### Configure Environment

```bash
python3 -m venv venv 
# MacOS / Linux
source venv/bin/activate
# CMD
venv/Scripts/activate.bat
# Powershell
venv/Scripts/Activate.ps1

# Install requirements
pip install -r requirements.txt
```

#### [Firebase Emulator][firebase-emulator]

It is possible for this script to be used with Firebase Emulator so that test environments can be setup or the data can be validated before uploading to Firebase.

To configure Firebase Emulator:

```bash
# Initialise Firebase Emulators
firebase init emulators
# Start Emulator
firebase emulators:start
# OPTIONAL - run the emulator whilst saving state
firebase emulators:start --import .env --export-on-exit .env
```

To configure the script for working with the Firebase Emulator, create a `.env` file at the root of the project and add the following line:

```bash
export FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"
```

Where the IP address corresponds to the one configured in the emulator.

## Usage

```
❯ python3 main.py
usage: main.py [-h] [-d] [-f FILE] [-k KEY] [-e] [-c COLLECTION] {validate,upload}

A set of utility scripts to quickly interact with Firebase Firestore databases.

positional arguments:
  {validate,upload}     validate = Validate the JSON, upload = Write the JSON to firestore,

options:
  -h, --help            show this help message and exit
  -d, --duplicate       Allow duplicate entries
  -f FILE, --file FILE  The file path to the JSON data.
  -k KEY, --key KEY     Path to the Firebase Service Key.
  -c COLLECTION, --collection COLLECTION
                        The collection to upload the data to.

Upload Options:
  -e, --emulator        Use Firebase Emulator
```


<!-- MARKDOWN LINKS & IMAGES -->
[firebase-emulator]: https://firebase.google.com/docs/emulator-suite