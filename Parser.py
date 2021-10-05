import os
import xml.etree.ElementTree as ET


class Parser:
    def __init__(self, file_name, file_type=None):
        if not os.path.isfile(file_name):
            raise FileNotFoundError
        self.file_name = os.path.abspath(file_name)

        if file_type is None:
            _, file_type = os.path.splitext(file_name)
        self.file_type = file_type
        self.result = dict()

    def parse(self):
        raise NotImplementedError


class XMLParser(Parser):
    def parse(self):
        tree = ET.parse(self.file_name)
        root = tree.getroot()
        trans = root.find('Transaction')
        self.result['file_name'] = self.file_name.split('/')[-1]

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
    def parse(self):
        pass