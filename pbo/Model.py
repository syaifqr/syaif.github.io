from DBConnector import DBConnect
from datetime import datetime

class Model:

    def __init__(self,table,column):
        self.table = table
        self.column = column

    def insertKaryawan(self):
        connection = DBConnect()
        nama = input("Masukkan nama karyawan : ")
        idUser = (input("Masukkan idUser : "))
        alamat = (input("Masukkan harga : "))
        jK = input("Jenis kelamin : ")
        query = "INSERT INTO "+self.table+" VALUES(idPegawai,'"+str(idUser)+"','"+nama+"','"+alamat+"','"+jK+"')"
        result = connection.executeInsert(query)

    def insertBarang(self):
        connection = DBConnect()
        nama = input("Masukkan nama barang : ")
        stok = (input("Masukkan stok : "))
        harga = (input("Masukkan harga : "))
        query = "INSERT INTO "+self.table+" VALUES(idBarang,'"+str(nama)+"','"+str(stok)+"','"+str(harga)+"')"
        result = connection.executeInsert(query)
    
    def getAllDataBarang(self):
        connection = DBConnect()
        query = "SELECT * from "+self.table
        result = connection.executeSelectBarang(query)
        return(result)
    
    def getAllDataKaryawan(self):
        connection = DBConnect()
        query = "SELECT * from "+self.table
        result = connection.executeSelectKaryawan(query)
        return(result)

    def getAllDataOrder(self):
        connection = DBConnect()
        query = "SELECT * from "+self.table
        result = connection.executeSelectOrder(query)
        return(result)

    def getSearchBarang(self):
        connection = DBConnect()
        inputan = input("Cari berdasarkan nama/id/stok/harga : ")
        query = "SELECT * from "+self.table+" where namaBarang ='"+inputan+"'"+" OR idBarang ='"+inputan+"'"+" OR stok ='"+inputan+"'"+" OR hargaBarang ='"+inputan+"'"
        result = connection.executeSelectBarang(query)
        return(result)

    def getSearchKaryawan(self):
        connection = DBConnect()
        inputan = input("Cari berdasarkan nama/id/jenis kelamin : ")
        query = "SELECT * from "+self.table+" where namaKaryawan ='"+inputan+"'"+" OR idPegawai ='"+inputan+"'"+" OR jenisKelamain ='"+inputan+"'"
        result = connection.executeSelectKaryawan(query)
        return(result)

    def updateMasuk(self):
        connection = DBConnect()
        inUse = input("Masukkan id: ")
        masuk = input("Masukkan barang : ")
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        query = "UPDATE barang SET stok = stok + "+masuk+" where idBarang= "+inUse
        result = connection.executeInsert(query)
        que = "INSERT INTO transaksi VALUES(idOrder,'"+inUse+"','"+masuk+"','masuk','"+(formatted_date)+"')"
        record = connection.executeInsertUpdate(que)

    def updateKeluar(self):
        connection = DBConnect()
        inUse = input("Masukkan id: ")
        keluar = input("Keluar barang : ")
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        query = "UPDATE barang SET stok = stok - "+keluar+" where idBarang= "+inUse
        result = connection.executeInsert(query)
        que = "INSERT INTO transaksi VALUES(idOrder,'"+inUse+"','"+keluar+"','masuk','"+(formatted_date)+"')"
        record = connection.executeInsertUpdate(que)


    def updateHarga(self):
        connection = DBConnect()
        inUse = input("Masukkan id: ")
        hargaBaru = input("Update Harga : ")
        query = "UPDATE barang SET hargaBarang = "+hargaBaru+" where idBarang= "+inUse
        result = connection.executeInsert(query)

    def delete(self):
        connection = DBConnect()
        inUse = input("Masukkan id data yang ingin dihapus: ")
        query = "DELETE from "+self.table+" where idBarang="+inUse
        print(query)
        result = connection.executeInsert(query)

    def getColumn(self):
        return self.column
    
    def getTable(self):
        return self.table
        