class hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("hewan ini mengeluarkan suara.")
    
class Kucing(hewan):
    def suara(self):
        print("meong")

class Anjing(hewan):
    def suara(self):
        print("guk guk!")

animal = hewan("hewan")
kucing = Kucing("kucing")
anjing = Anjing("anjing")

animal.suara()
kucing.suara()
animal.suara()
anjing.suara()