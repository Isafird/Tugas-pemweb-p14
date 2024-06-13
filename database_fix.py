import os
import mysql.connector

def init_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    
    if mydb.is_connected():
        print("Database berhasil terhubung")
    else:
        print("Gagal terhubung ke database")
    
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS tk_p14")
    print("Database berhasil dibuat atau sudah ada")
    
    mydb.close()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="tk_p14"
    )
    
    cursor = mydb.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS ytta(tahun VARCHAR(10) PRIMARY KEY, judul VARCHAR(30), genre VARCHAR(20), studio VARCHAR(20))""")
    print("Tabel berhasil dibuat atau sudah ada")

    return mydb, cursor

mydb, cursor = init_db()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("===Database Film===")
    print("[1] Insert Data")
    print("[2] Tampilkan Data")
    print("[3] Update Data")
    print("[4] Hapus Data")
    print("[5] Cari Data")
    print("[0] Exit")
    print("------------------")

    menu = input("Pilih Menu: ")
    if menu == '1':
        menu1()
    elif menu == '2':
        menu2()
    elif menu == '3':
        menu3()
    elif menu == '4':
        menu4()
    elif menu == '5':
        menu5()
    elif menu == '0':
        print("Terima kasih Telah Berkunjung")
        exit()
    else:
        print("Menu yang anda masukkan tidak ada, masukkan pilihan yang tersedia")
        kembali()

def menu1():
    while True:
        clear_screen()
        print("===Insert Data===")
        tahun = input("Masukkan Tahun (atau ketik 'kembali' untuk kembali ke menu): ").lower()
        if tahun == 'kembali':
            break
        judul = input("Masukkan Judul: ")
        genre = input("Masukkan Genre: ")
        studio = input("Masukkan Studio: ")
        
        sql = "INSERT INTO ytta (tahun, judul, genre, studio) VALUES (%s, %s, %s, %s)"
        val = (tahun, judul, genre, studio)
        
        cursor.execute(sql, val)
        mydb.commit()
        print("Data berhasil ditambahkan!")
    
    kembali()

def menu2():
    clear_screen()
    print("===Tampilkan Data===")
    cursor.execute("SELECT * FROM ytta")
    results = cursor.fetchall()
    for row in results:
        print(f"tahun: {row[0]}, judul: {row[1]}, genre: {row[2]}, studio: {row[3]}")
    kembali()

def menu3():
    while True:
        clear_screen()
        print("===Update Data===")
        tahun_asal = input("Masukkan tahun dari data yang akan dirubah (atau ketik 'kembali' untuk kembali ke menu): ").lower()
        if tahun_asal == 'kembali':
            break
        tahun = input("Masukkan tahun baru: ")
        judul = input("Masukkan judul baru: ")
        genre = input("Masukkan genre baru: ")
        studio = input("Masukkan studio baru: ")
        
        sql = "UPDATE ytta SET tahun = %s, judul = %s, genre = %s, studio = %s WHERE tahun = %s"
        val = (tahun, judul, genre, studio, tahun_asal)
        
        cursor.execute(sql, val)
        mydb.commit()
        print("Data berhasil diupdate!")
    
    kembali()

def menu4():
    while True:
        clear_screen()
        print("===Hapus Data===")
        tahun = input("Masukkan tahun dari data yang ingin dihapus (atau ketik 'kembali' untuk kembali ke menu): ").lower()
        if tahun == 'kembali':
            break
        
        sql = "DELETE FROM ytta WHERE tahun = %s"
        val = (tahun,)
        
        cursor.execute(sql, val)
        mydb.commit()
        print("Data berhasil dihapus!")
    
    kembali()

def menu5():
    clear_screen()
    print("===Cari Data===")
    cari = input("Masukkan data yang ingin dicari: ")
    sql = "SELECT * FROM ytta WHERE tahun LIKE %s OR judul LIKE %s OR genre LIKE %s"
    val = (f"%{cari}%", f"%{cari}%", f"%{cari}%")
    
    cursor.execute(sql, val)
    results = cursor.fetchall()
    if not results:
        print("Data tidak ditemukan.")
    else:
        for row in results:
            print(f"tahun: {row[0]}, judul: {row[1]}, genre: {row[2]}, studio: {row[3]}")
    
    kembali()

def kembali():
    input("Tekan Enter untuk kembali ke menu...")
    show_menu()

while True:
    show_menu()
