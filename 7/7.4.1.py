import os.path

def structure_catalog(arr_dir, arr_file):
    for root, dirs, files in os.walk('structure'):
        for d in dirs:
            arr_dir.append(d)
        for f in files:
            arr_file.append(f)
    return(arr_dir, arr_file)

array_dirs = []
array_files = []
structure_catalog(array_dirs, array_files)

print("СПИСОК КАТАЛОГОВ:")
for d in array_dirs:
    print(d)

print("СПИСОК ФАЙЛОВ:")
for f in array_files:
    print(f)
