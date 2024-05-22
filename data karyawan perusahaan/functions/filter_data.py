from tabulate import tabulate
from .database import *
from .validation import validation_umur,validation_alpha,validation_digit

def filter_data():
    while True:
        criteria = input('Masukkan nama kolom yang ingin di filter: ')
        filtered_data = []

        if criteria.lower() == 'nama':
            name_to_filter = validation_alpha('masukkan nama yang ingin di filter: ').lower()
            filtered_data = [item for item in data if name_to_filter in item.get('Nama').lower()]
            if filtered_data:
                print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid'))
                break
            else:
                print('Tidak ada data yang cocok dengan kriteria nama tersebut.')
                
        if criteria == 'Umur'.lower():
            age_to_filter = validation_umur('masukkan umur yang ingin di filter: ')
            filtered_data = [item for item in data if item.get('Umur') == age_to_filter]
            if filtered_data:
                print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid'))
                break
            else:
                print('Tidak ada data yang cocok dengan kriteria umur tersebut.')
            

        elif criteria.lower() == 'jenis kelamin':
            gender_to_filter = validation_alpha('Masukkan jenis kelamin yang ingin di filter: ')
            filtered_data = [item for item in data if gender_to_filter.lower() == item.get('Jenis Kelamin').lower()]
            if filtered_data:
                print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid'))
                break
            else:
                print('Tidak ada data yang cocok dengan kriteria jenis kelamin tersebut.')

        elif criteria == 'Alamat'.lower():
            city_to_filter = validation_alpha('Masukkan alamat yang ingin di filter: ')
            filtered_data = [item for item in data if item.get('Alamat').lower() == city_to_filter.lower()]
            if filtered_data:
                print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid'))
                break
            else:
                print('Tidak ada data yang cocok dengan kriteria alamat tersebut.')

        elif criteria == 'Divisi'.lower():
            division_to_filter = validation_alpha('Masukkan divisi yang ingin di filter: ')
            filtered_data = [item for item in data if item.get('Divisi').lower() == division_to_filter.lower()]
            if filtered_data:
                print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid'))
                break
            else:
                print('Tidak ada data yang cocok dengan kriteria divisi tersebut.')

        elif criteria == 'Level'.lower():
            level_to_filter = validation_alpha('Masukkan level yang ingin di filter: ')
            filtered_data = [item for item in data if item.get('Level').lower() == level_to_filter.lower()]
            if filtered_data:
                print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid'))
                break
            else:
                print('Tidak ada data yang cocok dengan kriteria level tersebut.')

        elif criteria == 'Jabatan'.lower():
            position_to_filter = validation_alpha('Masukkan jabatan yang ingin di filter: ')
            filtered_data = [item for item in data if item.get('Jabatan').lower() == position_to_filter.lower()]
            if filtered_data:
                print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid'))
                break
            else:
                print('Tidak ada data yang cocok dengan kriteria jabatan tersebut.')

        elif criteria == 'Gaji'.lower():
            salary_to_filter = validation_digit('Masukkan gaji yang ingin di filter: ')
            filtered_data = [item for item in data if item.get('Gaji') == salary_to_filter]
            if filtered_data:
                print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid'))
                break
            else:
                print('Tidak ada data yang cocok dengan kriteria gaji tersebut.')

        else:
            print('Input tidak benar. Silakan coba lagi.')
            print(tabulate(filtered_data,headers='keys',tablefmt='fancy_grid'))