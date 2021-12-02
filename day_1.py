data = open("C:/Users/alikr/Desktop/input.txt","r")
string = data.read()
list = string.split()
count = 0
temp = int(list[0])
for i in list[1:]:
    i = int(i)
    if i>temp:
        count+=1
    temp = i
print("Part 1:",count)
list_sum = []
for i in range(len(list[:-2])):
    list_sum.append(int(list[i])+int(list[i+1])+int(list[i+2]))

count = 0
temp = int(list_sum[0])
for i in list_sum:
    if i>temp:
        count+=1
    temp = i
print(count)

