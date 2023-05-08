from linkml_runtime.utils.schemaview import SchemaView
import os
import requests
import csv
import time
from typing import List

INFORES_TSV = os.path.join('infores_catalog_nodes.tsv')


def is_valid_urls(url: str) -> bool:
    retries = 3
    for i in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
            else:
                print(f"Response status code: {response.status_code}. Retrying...")
                time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"Exception: {e}. Retrying...")
            time.sleep(1)
    return False


class InformationResource:

    def __init__(self) -> None:
        infores_map = {}

    def dump(self):
        raise NotImplementedError

    def validate(self):
        infores_map = {}
        with open(INFORES_TSV, 'r') as tsv_file:
            reader = csv.reader(tsv_file, delimiter='\t')
            for line in reader:
                if line[2] == 'id' or line[3] == '':
                    continue
                if line[2] == 'infores:athena' \
                        or line[2] == 'infores:isb-wellness' \
                        or line[0] == 'deprecated' \
                        or line[2] == 'infores:isb-incov' \
                        or line[2] == 'infores:preppi'  \
                        or line[2] == 'infores:ttd' \
                        or line[2] == 'infores:flybase' \
                        or is_valid_urls(line[3]):
                    infores_map[line[2]] = {
                        "status": line[0],
                        "name": line[1],
                        "url": line[3],
                        "synonyms": line[4],
                        "description": line[5],
                    }
                else:
                    print(line)
                    print("Invalid infores URL:" + line[3] + " for " + line[2])
                    raise ValueError("Invalid infores URL")


if __name__ == "__main__":
    InformationResource().validate()
