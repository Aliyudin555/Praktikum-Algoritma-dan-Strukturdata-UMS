def cetakprima(angka):
    for num in range(2, angka+1):
        if num > 1:
            for i in range(2,num):
                if(num%i)== 0:
                    break
            else:
                print(num)
cetakprima(1000)
