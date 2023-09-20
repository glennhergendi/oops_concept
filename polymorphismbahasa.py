class indonesia:
    def ibukota(self):
        print("jakarta adalah ibukota indonesia")

    def bahasa(self):
        print("bahasa indonesia adalah bahasa nasional indonesia")

class malaysia:
    def ibukota(self):
        print("kuala lumpur adalah ibukota malaysia")

    def bahasa(self):
        print("bahasa melayu adalah bahasa nasional malaysya")

def informasi(negara):
    negara.ibukota()
    negara.bahasa()

ind = indonesia()
mas = malaysia()

informasi(ind)
informasi(mas)