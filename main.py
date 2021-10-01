numbers = [0,1,0,3,12]
aux = []
aux2 = []

for x in range(len(numbers)):
    if numbers[x] == 0:
        aux.append(numbers[x])
    else:
        aux2.append(numbers[x])

print(aux)
print(aux2)


aux2 += aux

print(aux2)
