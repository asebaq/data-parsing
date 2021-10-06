# XML and CSV Parser
Parse XML and CSV files to JSON

# How to use
To use it clone this repo and install the required packages

`pip install -r requirements.txt`

XML to JSON

`python parser.py xml <xml file>`

Example:
`python parser.py xml file.xml`

For multiple files:
`python parser.py xml file1.xml file2.xml file3.xml`

CSV to JSON

`python parser.py csv <customer file> <vehicle file>`

Example:
`python parser.py csv customer.csv vehicles.csv`

For multiple files:
`python parser.py csv customer1.csv vehicles1.csv customer2.csv vehicles2.csv customer3.csv vehicles3.csv`
