import xml.etree.ElementTree as ET
import argparse
import os
import json
import csv
import datetime


def jprint(obj):
    """
        The function is to create a formatted string of the Python JSON object.
    """
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', help='Parsed file type')
parser.add_argument('-p', '--path', help='Parsed file path')
args = parser.parse_args()

file_path = os.path.abspath(args.path)
result = dict()
result_path = os.path.abspath('./python_task_data/output')
result['file_name'] = args.path.split('/')[-1]

if args.type.lower() == 'csv':
    result_path = os.path.join(result_path, 'csv')
    csv_data = csv.reader(file_path, delimiter=',')
    line_count = 0
    for row in csv_data:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1

if args.type.lower() == 'xml':
    tree = ET.parse(file_path)
    root = tree.getroot()
    result_path = os.path.join(result_path, 'xml')

    trans = root.find('Transaction')

    for i, customer in enumerate(trans.findall('Customer')):
        result['transaction'] = list()
        result['transaction'].append({'customer': customer.attrib})

        date = trans.find('Date')
        result['transaction'][i]['date'] = date.text

        name = customer.find('Name').text
        result['transaction'][i]['customer']['name'] = name

        address = customer.find('Address').text
        result['transaction'][i]['customer']['address'] = address

        phone = customer.find('Phone').text
        result['transaction'][i]['customer']['phone'] = phone

        units = customer.find('Units')
        auto = units.find('Auto')

        result['transaction'][i]['vehicles'] = list()

        for j, vehicle in enumerate(auto.findall('Vehicle')):
            result['transaction'][i]['vehicles'].append(dict())

            vehicle_id = vehicle.attrib['id']
            result['transaction'][i]['vehicles'][j]['id'] = vehicle_id

            make = vehicle.find('Make').text
            result['transaction'][i]['vehicles'][j]['make'] = make

            vin_number = vehicle.find('VinNumber').text
            result['transaction'][i]['vehicles'][j]['vin_number'] = vin_number

            model_year = vehicle.find('ModelYear').text
            result['transaction'][i]['vehicles'][j]['model_year'] = model_year

    os.makedirs(result_path, exist_ok=True)
    ct = datetime.datetime.now()
    ts = str(ct.timestamp())
    result_path = os.path.join(result_path, f"{ts}_{result['file_name']}.json")
    with open(result_path, 'w') as results_file:
        json.dump(result, results_file, ensure_ascii=False, indent=4)

    # print('result =')
    # jprint(result)

