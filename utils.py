import json
import os
import datetime


def jprint(obj):
    """
        The function is to create a formatted string of the Python JSON object
    """
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def save_json(file_dir, file_data):
    """
        The function is to save Dict object to a JSON file
    """
    os.makedirs(file_dir, exist_ok=True)
    ct = datetime.datetime.now()
    ts = str(ct.timestamp())
    file_name = file_data['file_name']
    if 'xml' in file_data['file_name']:
        file_name = file_data['file_name'][:-4]
    result_path = os.path.join(file_dir, f"{ts}_{file_name}.json")
    with open(result_path, 'w') as results_file:
        json.dump(file_data, results_file, ensure_ascii=False, indent=4)
