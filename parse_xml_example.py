import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

# АТРИБУТ ОТДЕЛЬНОГО ЭЛЕМЕНТА
print('Item #2 attribute:')
print(root[0][1].attrib)

# АТРИБУТЫ ВСЕХ ЭЛЕМЕНТОВ
print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

# ДАННЫЕ ОТДЕЛЬНОГО ЭЛЕМЕНТА
print('\nItem #2 data:')
print(root[0][1].text)

# ДАННЫЕ ВСЕХ ЭЛЕМЕНТОВ
print('\nAll item data:')
for elem in root:
    for subelem in elem:
        print(subelem.text)
