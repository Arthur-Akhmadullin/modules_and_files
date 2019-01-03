import os.path

def structure_catalog(arr_dir, arr_file):
    for root, dirs, files in os.walk('structure'):
        for dir in dirs:
            arr_dir.append(dir)
        for file in files:
            arr_file.append(file)
    return(arr_dir, arr_file)

array_dirs = []
array_files = []
structure_catalog(array_dirs, array_files)

print("СПИСОК КАТАЛОГОВ:")
for dir in array_dirs:
    print(dir)

print("СПИСОК ФАЙЛОВ:")
for file in array_files:
    print(file)
