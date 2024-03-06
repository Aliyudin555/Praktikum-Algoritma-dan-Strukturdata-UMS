class Mahasiswa(object):
    """Class Interaktif"""
    def __init__(self, nama,nim,kota,us):
        self.nama = nama
        self.NIM = nim
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama+', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilKotaTinggal(self):
        print(self.kotaTinggal)
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self, tbhSaku):
        self.uangSaku = self.uangSaku + tbhSaku
        return self.uangSaku

nama = input("Masukan Nama: ")
NIM = input("Masukan NIM: ")
kota = input ("Masukan Kota: ")
us = int(input("Masukan Uang Saku: "))
x = Mahasiswa(nama, NIM, kota, us)
print(x)
