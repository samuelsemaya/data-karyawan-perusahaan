from tabulate import tabulate
from .database import *
from .validation import validation_alpha
from .clear_screen import clear

def sorted_data():

    header_table = ['No.', 'NIK', 'Nama', 'Umur', 'Jenis Kelamin', 'Alamat', 'Divisi', 'Level', 'Jabatan', 'Gaji']

    while True:
        try:
            input_key = validation_alpha('Masukkan nama kolom yang ingin diurutkan: ').capitalize()

            if input_key not in header_table:
                raise ValueError

            order_choice = None

            while order_choice not in [1, 2]:
                try:
                    order_choice = int(input('Pilih urutan pengurutan: 1. Ascending 2. Descending (1-2): '))
                    if order_choice not in [1, 2]:
                        raise ValueError('Input urutan tidak valid. Silakan coba lagi.')
                except:
                    print('Masukkan hanya angka !')

            sorted_data = sorted(data, key=lambda x: x[input_key], reverse=(order_choice == 2))

            table_data = []

            for item in sorted_data:
                table_data.append([item.get(key, '') for key in item])

            clear()

            print(tabulate(table_data, headers=header_table, tablefmt='fancy_grid'))
            break

        except:
            print('Input kolom tidak valid. Silakan coba lagi.')