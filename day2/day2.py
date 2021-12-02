


instructions = {
    "horizontal" : 0,
    "vertical" : 0,
    "aim" : 0,
}

with open("input.txt", "r") as file:
    while True:
        input = file.readline()
        if not input:
            print(instructions["horizontal"] * instructions["vertical"])
            break
        
        command, number = input.split(" ")
        if command == "down":
            instructions["aim"] += int(number)
        elif command == "up":
            instructions["aim"] -= int(number)
        else:
            instructions["horizontal"] += int(number)
            instructions["vertical"] += instructions["aim"] * int(number)

        print(instructions)