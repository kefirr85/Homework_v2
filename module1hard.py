grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
st_srt = sorted(students)

students_sr_bal = {st_srt: sum(grades) / len(grades)
                   for st_srt, grades in zip(st_srt, grades)}
print(students_sr_bal)
