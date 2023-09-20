class kubus:
    ## method setter
    def setrusuk(self,rusuk):
        self.rusuk = rusuk

    ## method privat
    def volume(self):
        return self.rusuk**3
    
    ## method publik
    def tampilInfo(self):
        print("rusuk :", self.rusuk)
        print("volume :", self.volume())

cube = kubus()
cube.setrusuk(4)
cube.tampilInfo()