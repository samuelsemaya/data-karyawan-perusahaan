from tabulate import tabulate
from .database import *
from .validation import validation_digit,validation_alpha
from .read_data import read_data
from main import main_data
from .clear_screen import clear

def delete_data():
    while True:
        menu_delete = validation_digit('Masukkan Nomor yang ingin di hapus: ')
        if menu_delete < 1 or menu_delete > len(data):
            print('data tidak ditemukan')
        else:
            delete_item = [data[menu_delete - 1]]
            print(tabulate(delete_item,headers='keys',tablefmt='fancy_grid'))
            konfirmasi = validation_alpha('Yakin ingin menghapus data? (y/n) atau \'u\' ke menu utama: ')
            if konfirmasi.lower() == 'y':
                del data[menu_delete - 1]
                clear()
                print(f'\n')
                print(f'{'Data berhasil dihapus':^115}'.upper())
                print(f'\n\n')
            elif konfirmasi.lower() == 'n':
                clear()
                read_data()
                delete_data()
            elif konfirmasi.lower() == 'u':
                clear()
                main_data()

            for index, value in enumerate(data,1):
                value['No.'] = index
            break