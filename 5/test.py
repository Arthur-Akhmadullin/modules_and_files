import xml.etree.ElementTree as ETree
from lesson_xml import tag_value, attrib_value

xml1 = ETree.parse('demo.xml')
root = xml1.getroot()


array_root = []
array_language = []
array_pc = []
for i in range(len(root) - 2):
    array_root.append(root[i].text)
for i in range(len(root[3])):
    array_language.append(root[3][i].text)
for i in range(len(root[4])):
    array_pc.append(root[4][i].text)


mas = []
test_value_1 = "pc_item"
test_value_2 = "asdf"
test_value_3 = "age"

tag_value(root, test_value_1, mas)
if array_pc == mas:
    print("test tag_value OK")
mas.clear()

tag_value(root, test_value_2, mas)
if len(mas) == 0:
    print("test tag_value OK")
mas.clear()

tag_value(root, test_value_3, mas)
if array_root[1] == mas[0]:
    print("test tag_value OK")


if attrib_value(root, "name") == 7:
    print("test attrib_value is OK")

if attrib_value(root, "asdf") == 0:
    print("test attrib_value is OK")
