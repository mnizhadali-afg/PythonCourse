## ------------ Cube List Generator -------------- ##
## The program takes list of inputs from (1 - 10) and
## outputs the Cube of each numbers. ################

def cubeList(values):
    for i in range(len(values)):
        values[i] **= 3

numbers = [1,2,3,4,5,6,7,8,9,10]

cubeList(numbers)
print(numbers)