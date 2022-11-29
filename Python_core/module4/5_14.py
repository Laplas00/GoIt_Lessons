def lookup_key(data, value):
    my_list = []
    for i in data:
        if value == data[i]:
            print(f"{value} == {i}")
            my_list.append(i)
        else:
            print(f"else{value} == {i}")
    return(my_list)


lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2)
