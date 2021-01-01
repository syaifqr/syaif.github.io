from Model import Model

class Barang(Model):
    
    def __init__(self):
        super().__init__("barang",["namaBarang","stok","hargaBarang"])
