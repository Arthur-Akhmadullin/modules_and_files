import xml.etree.ElementTree as ETree

data = ETree.Element('data')

itm_name = ETree.SubElement(data, 'name')
itm_sex = ETree.SubElement(data, 'sex')
itm_age = ETree.SubElement(data, 'age')
itm_langs = ETree.SubElement(data, 'languages')
itm_pc = ETree.SubElement(data, 'pc')

itm_l1 = ETree.SubElement(itm_langs, 'language')
itm_l1.text = '9'
itm_l1.set('name','Python')
itm_l1 = ETree.SubElement(itm_langs, 'language')
itm_l1.text = '7'
itm_l1.set('name','Java')

itm_pc1 = ETree.SubElement(itm_pc, 'pc_item')
itm_pc1.text = 'Linux'
itm_pc1.set('name','os')
itm_pc1 = ETree.SubElement(itm_pc, 'pc_item')
itm_pc1.text = 'ram'
itm_pc1.set('name','64')

serialze = ETree.tostring(data, encoding='utf8', method='xml').decode()
fil = open("items.xml", "w")
fil.write(serialze)

for lng in itm_langs.findall('language'):
    print(lng.attrib, lng.text)

item = data.find('pc')
for subitem in item.findall('pc_item'):
    print(subitem.text)

for item in data.iter():
    print(item.tag, item.text, item.attrib)

parent_map = {c.tag:p.tag for p in root.iter() for c in p}