print ('+-----------------------------------------------')
print ('  Program  Menghitung Pembelian Sederhana       ')
print ('      ')
print ('      ')
print ('      Kelompok 21 Shift 2                      ')
print ('  1. Setyo Adhi Purwito     / 21120117130077   ')
print ('  2. Fajrul Falah          / 21120117120033    ')
print ('-----------------------------------------------')
print ('\n')

from inputan import inputan
from fungsi import fungsi

pembeli = inputan()
pembeli.inputnama()
pembeli.hargabarang()
pembeli.jumlah()
pembeli.uang()


Fungsipembeli = fungsi()
Fungsipembeli.totalharga()
Fungsipembeli.kemb()

print('')
print('===========================================')
print('             TOKO SUKA FAJRUL ')
print('===========================================')
print('Nama Barang              : ',pembeli.nama[0] )  
print('')
print('Harga Barang             : ','Rp.',pembeli.harga[0])
print('')
print('Jumlah Barang            : ', pembeli.jumlahbarang[0])
print('')
print('Total Harga              : ','Rp.',Fungsipembeli.total[0])
print('')
print('Uang Anda                : ','Rp.',Fungsipembeli.uangku[0])
print('')
print('Kembalian                : ','Rp.',Fungsipembeli.kembalian[0])
print('')
