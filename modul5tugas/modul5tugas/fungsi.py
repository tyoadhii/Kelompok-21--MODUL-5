from inputan import inputan
class fungsi(inputan):
    totalharga = []
    total = []
    kemb = []
    kembalian = []


    def __init__(self):
       print("")

    def totalharga(self):
        upah = int(inputan.harga[0]) * int(inputan.jumlahbarang[0])
        self.total.append(upah)
        return self.total
    
    def kemb(self):
        k =  int(inputan.uangku[0]) - int(fungsi.total[0])
        self.kembalian.append(k)
        return self.kembalian

