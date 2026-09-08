xd = "Jere no teni niun brillo"
chori = xd.find("t")

print(chori)
#OUTPUT: 8  

trap_capos = xd.find("J", 12, 18)
print(trap_capos)
#OUTPUT: -1 
#("J no está en el indice dado (12 a 18)")