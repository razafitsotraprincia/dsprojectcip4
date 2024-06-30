import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('UNdata_Export_20240624_084602358.xml')
root = tree.getroot()

# Extract data and convert to a list of dictionaries
data = []
year = ''
fertility_rate = ''
record_data = {}
# Select the years and the corresponding fertility rate from date source
for record in root.iter():
    for key, value in record.attrib.items():
        if key == 'name' and value == 'Year(s)':
            year = record.text
        if key == 'name' and value == 'Value' and record.text is not None:
            fertility_rate = float(record.text)
            record_data[year] = fertility_rate
    data.append(record_data)
# Extracting the dictionary from the list
data_list = data[0]
# Sorting the dictionary by keys (year)
sorted_data = dict(sorted(data_list.items()))
# Print the sorted list with the year and the fertlity rate
print(sorted_data)
    