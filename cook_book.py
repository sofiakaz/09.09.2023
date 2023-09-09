def add_meal(line):
    one_meal = {}
    meal_details = line.split('\n')
    one_meal[meal_details[0]] = []
    num_of_ingredients = int(meal_details[1])
    for i in range(2, 2 + num_of_ingredients):
        one_ingredient = {}
        details = meal_details[i].split(" | ")
        one_ingredient["ingredient_name"] = details[0]
        one_ingredient["quantity"] = int(details[1])
        one_ingredient["measure"] = details[2]
        one_meal[meal_details[0]].append(one_ingredient)
    return one_meal

with open('ingredients.txt', encoding='utf-8') as f:
    recipe = f.read()
    cook_book = {}

    for line in recipe.split('\n\n'):
        meal = add_meal(line)
        cook_book.update(meal)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient["ingredient_name"]
                measure = ingredient["measure"]
                quantity = int(ingredient["quantity"]) * person_count

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]["quantity"] += quantity
                else:
                    shop_list[ingredient_name] = {"measure": measure, "quantity": quantity}

    return shop_list

print(cook_book)
dishes_to_cook = ['Запеченный картофель', 'Омлет']
person_count = 2
result = get_shop_list_by_dishes(dishes_to_cook, person_count)
print(result)










        

