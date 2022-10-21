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


file = open('/Users/black/Documents/GoIt_Lessons/module6/8_14/output', 'w')


def save_applicant_data(source, output):
    result = ''
    a = 1
    print(len(source))
    with open(output, 'w') as path:
        for di in source:
            for key in di:
                result += str(di[key])
                if key == 'eng':
                    if len(source) != a:
                        result += '\n'
                else:
                    result += ','
            a += 1
            path.writelines(result)
            result = ''

        print('----done')


save_applicant_data(
    mylist, '/Users/black/Documents/GoIt_Lessons/module6/8_14/output')
