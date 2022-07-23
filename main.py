import os


def create_cook_book():
    path = os.path.join(os.getcwd(), "recipes.txt")
    cook_book = dict()
    with open(path, encoding="utf-8") as file:
        text = file.read()
        dish_list = text.split("\n\n")
        file.seek(0, 0)
        for dish in dish_list:
            key = file.readline().replace("\n", "")
            component_count = int(file.readline())
            cook_book[key] = []
            for component in range(component_count):
                component_list = file.readline().replace("\n", "").split(" | ")
                cook_book[key].append({'ingredient_name': component_list[0], 'quantity': int(component_list[1]),
                                       'measure': component_list[2]})
            file.readline()
    print(cook_book)


create_cook_book()
