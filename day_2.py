data = open("C:/Users/alikr/Desktop/input.txt","r")
string = data.read()
list = string.split()
forward = 0
depth = 0
for i,a in enumerate(list):
    if a == "forward":
        forward += int(list[i+1])
    if a == "down":
        depth += int(list[i+1])
    if a == "up":
        depth -= int(list[i+1])

print("Part 1:",forward*depth)

forward = 0
depth = 0
aim = 0
for i,a in enumerate(list):
    if a == "forward":
        forward += int(list[i+1])
        depth += aim*int(list[i+1])
    if a == "down":
        aim += int(list[i+1])
    if a == "up":
        aim -= int(list[i+1])

print("Part 2:", forward*depth)
