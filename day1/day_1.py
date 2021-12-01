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