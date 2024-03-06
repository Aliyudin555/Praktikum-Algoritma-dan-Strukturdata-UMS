class Manusia (object):
    def __init__(self, nama):
        self.nama=nama
    def ucapkansalam(self):
        print('Salam, namaku' , self.nama)
    def makan (self,s):
        print("Saya baru saja makan",s)
        self.keadaan = 'kenyang'
    def olahraga (self, k):
        print('saya baru saja Latihan' ,k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua (self,n):
        return n*2
    
class Mahasiswa(Manusia):
        def __init__(self,nama,NIM,kota,us):
            self.nama   =   nama
            self.NIM   =   NIM
            self.kotaTinggal = kota
            self.uangSaku = us
            self.MK=[]
        def __str__(self):
            s  =   self.nama   +   ',   NIM   '  +   str(self.NIM)\
                 + '. Tinggal di ' + self.kotaTinggal \
                 +   '.   Uang   saku   Rp   '  +   str(self.uangSaku)\
                 +   'tiap   bulannya.'
            return s
        def ambilNama(self):
            return  self.nama
        def ambilNIM(self):
            return  self.NIM
        def ambilkotaTinggal(self):
            return self.kotaTinggal
        def perbaruikotaTinggal(self,x):
            self.kotaTinggal = x
        def ambilUangSaku(self):
            return self.uangSaku
        def tambahUangsaku(self,y):
            self.uangSaku += int(y)
        def makan(self,s):
            print("Saya   baru   saja   makan",s,"sambil   belajar.")
            self.keadaan   ='kenyang'
        def listKuliah(self):
            return self.MK
        def ambilKuliah(self, x):
            self.MK.append(x)
        def hapusMK(self, x):
            self.MK.remove(x)

m9= Mahasiswa('Reza', 232, 'Surakarta', 100000)

print(m9.ambilkotaTinggal())
m9.perbaruikotaTinggal('Purwodadi')
print(m9.ambilkotaTinggal())

print(m9.ambilUangSaku())
m9.tambahUangsaku(200000)
print(m9.ambilUangSaku())
