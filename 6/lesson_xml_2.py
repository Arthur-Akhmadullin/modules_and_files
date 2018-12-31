import xml.etree.ElementTree as ETree

xml1 = ETree.parse('demo_full.xml')
root = xml1.getroot()

def find_nodes(tag):
    array = []
    try:
        for item in root.iter(tag):
            if item.tag == tag:
                array.append([item.attrib, item.text])
        if array == []:
            print("Не найдено")
    except Exception:
        print("Что-то пошло не так...")
    return(array)

def find_parent(child_node):
    array_parent = []
    for parent in root.iter():
        for child in parent:
            if child.tag == child_node:
                array_parent.append(parent.tag)
    return(array_parent)

def delete_child_node(tag):
    try:
        for nodes in root.iter():
            for item in nodes.findall(tag):
                nodes.remove(item)
    except Exception:
        print("Упс...")
    return (root)


if __name__ == "__main__":

    # Напишите функцию, которая формирует список всех узлов по заданному тегу
    # независимо от их глубины в XML-документе. На вход функция получает корневой узел.
    tag = "language"
    print(find_nodes(tag))

    #Напишите функцию, которая находит родителя заданного узла.
    print(find_parent("language"))

    #Напишите функцию, которая удаляет все узлы по заданному тегу независимо
    # от их глубины в XML-документе.
    delete_child_node("language")
    xml1.write("demo_full_new.xml")