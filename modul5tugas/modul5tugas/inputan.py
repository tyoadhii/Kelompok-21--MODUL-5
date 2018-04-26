class inputan(object):
    nama = []
    harga = []
    jumlahbarang = []
    uangku = []

    def __init__(self):
        print("")
       
    def inputnama(self):
        a = input    ('Masukan Nama Barang            : ')
        print('')
        self.nama.append(a)
        return self.nama

    def hargabarang(self):
        b = input ('Masukan Harga Barang          : ')
        print('')
        self.harga.append(b)
        return self.harga

    def jumlah(self):
        c = int(input('Masukan Jumlah Barang         : '))
        print('')
        self.jumlahbarang.append(c)
        return self.jumlahbarang

    def uang(self):
        d= int(input('Uang Anda     : '))
        print('')
        self.uangku.append(d)
        return self.uangku