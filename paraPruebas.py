#nucleotido
a = ['N','N','N','N','NH']
#Guanina
g = ['N','N','N','NH','N','O']
#Timina
t = ['N','O','N','O','CH']
#Citosina
c = ['N','N','O','NH']

posibiA = [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,t,g,c,a,a,a,a,a,a,a]
print(len(posibiA))

    
    tree = []
    for tr in range(len(cinco)):
        if cinco[tr] == base[0]:
            tree.append(respuesta[0])
        if cinco[tr] == base[1]:
            tree.append(respuesta[1])
        if cinco[tr] == base[2]:
            tree.append(respuesta[2])
        if cinco[tr] == base[3]:
            tree.append(respuesta[3])