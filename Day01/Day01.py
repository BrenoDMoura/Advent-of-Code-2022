with open("Day01.txt", "r") as f:
    txt = f.readlines()

elfs = []
max = 0
lucena = []

#FILTRANDO \n:

for e in range(len(txt)):
    txt[e] = txt[e][:-1]
    
    if(txt[e] != ""):
        txt[e] = int(txt[e])
        #ATÉ AQUI FUNCIONA!
        max += txt[e]
    else:
        lucena.append(max)
        max = 0
        pass
    #ATÉ AQUI, O CÓDIGO EXIBE NA LISTA LUCENA,
    #QUANTAS CALORIAS OS ELFOS POSSUEM 

#SOLUTION FOR PART 1:
# maior = 0

# for e in range(len(lucena)):
#     if(lucena[e] > maior):
#         maior = lucena[e]

#print(maior)  71471
#####################

##### PART 2 SOLUTION #####
lucena.sort(reverse=True)
for e in range(3):
    print(lucena[e](sum))
###########################

