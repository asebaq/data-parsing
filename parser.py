#!/usr/bin/python3
import argparse
import os
from utils import save_json, get_database
from Parser import CSVParser, XMLParser


# python parser.py csv <customer file> <vehicle file>
# python parser.py csv ./python_task_data/input_data/csv/customers.csv ./python_task_data/input_data/csv/vehicles.csv
# python parser.py xml <xml file>
# python parser.py xml ./python_task_data/input_data/xml/file1.xml


def main(args):
    result_path = os.path.abspath('./output')
    result_path = os.path.join(result_path, args.format.lower())
    db_config_file = './db_config.ini'
    trufla_db = get_database(db_config_file)
    if args.format.lower() == 'xml':
        xml_col = trufla_db["xml"]
        for xml_file in args.files:
            xml_parser = XMLParser(xml_file, args.format)
            result = xml_parser.parse()
            save_json(result_path, result)
            xml_col.insert_one(result)

    elif args.format.lower() == 'csv':
        csv_col = trufla_db["csv"]
        for i in range(0, len(args.files) - 1, 2):
            csv_parser = CSVParser(args.files[i], args.files[i + 1], args.format)
            result = csv_parser.parse()
            save_json(result_path, result)
            csv_col.insert_one(result)

    else:
        print("File format is not supported")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('format', help='Parsed file type')
    parser.add_argument('files', nargs='+', help='Parsed files path')
    args = parser.parse_args()
    main(args)
