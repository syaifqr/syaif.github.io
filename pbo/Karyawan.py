from Model import Model

class Karyawan(Model):

    def __init__(self):
        super().__init__("karyawan",["idUser","namaKaryawan","alamat","jenisKelamin"])

    