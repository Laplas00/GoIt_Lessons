

guys = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

print("\n")
# def formatted_grades(students):
#     grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
#     a = 1
#     count = len(students) + 1
#     mylist = []
#     for ball in grades:
#         for name in students:
#             mylist.append("{:>4}|{:<10}|{:^5}|{:^5}".format(a,name, students[name], grades[students[name]]))
#             students.pop(name)
#             break    
#         a += 1
#         if a == count:
#             break
#         else:
#             continue
#     return mylist

# for name in students:
#     print(a, ball, grades[ball], name, students[name],"\n")
#     students.pop(name)
#     break

a = 1
            
def formatted_grades(students):
    grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    global a 
    


    a+=1



for el in formatted_grades(guys):
    print(el)



#    1|Nick      |  A  |  5
#    2|Olga      |  B  |  5
#    3|Mike      | FX  |  2
#    4|Anna      |  C  |  4