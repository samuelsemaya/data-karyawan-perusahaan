import functions

def main_data():
    while True:
        print(40*'=')
        print(f'{'DATA KARYAWAN PERUSAHAAN SS':^40}')
        print(40*'=')
        print('''
1. Baca Data
2. Tambah Data
3. Ubah Data
4. Hapus Data
5. Filter Data
6. Urutkan Data
7. Keluar
''')
        input_menu = functions.validation_digit('Pilih menu (1-7): ')
        if input_menu == 1:
            functions.clear()
            functions.read_data()
            lanjut = functions.lanjut_loop2()
            if lanjut == 'n':
                break

        elif input_menu == 2:
            keluar = False
            while True:
                functions.clear()
                functions.create_data()
                functions.clear()
                functions.read_data()
                lanjut = functions.lanjut_loop()
                if lanjut.lower() == 'n':
                    keluar = True
                    functions.clear()
                    break
                elif lanjut.lower() == 'u':
                    functions.clear()
                    break
            if keluar == True:
                break
            
        elif input_menu == 3:
            keluar = False
            while True:
                functions.clear()
                functions.read_data()
                functions.update_data()
                lanjut = functions.lanjut_loop()
                if lanjut.lower() == 'n':
                    keluar = True
                    break
                elif lanjut.lower() == 'u':
                    break
            if keluar == True:
                break

        elif input_menu == 4:
            keluar = False
            while True:
                functions.clear()
                functions.read_data()
                functions.delete_data()
                functions.read_data()
                lanjut = functions.lanjut_loop()
                if lanjut.lower() == 'n':
                    keluar = True
                    break
                elif lanjut.lower() == 'u':
                    break
            if keluar == True:
                break

        elif input_menu == 5:
            keluar = False
            while True:
                functions.clear()
                functions.read_data()
                functions.filter_data()
                lanjut = functions.lanjut_loop()
                if lanjut.lower() == 'n':
                    keluar = True
                    break
                elif lanjut.lower() == 'u':
                    break
            if keluar == True:
                break

        elif input_menu == 6:
            keluar = False
            while True:
                functions.clear()
                functions.read_data()
                functions.sorted_data()
                lanjut = functions.lanjut_loop()
                if lanjut.lower() == 'n':
                    keluar = True
                    break
                elif lanjut.lower() == 'u':
                    break
            if keluar == True:
                break

        elif input_menu == 7:
            functions.clear()
            functions.blink_text('Terima kasih telah menggunakan program ini')
            quit()
        else:
            functions.clear()
            print(f'\n')
            print(f'{'Input yang dimasukkan salah':^40}')
            print(f'\n\n')

if __name__ == '__main__':
    functions.clear()
    main_data()