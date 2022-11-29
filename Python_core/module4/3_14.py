def format_ingredients(items):
    if len(items) <= 1:
        return "".join(items)
    else:
        items.insert(-1, " and ")
    for i in range(len(items)):
        if items[i+1] == " and ":
            break
        else:
            if items[i] == ", ":
                continue
            else:
                items.insert(i + 1, ", ")

    return("".join(items))


print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))

# тушить - stew
# варить - weld
