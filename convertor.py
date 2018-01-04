from src.json2xml import Json2xml
data = Json2xml.fromurl('https://coderwall.com/vinitcool76.json').data
data_object = Json2xml(data)
xml_data = data_object.json2xml() #xml output

with open('star.xml', 'w') as file:
    file.write(xml_data)
