INFO_CATS_FILE = 'cats_information.txt'


def get_cats_info(path):
    list_of_cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.split(',')
                cat_age = cat_age.rstrip('\n')
                cat = {'id': cat_id, 'name': cat_name, 'age': cat_age}
                list_of_cats.append(cat)
        return list_of_cats
    except FileNotFoundError:
        return print(f'File {path} does not exist!')


if get_cats_info(INFO_CATS_FILE):
    print(get_cats_info(INFO_CATS_FILE))
