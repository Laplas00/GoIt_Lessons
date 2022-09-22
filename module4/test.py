def hobby_dict():

    print("Программа что бы отслеживать хобби")
    my_dict = {}
    while True:
        name = input('Введите назваание хобби: ')
        if name == "exit":
            break
        time = input("Введите год в котором вы этим занимались: ")
        if time == "exit":
            break
        my_dict[name] = time
        print(my_dict)
        for i in my_dict:
            print(my_dict[i])


mama = "lola_loi,mzf_haha"

print(mama[:])
