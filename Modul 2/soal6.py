class Manusia(object):
    """
        Membuat Class 'Manusia' dengan inisial 'nama'
    """
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Assalamualaikum, Namaku ',self.nama)
    def makan(self, x):
        print(self.nama,'baru saja selesai makan', x)
        self.keadaan = 'kenyang'
    def renang(self, y):
        print(self.nama,'baru saja selesai renang', y)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,z):
        return z*2

class siswaSMA(Manusia):
    """
        Membuat Class SiswaSMA
    """
    def __init__(self,nama,absen,jurusan):
        self.nama = nama
        self.absen = absen
        self.jurusan = jurusan
        self.ekskul = []
    def __str__(self):
        s = 'Nama saya '+str(self.nama)\
            +', nomor absen saya '+int(self.absen)\
            +', jurusan saya adalah '+str(self.jurusan)
        return s
    def ambilAbsen(self):
        return self.absen
    def ambiljurusan(self):
        return self.jurusan
    def hobi(self):
        return self.hobi
    def tambahhobi(self,a):
        self.hobi.append(a)
