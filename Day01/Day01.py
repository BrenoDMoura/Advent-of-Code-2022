with open("Day01.txt", "r") as f:
    txt = f.readlines()

elfs = []
max = 0
calories = []

#REMOVING \n:

for e in range(len(txt)):
    txt[e] = txt[e][:-1]
    
    if(txt[e] != ""):
        txt[e] = int(txt[e])
        max += txt[e]
    else:
        calories.append(max)
        max = 0
        pass
    

#SOLUTION FOR PART 1:
#bigger = 0

calories.sort(reverse=True)
print(calories[0]) #71471

# for e in range(len(calories)):
#     if(calories[e] > bigger):
#         bigger = calories[e]

#print(bigger)  71471
#####################

##### PART 2 SOLUTION ##### 211189
#
#print(sum(calories[:3]))
###########################

