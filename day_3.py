
from os import X_OK


def binary_to_decimal(x):
    two = 1
    result = 0
    for i in x[::-1]:
        result += int(i)*two
        two *=2
    return result

data = open("C:/Users/alikr/Desktop/input.txt","r")
string = data.read()
list = string.split()
bit_length = len(list[0])
gamma = ""
epsilon = ""
for j in range(bit_length):
    one=0
    zero=0
    for i in list:
        if i[j] == "1":
            one += 1
        else:
            zero += 1
    if one> zero:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("Part 1:",binary_to_decimal(gamma)*binary_to_decimal(epsilon))

oxygen_gr = list.copy()
CO2_sr = list.copy()
for j in range(bit_length):
    temp = []
    one=0
    zero=0
    for i in oxygen_gr:
        if i[j] == "1":
            one += 1
        else:
            zero += 1
    if one >= zero:
        for i in oxygen_gr:
            if i[j]=="0":
                temp.append(i)
        for i in temp:
            if len(oxygen_gr) != 1:
                oxygen_gr.remove(i)
    else:
        for i in oxygen_gr:
            if i[j]=="1":
                temp.append(i)
        for i in temp:
            if len(oxygen_gr) != 1:
                oxygen_gr.remove(i)
    one=0
    zero=0
    temp = []
    for i in CO2_sr:
        if i[j] == "1":
            one += 1
        else:
            zero += 1
    if one >= zero:
        for i in CO2_sr:
            if i[j]=="1":
                temp.append(i)
        for i in temp:
            if len(CO2_sr) != 1:
                CO2_sr.remove(i)
    else:
        for i in CO2_sr:
            if i[j]=="0":
                temp.append(i)
        for i in temp:
            if len(CO2_sr) > 1:
                CO2_sr.remove(i)
print("Part 2:",binary_to_decimal(oxygen_gr[0])*binary_to_decimal(CO2_sr[0]))

