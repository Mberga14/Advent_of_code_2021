import os

measure = 0
with open("input.txt", "r") as file:
    t1 = file.readline()
    while True:
        t2 = file.readline()
        if t1 not in "" and t2 not in "" and int(t1) < int(t2):
            measure = measure + 1
        
        t1=t2
        if not t2:
            print(measure)
            break



measure = 0
with open("input.txt", "r") as file:
    first_sum = 0
    second_sum = 0
    t1 = file.readline()
    t2 = file.readline()
    while True:
        t3 = file.readline()
        if not t3:
            print(measure-1)
            break

        second_sum = int(t1) + int(t2) + int(t3)
        print(first_sum, second_sum)

        if second_sum > first_sum:
            measure +=1

        first_sum = second_sum
        
        t1=t2
        t2=t3