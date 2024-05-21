from .clear_screen import clear
from .blink import blink_text

def lanjut_loop():
    while True:
        menu_2 = input('Apakah mau lanjut? (y/n) atau \'u\' ke menu utama: ').lower().strip()
        if menu_2 == 'y':
            clear()
            return menu_2
        elif menu_2 == 'n':
            clear()
            blink_text('Terima kasih telah menggunakan program ini')
            return menu_2
        elif menu_2 == 'u':
            clear()
            return menu_2
        else:
            print('Input yang anda masukkan salah')

def lanjut_loop2():
    while True:
        menu_2 = input('\'u\' ke menu utama atau \'n\' keluar dari program: ').lower().strip()
        if menu_2 == 'n':
            clear()
            blink_text('Terima kasih telah menggunakan program ini')
            return menu_2
        elif menu_2 == 'u':
            clear()
            return menu_2
        else:
            print('Input yang anda masukkan salah')