grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students= sorted(students)
grades_m=[sum(l)/len(l) for l in grades]
st_gr= dict(zip(students, grades_m))
print(st_gr)