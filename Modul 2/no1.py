
#1a
class Pesan (object):
    def __init__(self, sebuahString):
        self.teks= sebuahString
    def cetakIn(self):
        print(self.teks)
    def cetakhurufbesar(self):
        print(str.upper(self.teks))
    def cetakhurufkecil(self):
        print(str.lower(self.teks))
    def jumlah(self):
        return len(self.teks)
    def cetakjumlahkarakter(self):
        print('Kalimat mempunyai', len(self.teks), 'karakter')
    def perbarui(self, StringNew):
        self.teks= StringNew
    def apakahTerkandung(self, kata):
        if str(kata) in self.teks:
            return True
        else:
            return False

#1b
    def hitungKonsonan(self):
        hk= 'aiueo'
        hasil=0
        for i in self.teks:
            if i not in hk and i!='':
                hasil +=1
        return hasil

#1c
    def hitungVokal(self):
        hv= 'aiueo'
        hasil=0
        for i in self.teks:
            if i in hv:
                hasil +=1
        return hasil
