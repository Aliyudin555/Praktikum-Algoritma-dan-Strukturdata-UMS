x=input("Masukan angka:")
bilangan=int(x)
b_prima="bilangan Prima"
b_bukan="bukan bilangan prima"
jumlah= 0

if bilangan== 2:
    teks= b_prima
else:
    for i in range(2, bilangan+1):
        if bilangan % i == 0:
            stat = 1
            jumlah= jumlah + stat
if jumlah == 1:
    teks= b_prima
else:
    teks= b_bukan
    
print("%s adalah " %x+ teks)