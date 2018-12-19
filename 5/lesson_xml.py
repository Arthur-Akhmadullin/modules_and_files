import xml.etree.ElementTree as ETree

xml1 = ETree.parse('demo.xml')
root = xml1.getroot()

def show_nodes(i):
    array = []
    for j in range(len(root[i])):
        array.append([root[i][j].tag, root[i][j].attrib["name"], root[i][j].text])
    return(array)


def tag_value(node, tagname, array):
    for i in range(len(node)):
        if node[i].tag == tagname:
            array.append(node[i].text)
        if len(node[i]) > 0:
            tag_value(node[i], tagname, array)
    return(array)


def attrib_value(node, attribname):
    sum = 0
    for i in range(len(node)):
        if attribname in node[i].attrib.keys():
            sum += 1
        if len(node[i]) > 0:
            sum += attrib_value(node[i], attribname)
    return(sum)


if __name__ == '__main__':
    # Задание 5.3.1 - выводим содержание узлов language и pc
    print("Содержимое узла:")
    for items in show_nodes(3):
        print(items)
    print("Содержимое узла:")
    for items in show_nodes(4):
        print(items)

    print("------------------------------------")
    # Задание 5.3.2 - Список значений для конкретного тега
    text_list = []
    tag = "pc_item"
    tag_value(root, tag, text_list)
    print("Список значений:", text_list)

    print("------------------------------------")
    # Задание 5.3.3 - Количестов узлов
    print("Количество узлов с заданным атрибутом =", attrib_value(root, "name"))