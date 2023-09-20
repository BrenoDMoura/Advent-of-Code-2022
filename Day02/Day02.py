with open("Day02.txt", "r") as file:
    input = file.readlines()

result = []
me = []
opponent = []
points = 0

for e in range(len(input)):
    input[e] = input[e][:-1]

for e in input:
    separating = e.split()
    result.extend(separating)

opponent = result[::2]

for e in range(len(result)): 
    if(e % 2 != 0):
        me.append(result[e])

for e in range(len(me)):
    if(opponent[e] == "A" and me[e] == "X"):
        pass
