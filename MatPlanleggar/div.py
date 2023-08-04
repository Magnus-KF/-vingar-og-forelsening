def transform_text_to_list(text):
    line_list = text.split('\n')
    return line_list
"""
def duplicate_check(choice):
    if choice in trash:
"""
ingredientDict = {}
def shopping_list_cleaner(shoppinglist):
    ingredientDict.clear()
    for meal in shoppinglist:
        for ingredient in meal:
            if ingredient == "" or ingredient == " ":
                continue
            elif ingredientDict.get(ingredient) is not None:
                ingredientDict[ingredient] +=1
            else:
                ingredientDict[ingredient] = 1
    return ingredientDict

