import random

for files in range(1,11):
    name_file = str(files) + '.txt'

    with open(name_file, 'tw', encoding='utf-8') as f:
        for j in range(0,2):
            f.write(str(random.randint(1,10)) + '\n')
        f.write(str(random.randint(1, 10)))
    f.close()