def get_recipe(path, search_id):
    with open(path, "r") as file:
        result = {}
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip().split(',')
            if search_id == line[0]:
                result.update(
                    {"id": line[0], "name": line[1], "ingredients": line[2::]})
                print(result)
                print("nashel")
                break
            else:
                continue
        if result == {}:
            return None
        else:
            return result


print(get_recipe("/Users/black/Documents/GoIt_Lessons/module6/train/recipies.txt",
      "60b90c3b13067a15887e1ae4"))


# {
#     'id': '60b90c3b13067a15887e1ae4',
#     'name': ' Watermelon Cucumber Salad',
#     'ingredients': [
#         ' 1 large seedless watermelon',
#         ' 12 leaves fresh mint',
#         ' 1 cup crumbled feta cheese'
#     ]
# }


# {
#     "id": "60b90c3b13067a15887e1ae4",
#     "name": "Watermelon Cucumber Salad",
#     "ingredients": [
#         "1 large seedless watermelon",
#         "12 leaves fresh mint",
#         "1 cup crumbled feta cheese",
#     ],
# }
