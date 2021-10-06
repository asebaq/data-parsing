import os
import xml.etree.ElementTree as ET
import csv
import datetime


class Parser:
    """
        Parser abstract class
    """
    def __init__(self, file_name, file_type=None):
        # Do simple file validation
        if not os.path.isfile(file_name):
            raise FileNotFoundError
        self.file_name = os.path.abspath(file_name)

        # If type is none we can extract it
        if file_type is None:
            _, file_type = os.path.splitext(file_name)
        self.file_type = file_type
        self.result = dict()

    def parse(self):
        raise NotImplementedError

    # TODO: Add a validation function (To validate against missing fields)


class XMLParser(Parser):
    def parse(self):
        """
            Parse XML file into Dict object
            :return: Dict object
        """
        # Load XML file
        tree = ET.parse(self.file_name)
        root = tree.getroot()
        trans = root.find('Transaction')
        self.result['file_name'] = self.file_name.split('/')[-1]

        # Extract customers data
        for i, customer in enumerate(trans.findall('Customer')):
            self.result['transaction'] = list()
            self.result['transaction'].append({'customer': customer.attrib})

            date = trans.find('Date')
            self.result['transaction'][i]['date'] = date.text

            name = customer.find('Name').text
            self.result['transaction'][i]['customer']['name'] = name

            address = customer.find('Address').text
            self.result['transaction'][i]['customer']['address'] = address

            phone = customer.find('Phone').text
            self.result['transaction'][i]['customer']['phone'] = phone

            units = customer.find('Units')
            auto = units.find('Auto')

            self.result['transaction'][i]['vehicles'] = list()

            if auto is None:
                return self.result

            # Extract vehicles data
            for j, vehicle in enumerate(auto.findall('Vehicle')):
                self.result['transaction'][i]['vehicles'].append(dict())

                vehicle_id = vehicle.attrib['id']
                self.result['transaction'][i]['vehicles'][j]['id'] = vehicle_id

                make = vehicle.find('Make').text
                self.result['transaction'][i]['vehicles'][j]['make'] = make

                vin_number = vehicle.find('VinNumber').text
                self.result['transaction'][i]['vehicles'][j]['vin_number'] = vin_number

                model_year = vehicle.find('ModelYear').text
                self.result['transaction'][i]['vehicles'][j]['model_year'] = model_year
        return self.result


class CSVParser(Parser):
    """
        CSV Parser class
    """
    def __init__(self, file1_name, file2_name, file_type=None):
        super().__init__(file1_name, file_type)
        if not os.path.isfile(file2_name):
            raise FileNotFoundError
        self.file2_name = os.path.abspath(file2_name)

    def parse(self):
        """
            Parse CSV file into Dict object
            :return: Dict object
        """
        self.result['file_name'] = self.file_name.split('/')[-1] + '_' + self.file2_name.split('/')[-1]
        self.result['transaction'] = list()

        # Extract customers data
        with open(self.file_name, 'r', newline='') as csv_file1:
            customers_data = csv.DictReader(csv_file1)
            for i, row1 in enumerate(customers_data, start=1):
                idx = i - 1
                vehicles_count = -1
                self.result['transaction'].append(dict())
                date_time_obj = datetime.datetime.strptime(row1['date'], '%d/%m/%Y')
                self.result['transaction'][idx]['date'] = str(date_time_obj.date())
                del row1['date']

                self.result['transaction'][idx]['customer'] = dict(row1)
                self.result['transaction'][idx]['vehicles'] = list()
                # Extract vehicles data
                with open(self.file2_name, 'r', newline='') as csv_file2:
                    vehicles_data = csv.DictReader(csv_file2)
                    for j, row2 in enumerate(vehicles_data, start=1):
                        if row2['owner_id'] == self.result['transaction'][idx]['customer']['id']:
                            vehicles_count += 1
                            del row2["owner_id"]
                            self.result['transaction'][idx]['vehicles'].append(row2)
        return self.result
