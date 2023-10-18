# algorithm

allergens = []
# allergens
def allergen_filter(allergen_list: list):
    allergen_list_as_set = set()
    for allergen in allergen_list:
        allergen_list.add(allergen)
    
    name_list = []
    for recipe_name in allergens:
        allergen_in_recipe = False
        for allergen in recipe_name[allergens]:
            if allergen in allergen_list_as_set:
                allergen_in_recipe = True
        if not allergen_in_recipe:
            name_list.append(recipe_name)

    return name_list