from pathlib import Path

INFO_CATS_FILE = Path('cats_information.txt')


def get_cats_info(path):
    list_of_cats = []
    if path.exists():
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.split(',')
                cat_age = cat_age.rstrip('\n')
                cat = {'id': cat_id, 'name': cat_name, 'age': cat_age}
                list_of_cats.append(cat)
        return list_of_cats
    else:
        print(f'File {path} not exist!')


print(get_cats_info(INFO_CATS_FILE))
