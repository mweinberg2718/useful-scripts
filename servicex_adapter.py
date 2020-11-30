from datetime import datetime
import requests


MAX_RETRIES = 3


class ServiceXAdapter:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def post_status_update(self, status_msg, severity="info"):
        success = False
        attempts = 0
        while not success and attempts < MAX_RETRIES:
            try:
                requests.post(self.endpoint + "/status", data={
                    "timestamp": datetime.now().isoformat(),
                    "source": "DID Finder",
                    "severity": severity,
                    "info": status_msg
                })
                success = True
            except requests.exceptions.ConnectionError:
                print("Connection err. Retry")
                attempts += 1
        if not success:
            print("******** Failed to write status message")
            print("******** Continuing")

    def put_file_add(self, file_info):
        success = False
        attempts = 0
        while not success and attempts < MAX_RETRIES:
            try:
                requests.put(self.endpoint + "/files", json={
                    "timestamp": datetime.now().isoformat(),
                    "file_path": file_info['file_path'],
                    'adler32': file_info['adler32'],
                    'file_size': file_info['file_size'],
                    'file_events': file_info['file_events']
                })
                success = True
            except requests.exceptions.ConnectionError:
                print("Connection err. Retry")
                attempts += 1
        if not success:
            print("******** Failed to add new file")
            print("******** Continuing")

    def post_preflight_check(self, file_entry):
        success = False
        attempts = 0
        while not success and attempts < MAX_RETRIES:
            try:
                requests.post(self.endpoint + "/preflight", json={
                    'file_path': file_entry['file_path']
                })
                success = True
            except requests.exceptions.ConnectionError:
                print("Connection err. Retry")
                attempts += 1
        if not success:
            print("******** Failed to write preflight check")
            print("******** Continuing")

    def put_fileset_complete(self, summary):
        success = False
        attempts = 0
        while not success and attempts < MAX_RETRIES:
            try:
                requests.put(self.endpoint + "/complete", json=summary)
                success = True
            except requests.exceptions.ConnectionError:
                print("Connection err. Retry")
                attempts += 1
        if not success:
            print("******** Failed to write fileset complete")
            print("******** Continuing")
