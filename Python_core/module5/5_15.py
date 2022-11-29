def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers(list_phones):
    numbers = {"UA": [],
               "JP": [],
               "TW": [],
               "SG": []}

    print(list_phones)
    for number in list_phones:
        print(number)
        # Тут делаем проверкук на начало тф
        # Присваиваем значения каждой стране

        japan = number.find("81", 0, 2)
        singapore = number.find("65", 0, 2)
        taiwan = number.find("886", 0, 3)
        ukraine = number.find("380", 0, 3)
        if japan != -1:
            numbers["JP"].append(number)
            print(numbers["JP"])
        elif singapore != -1:
            numbers["SG"].append(number)
            print("singapore")
        elif taiwan != -1:
            numbers["TW"].append(number)
            print("taiwan")
        elif ukraine != -1:
            numbers["UA"].append(number)
            print("ukraine")
    return numbers


get_phone_numbers(['81998759405', '818765347', '8867658976', '657658976'])
