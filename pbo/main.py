from Login import Login
from Karyawan import Karyawan
from Barang import Barang
from masuk import admin
from transaksi import Transaksi
from DBConnector import DBConnect
from getpass import getpass

def main():
    while(True):
        print("Program")
        print("""
        1. Insert Data
        2. Lihat Data
        3. Update Data
        4. Delete Data
        5. Search Data
        """)
        inputan = int(input("Masukan Pilihan : "))
        if  inputan == 1:
            print("""
            1. Tambahkan data barang
            2. Tambahkan data karyawan
            """)
            inp = int(input("Masukkan pilihan : "))
            if inp == 1:
                insertDataBarang()
            else:
                insertDataKaryawan()
        elif inputan == 2:
            print("""
            1. Tampilkan data barang
            2. Tampilkan data karyawan
            3. Tampilkan data order
            """)
            inp = int(input("Masukkan pilihan : "))
            if inp == 1:
                showDataBarang()
            elif inp == 2:
                showDataKaryawan()
            else:
                showDataOrder()
        elif inputan == 3:
            print("""
            1. Update barang masuk
            2. Update barang keluar
            3. Update harga
            """)
            inp = int(input("Masukkan pilihan : "))
            if inp == 1:
                showDataBarang()
                updateMasukData()
            elif inp == 2:
                showDataBarang()
                updateKeluarData()
            else:
                showDataBarang()
                updateHargaData()
        elif inputan == 4:
            deleteData()
        else:
            print("""
            1. Cari data barang
            2. Cari data karyawan
            """)
            inp = int(input("Masukkan pilihan : "))
            if inp == 1:
                searchBarang()
            else:
                searchKaryawan()
        finish = input("Selesai? (Y/N) ")
        if finish == 'Y':
            break

def insertDataBarang():
    print("INSERT DATA BARANG")
    model = Barang()
    model.insertBarang()

def insertDataKaryawan():
    print("INSERT DATA KARYAWAN")
    model = Barang()
    model.insertKaryawan()

def showDataBarang():
    model = Barang()
    data = model.getAllDataBarang()
    print(data)

def showDataKaryawan():
    model = Karyawan()
    data = model.getAllDataKaryawan()
    print(data)

def showDataOrder():
    model = Transaksi()
    data = model.getAllDataOrder()
    print(data)

def searchBarang():
    model = Barang()
    data = model.getSearchBarang()
    print(data)

def searchKaryawan():
    model = Karyawan()
    data = model.getSearchKaryawan()
    print(data)

def updateMasukData():
    model = Barang()
    model = Transaksi()
    model.updateMasuk()

def updateKeluarData():
    model = Barang()
    model.updateKeluar()

def updateHargaData():
    model = Barang()
    model.updateHarga()

def deleteData():
    model = Barang()
    model.delete()

def loginDB(Database):
    userLg = input("Masukkan username : ")
    pwLg = getpass("Masukkan password : ")
    query = "SELECT * FROM login WHERE username=%s"
    val=(userLg,)
    adm = Database.executeLogin(query,val)
    if adm:
        objAdmin = admin(adm[1], adm[2])
        if pwLg==adm[2]:
            print("Selamat Datang",objAdmin.username)
            main()
        else:
            print("Password yang Anda masukkan salah, coba lagi ")
            loginDB(Database)
    else:
        print("Username yang Anda masukkan salah, coba lagi ")
        loginDB(Database)

Database=DBConnect()
loginDB(Database)








