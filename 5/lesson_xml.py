import xml.etree.ElementTree as ETree

xml1 = ETree.parse('demo.xml')
root = xml1.getroot()

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
    text_list = []
    tag_value(root, "pc_item", text_list)
    print("Список значений:", text_list)

    print("Количество узлов с заданным атрибутом =", attrib_value(root, "name"))