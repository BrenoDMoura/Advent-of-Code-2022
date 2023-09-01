with open("Day01.txt", "r") as f:
    txt = f.readlines()

elfs = []
max = 0
calories = []

#FILTRANDO \n:

for e in range(len(txt)):
    txt[e] = txt[e][:-1]
    
    if(txt[e] != ""):
        txt[e] = int(txt[e])
        #ATÉ AQUI FUNCIONA!
        max += txt[e]
    else:
        calories.append(max)
        max = 0
        pass
    #ATÉ AQUI, O CÓDIGO EXIBE NA LISTA LUCENA,
    #QUANTAS CALORIAS OS ELFOS POSSUEM 

#SOLUTION FOR PART 1:
bigger = 0

# for e in range(len(calories)):
#     if(calories[e] > bigger):
#         bigger = calories[e]

#print(bigger)  71471
#####################

##### PART 2 SOLUTION #####
calories.sort(reverse=True)
for e in range(3):
    bigger += calories[e]

print(bigger)
###########################

