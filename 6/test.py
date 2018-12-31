from lesson_xml_2 import find_nodes, find_parent, delete_child_node, xml1
import xml.etree.ElementTree as ETree

def test_find_nodes(array, tag):
    if array == find_nodes(tag):
        return("TEST OK")
    else:
        return("TEST FAILED")


tag = "language"

array_find_nodes_1 = [[{'name': 'Python'}, '9'], [{'name': 'Java'}, '7'], [{'name': 'C#'}, '8'],
                      [{'name': 'Go'}, '790'], [{'name': 'Ruby'}, '800']]
array_find_nodes_2 = [[{'name': 'Python'}, '9'], [{'name': 'Java'}, '7'], [{'name': 'C#'}, '8']]
print(test_find_nodes(array_find_nodes_1, tag))
print(test_find_nodes(array_find_nodes_2, tag))

print("------------------------------")


def test_find_parent(array, tag):
    if array == find_parent(tag):
        return("TEST OK")
    else:
        return("TEST FAILED")


array_test_parent_1 = ['languages', 'languages', 'languages', 'pc_item', 'pc_item']
array_test_parent_2 = ['languages', 'pc_item']
print(test_find_parent(array_test_parent_1, tag))
print(test_find_parent(array_test_parent_2, tag))

print("------------------------------")


def test_delete_child_node(tag, k, i, j):
    delete_child_node(tag)
    xml1.write("demo_full_new.xml")
    xml_test = ETree.parse('demo_full_new.xml')
    root_test = xml_test.getroot()

    try:
        if len(root_test[k]) == 0:
            print("TEST OK")
        else:
            print("TEST FAILED")
        if len(root_test[i][j]) != 0:
            print("TEST OK")
        else:
            print("TEST FAILED")
    except Exception:
        print("Ошибка вводных данных для теста")

test_delete_child_node(tag, 3, 4, 2)