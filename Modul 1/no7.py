def faktorisasiprima(angka):
    list= []
    loop= 2
    while loop <= angka:
        if(angka % loop) ==0:
            angka /= loop
            list.append(loop)
        else:
            loop+=1
    return list
print(faktorisasiprima(10))
print(faktorisasiprima(120))
print(faktorisasiprima(19))
    
