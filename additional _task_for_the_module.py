grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_student = sorted(students)
journal = {}
result = sum (grades[0])/len (grades[0])
result1 = sum (grades[1])/len (grades[1])
result2 = sum (grades[2])/len (grades[2])
result3 = sum (grades[3])/len (grades[3])
result4 = sum (grades[4])/len (grades[4])
journal [sort_student[0]] = result
journal [sort_student[1]] = result1
journal [sort_student[2]] = result2
journal [sort_student[3]] = result3
journal [sort_student[4]] = result4
print(journal)