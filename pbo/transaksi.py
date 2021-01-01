from Model import Model

class Transaksi(Model):
    
    def __init__(self):
        super().__init__("transaksi",["idBarang","jumlah","masuk/keluar","time"])