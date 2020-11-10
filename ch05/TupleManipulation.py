## ------------- Tuple in Python ------------- ##
## The program shows how to create and manipulate
## Tuples in Python. ############################

studentTuple = ('Amanda', 'Grey', ['Chemestry', 'Biology', 'Physics', 'Literature'], [98, 89, 85, 100])
firstName, lastName, subjects, grades = studentTuple

print(f'{firstName} {lastName} got this scores: ')
for i in range(len(subjects)):
    print('\t', subjects[i], ': ', grades[i])
