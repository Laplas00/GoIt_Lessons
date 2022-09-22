print("="*50)
mylist = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]


def save_applicant_data(source, output):
    result = []
    a = 0
    with open(output, "w") as f_out:
        for i in source:
            result.append(i["name"])
            result.append(i["specialty"])
            result.append(i["math"])
            result.append(i["lang"])
            result.append(i["eng"])
            result = [str(x) for x in result]
            for_output = ",".join(result)
            print(for_output)
            f_out.write(for_output)
            result = []
            if len(source) == a:
                break
            else:
                a += 1
                f_out.write("\n")
    return f"{'-'*50}\nRESULT IS - {result}"


print(save_applicant_data(
    mylist, "/Users/black/Documents/GoIt_Lessons/module6/train/output.txt"))
