class Mahasiswa(object):
    """
        Membuat metode menghapus mata kuliah dari ListKuliah
    """
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = []
    def __str__(self):
        s=self.nama+', NIM'+str(self.nim)\
           +'. Tinggal di '+self.kotaTinggal\
           +'. Uang Saku Rp. '+str(self.uangSaku)\
           +'tiap bulannya.'
        return s
    def listKuliah(self):
        return self.listKuliah
    def ambilKuliah(self, matkul):
        self.listKuliah.append(matkul)
    def hapusKuliah(self,matkul):
        self.listKuliah.remove(matkul)