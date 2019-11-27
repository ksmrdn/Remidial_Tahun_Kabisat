'''
ahun kabisat merupakan tahun yang mengalami penambahan satu 
hari dengan tujuan untuk menyesuaikan penanggalan dengan tahun astronomi. 
Dalam satu tahun tidak secara persis terdiri dari 365 hari, 
tetapi 365 hari 5 jam 48 menit 45,1814 detik. Jika hal ini tidak dihiraukan, 
maka setiap empat tahun akan kekurangan hampir 1 hari. 
Maka untuk mengkompensasi hal ini, setiap 4 tahun sekali, 
diberi 1 hari ekstra: 29 Februari.

Buatlah sebuah file python interaktif (.py) berisi sebuah function 
yang dapat menentukan suatu input dari user tergolong 
tahun kabisat atau tidak. Saat file dieksekusi, 
user diminta memasukkan angka tahun tertentu, 
kemudian akan muncul hasil yang menyatakan input user tersebut 
tergolong tahun kabisat atau tidak. 
'''

year = int(input("Masukkan Tahun: "))

def cekKabisat(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print('HASIL: TAHUN KABISAT')
            else:
                print('HASIL: BUKAN TAHUN KABISATt')
        else:
            print('HASIL: TAHUN KABISAT')
    else:
        print('HASIL: BUKAN TAHUN KABISAT')

cekKabisat(year)