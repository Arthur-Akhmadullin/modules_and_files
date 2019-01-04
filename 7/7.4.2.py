import os.path

def delete_catalog(cat_path):
    if os.path.isdir(cat_path):
        for root, dirs, files in os.walk(cat_path):
            if dirs == []:
                for f in files:
                    os.remove(root+"/"+f)
                os.rmdir(root)
            else:
                print("Каталог не пустой")
                break

delete_catalog("structure\delete_1")