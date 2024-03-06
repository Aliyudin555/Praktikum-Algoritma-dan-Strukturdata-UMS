#no 3a
def hurufVokal(kata):
    hv= ["a", "i","u","e","o","A","I","U","E","0"]
    hitung= 0
    for i in kata :
        if i in hv:
            hitung +=1
    jumlah= len(kata)
    print('(', jumlah, ',', hitung, ')')
print("huruf vokal:")
hurufVokal ('Surakarta')

#no 3b

def hurufKonsonan(kata):
    hv = ["a", "i","u","e","o","A","I","U","E","0"]
    konsonan= 0
    for i in kata :
        if i in hv:
            konsonan +=1
    jml=len(kata)
    print ("(", jml, ",", jml-konsonan, ")")
print('huruf konsonan')
hurufKonsonan('Surakarta')
