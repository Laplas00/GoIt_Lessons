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


def save_applicant_data(source, output=None):
    for di in source:
        print(di)
        for key in di:
            print(key)
            with open(output, 'a') as file_out:
                if key == 'eng':
                    file_out.write(str(di[key])+"\n")
                else:
                    file_out.write(str(di[key])+",")

        print('----done')


save_applicant_data(
    mylist, '/Users/black/Documents/GoIt_Lessons/module6/8_14/output')
