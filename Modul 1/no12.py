import random
r = random.randint (1,100)
print("Permainan tebak angka." + "\n"+
      "Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")
b = "Masukkan tebakan ke-"
f = ":> "
c=1
d = str(c)
for i in range(1,100):
    e = (b+d+f)
    a = int(input(e))
    c+=1
    d = str(c)
    if(a < r):
        print("Itu terlalu kecil. Coba lagi.")
    elif(a > r):
        print("Itu terlalu besar. Coba lagi.")
    elif(a == r):
        print("Ya. Anda benar")
        break
