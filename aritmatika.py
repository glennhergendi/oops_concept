class operasiaritmatika:
    #-- deklarasi property:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    #-- Operasi aritmatika dasar:
    def bilangan1(self):
        return self.X
    def bilangan2(self):
        return self.Y  
    def tambah(self):
        return self.X + self.Y
    def kurang(self):
        return self.X - self.Y
    def kali(self):
        return self.X * self.Y
    def bagi(self):
        return self.X / self.Y
    def sisa(self):
        return self.X % self.Y
#-- program utama & pemanggilan
X = int(input("masukan bilangan pertama :"))
Y = int(input("masukan bilangan kedua :"))
op = operasiaritmatika(X,Y)
bil1 = op.bilangan1()
bil2 = op.bilangan2()
optambah = op.tambah()
opkurang = op.kurang()
opkali = op.kali()
opbagi = op.bagi()
opsisa = op.sisa()
print('-- Operasi aritmatika sederhana --')
print(' Dengan OOP bahasa python ')
print('==============================================')
print('bilangan kesatu(X) = ', bil1)
print('bilangan kedua(Y) = ', bil2)
print("penjumlahan 2 bilangan = ", optambah)
print("pengurangan 2 bilangan = ", opkurang)
print("perkalian 2 bilangan = ", opkali)
print("pembagian 2 bilangan = ", opbagi)
print("sisa pembagian 2 bilangan = ", opsisa)
print("==============================================")

