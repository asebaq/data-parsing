import argparse
import os
from utils import save_json
from Parser import XMLParser

# USAGE
# python parser.py xml <file>
# python parser.py xml ./python_task_data/input_data/xml/file1.xml


def main(args):

    result_path = './output/'
    result_path = os.path.join(result_path, args.type)
    # Parse XML files and save the output to json files
    for xml_file in args.files:
        xml_parser = XMLParser(xml_file, args.type)
        result = xml_parser.parse()
        save_json(result_path, result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='Parsed file type')
    parser.add_argument('files', nargs='+', help='Parsed files path')
    args = parser.parse_args()
    main(args)

