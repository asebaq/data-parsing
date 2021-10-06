import argparse
import os
from utils import save_json
from Parser import CSVParser, XMLParser


# python parser.py csv <customer file> <vehicle file>
# python parser.py csv ./python_task_data/input_data/csv/customers.csv ./python_task_data/input_data/csv/vehicles.csv


def main(args):
    result_path = os.path.abspath('./output')
    result_path = os.path.join(result_path, args.format.lower())

    if args.format.lower() == 'xml':
        for xml_file in args.files:
            xml_parser = XMLParser(xml_file, args.format)
            result = xml_parser.parse()
            save_json(result_path, result)

    elif args.format.lower() == 'csv':
        for i in range(0, len(args.files)-1, 2):
            csv_parser = CSVParser(args.files[i], args.files[i+1], args.format)
            result = csv_parser.parse()
            save_json(result_path, result)
    else:
        print("File format is not supported")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('format', help='Parsed file type')
    parser.add_argument('files', nargs='+', help='Parsed files path')
    args = parser.parse_args()
    main(args)
