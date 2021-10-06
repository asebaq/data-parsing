import unittest
import os

from Parser import XMLParser, CSVParser
import json


class TestParser(unittest.TestCase):
    def test_xml_parsing(self):
        files = ['./python_task_data/input_data/xml/file1.xml',]
        gt_files = ['./python_task_data/output/xml/1623330410.13814_file1_enriched.json',]
        for i in range(len(files)):
            xml_parser = XMLParser(files[i], 'xml', True)
            result = xml_parser.parse()
            with open(gt_files[i], 'r') as gt_file:
                ground_truth = json.load(gt_file)
                self.assertEqual(result, ground_truth)

    def test_csv_parsing(self):
        files = ['./python_task_data/input_data/csv/customers.csv', './python_task_data/input_data/csv/vehicles.csv', ]
        gt_files = ['./python_task_data/output/csv/1631103367.0623286_customers.csv_vehicles.csv.json', '', ]
        for i in range(0, len(files)-1, 2):
            csv_parser = CSVParser(files[i], files[i + 1], 'csv', True)
            result = csv_parser.parse()
            with open(gt_files[i], 'r') as gt_file:
                ground_truth = json.load(gt_file)
                self.assertEqual(result, ground_truth)

