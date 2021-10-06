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
        xml_parser = XMLParser(args.files[0], args.format)
        result = xml_parser.parse()

    elif args.format.lower() == 'csv':
        csv_parser = CSVParser(args.files[0], args.files[1], args.format)
        result = csv_parser.parse()
    else:
        print("File format is not supported")
        return
    save_json(result_path, result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('format', help='Parsed file type')
    parser.add_argument('files', nargs='+', help='Parsed files path')
    args = parser.parse_args()
    main(args)
