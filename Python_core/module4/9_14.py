def is_valid_pin_codes(pin_codes):
    if pin_codes == []:
        return False
    my_list = []
    for i in pin_codes:
        for ri in i:
            try:
                ri == int(ri)
                print(f'{ri} == int({ri})')
                pass
            except:
                return False
        print(i)
        if type(i) == str:
            print(f"{i} is str")
            if len(i) == 4:
                print(f"len {i} is 4")
                if i not in my_list:
                    my_list.append(i)
                else:
                    return False
            else:
                return False
        else:
            print("not&")
            return False
    print(my_list)
    return True


is_valid_pin_codes(['1101', '9034', '001a'])
