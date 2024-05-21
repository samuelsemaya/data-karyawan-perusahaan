from tabulate import tabulate
from .database import *
from .validation import validation_alpha,validation_digit,validation_umur,validation_kelamin
from .read_data import read_data
from main import main_data
from .clear_screen import clear

def update_data():
    while True:
        ubah_input = validation_digit('Pilih nomor yang mau diubah data: ')
        if ubah_input < 1 or ubah_input > len(data):
            print('data tidak ditemukan')
        else:
            update_item = [data[ubah_input-1]]
            print(tabulate(update_item,headers='keys',tablefmt='fancy_grid'))
            konfirmasi = validation_alpha('Yakin ingin mengubah data? (y/n) atau \'u\' ke menu utama: ')
            if konfirmasi.lower() == 'y':
                ubah_nama = validation_alpha('Masukkan nama: ')
                ubah_umur = validation_umur('Masukkan umur: ')
                ubah_kelamin = validation_kelamin('Masukkan jenis kelamin: ')
                ubah_alamat = validation_alpha('Masukkan alamat: ')
                ubah_divisi = validation_alpha('Masukkan divisi: ')
                ubah_level = validation_alpha('Masukkan level: ')
                ubah_jabatan = validation_alpha('Masukkan jabatan: ')
                ubah_gaji = validation_digit('Masukkan gaji: ')

                if ubah_divisi.lower() == 'it' or ubah_divisi.lower() == 'hrd':
                    ubah_divisi = ubah_divisi.upper()
                else:
                    ubah_divisi = ubah_divisi.capitalize()

                data[ubah_input-1]['Nama'] = ubah_nama.title()
                data[ubah_input-1]['Umur'] = ubah_umur
                data[ubah_input-1]['Jenis Kelamin'] = ubah_kelamin.capitalize()
                data[ubah_input-1]['Alamat'] = ubah_alamat.title()
                data[ubah_input-1]['Divisi'] = ubah_divisi
                data[ubah_input-1]['Level'] = ubah_level.title()
                data[ubah_input-1]['Jabatan'] = ubah_jabatan.title()
                data[ubah_input-1]['Gaji'] = ubah_gaji
                clear()
                print(f'\n')
                print(f'{'Data berhasil diubah':^115}'.upper())
                print(f'\n\n')
                print(tabulate(data,headers='keys',tablefmt='fancy_grid'))
            elif konfirmasi.lower() == 'n':
                clear()
                read_data()
                update_data()
            elif konfirmasi.lower() == 'u':
                clear()
                main_data()

            for index, value in enumerate(data,1):
                value['No.'] = index
            break