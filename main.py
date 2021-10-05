import argparse
import os
import json
import datetime
from utils import jprint
from Parser import XMLParser


def main(args):

    xml_parser = XMLParser(args.path, args.type)
    result = xml_parser.parse()

    result_path = './python_task_data/output/xml'
    os.makedirs(result_path, exist_ok=True)
    ct = datetime.datetime.now()
    ts = str(ct.timestamp())
    result_path = os.path.join(result_path, f"{ts}_{result['file_name']}.json")

    with open(result_path, 'w') as results_file:
        json.dump(result, results_file, ensure_ascii=False, indent=4)

    # print('result =')
    # jprint(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', help='Parsed file type')
    parser.add_argument('-p', '--path', help='Parsed file path')
    args = parser.parse_args()
    main(args)

