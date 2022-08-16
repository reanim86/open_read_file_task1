with open('recipes.txt', encoding='utf-8') as file:

    def add_ingridients():
        numbers_ingridients = int(file.readline().strip())
        ingridients = []
        while numbers_ingridients != 0:
            ingr = file.readline().strip().split(' | ')
            ingridients.append({'ingredient_name': ingr[0], 'quantity': int(ingr[1]), 'measure': ingr[2]})
            numbers_ingridients -= 1
        return ingridients

    cook_book = {}
    while True:
        dish = file.readline().strip()
        cook_book[dish] = add_ingridients()
        empty_str = file.readline()
        if not empty_str:
            break

    print(cook_book)

