def formatRupiah(x):
    x = str(x)
    if len(x) <= 3:
        return 'Rp' + x
    else:
        sisa = formatRupiah(x[:-3])
        angka = x[-3:]
        return sisa + '.' + angka

print(formatRupiah(1500)) 
print(formatRupiah(2560000))
print(formatRupiah(700000))