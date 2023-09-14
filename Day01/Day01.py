with open("Day01.txt", "r") as f:
    txt = f.readlines()

elfs = []
Sum = 0
calories = []

#REMOVING \n:

for e in range(len(txt)):
    txt[e] = txt[e][:-1]
    
    if(txt[e] != ""):
        txt[e] = int(txt[e])
        Sum += txt[e]
    else:
        calories.append(Sum)
        Sum = 0
    
#SOLUTION FOR PART 1:
calories.sort(reverse=True)
print(calories[0]) #71471
##############################

##### PART 2 SOLUTION ##### 211189
print(sum(calories[:3]))
###########################