class Mobil:
    def init(self, warna, merk, nomor_polisi):
        self.warna = warna
        self.merk = merk
        self.nomor_polisi = nomor_polisi

def start(self):
    print("mobil sedang dinyalakan")

def stop(self):
    print("mobil sedang dimatikan")

def accelerate(self):
    print("mobil sedang dipercepat")

mobil_pertama = Mobil("hitam", "toyota", "abc123")
mobil_kedua = Mobil("merah", "honda", "def456")

print("atribut mobil pertama:")
print("warna:", mobil_pertama.warna)
print("merk:", mobil_pertama.merk)
print("nomor polisi:", mobil_pertama.nomor_polisi)
print("\natribut mobil kedua")
print("Warna:", mobil_kedua.warna)

print("Merk:", mobil_kedua.merk)

print("Nomor Polisi:", mobil_kedua.nomor_polisi)

print("\nMemanggil metode dari objek mobil pertama:")

mobil_pertama.start()

mobil_pertama.accelerate()

mobil_pertama.stop()