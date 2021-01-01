import mysql.connector
from mysql.connector import Error
import texttable

class DBConnect:
    def __init__(self):
        self.connection  = None

    def executeInsert(self,query):
        try:
            self.connection = mysql.connector.connect(host="localhost",database="perusahaan",username="root",password="Abgtua789")
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                print("success")
        except Error as e:
            print(e)

    def executeInsertUpdate(self,que):
        try:
            self.connection = mysql.connector.connect(host="localhost",database="perusahaan",username="root",password="Abgtua789")
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(que)
                self.connection.commit()
                print("success")
        except Error as e:
            print(e)

    def executeSelectBarang(self,query):
        try:
            self.connection = mysql.connector.connect(host="localhost",database="perusahaan",username="root",password="Abgtua789")
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                if cursor.rowcount <= 0:
                    print("Data tidak ditemukan")
                else:
                    tabel = texttable.Texttable(0)
                    tabel.set_cols_align(["l","l","l","l"])
                    tabel.set_cols_dtype(["a","a","a","a"])
                    tabel.set_cols_valign(["m","m","m","m"])
                    tabel.add_rows([["id barang","nama barang","stok","harga"]])
                    for data in record:
                        tabel.add_row([data[0],data[1],data[2],data[3]])
                    print(tabel.draw())
                return "success"
        except Error as e:
            print(e)
    
    def executeSelectKaryawan(self,query):
        try:
            self.connection = mysql.connector.connect(host="localhost",database="perusahaan",username="root",password="Abgtua789")
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                if cursor.rowcount <= 0:
                    print("Data tidak ditemukan")
                else:
                    tabel = texttable.Texttable(0)
                    tabel.set_cols_align(["l","l","l","l"])
                    tabel.set_cols_dtype(["a","a","a","a"])
                    tabel.set_cols_valign(["m","m","m","m"])
                    tabel.add_rows([["Id Pegawai","Id User","nama karyawan","alamat","jenis kelamin"]])
                    for data in record:
                        tabel.add_row([data[0],data[1],data[2],data[3]])
                    print(tabel.draw())
                return "success"
        except Error as e:
            print(e)

    def executeSelectOrder(self,query):
        try:
            self.connection = mysql.connector.connect(host="localhost",database="perusahaan",username="root",password="Abgtua789")
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                if cursor.rowcount <= 0:
                    print("Data tidak ditemukan")
                else:
                    tabel = texttable.Texttable(0)
                    tabel.set_cols_align(["l","l","l","l","l"])
                    tabel.set_cols_dtype(["a","a","a","a","a"])
                    tabel.set_cols_valign(["m","m","m","m","m"])
                    tabel.add_rows([["id order","id barang","jumlah","masuk/keluar","time"]])
                    for data in record:
                        tabel.add_row([data[0],data[1],data[2],data[3],data[4]])
                    print(tabel.draw())
                return "success"
        except Error as e:
            print(e)
    
    def executeLogin(self,query,val):
        try:
            self.connection = mysql.connector.connect(host="localhost",database="perusahaan",username="root",password="Abgtua789")
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query,val)
                return cursor.fetchone()
        except Error as e:
            print(e)

            



