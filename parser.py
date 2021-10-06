import argparse
import os
from utils import save_json
from Parser import XMLParser


# python parser.py xml <file>
# python parser.py xml ./python_task_data/input_data/xml/file1.xml

def main(args):

    result_path = './output/'
    result_path = os.path.join(result_path, args.type)

    for xml_file in args.path:
        xml_parser = XMLParser(xml_file, args.type)
        result = xml_parser.parse()
        save_json(result_path, result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='Parsed file type')
    parser.add_argument('path', nargs='+', help='Parsed files path')
    args = parser.parse_args()
    main(args)

