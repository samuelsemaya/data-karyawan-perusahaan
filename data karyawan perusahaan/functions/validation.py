def validation_alpha(x):
    while True:
        menu_4 = input(x)
        if menu_4.replace(' ','').isalpha():
            return menu_4
        else:
            print('Input tidak valid !')

def validation_digit(x):
    while True:
        menu = input(x)
        if menu.isdigit():
            return int(menu)
        else:
            print('Masukkan hanya angka !')

def validation_umur(x):
    while True:
        try:
            menu = input(x)
            menu2 = int(menu)
            if menu.isdigit() and menu2 >= 17 and menu2 <=100:
                return int(menu)
            else:
                print('Masukkan umur yang valid !')
        except:
            print('Masukkan hanya angka !')

def validation_kelamin(x):
    while True:
        menu_5 = input(x).lower()
        if menu_5.replace(' ','').isalpha() and menu_5 == 'pria':
            return menu_5
        elif menu_5.replace(' ','').isalpha() and menu_5 == 'wanita':
            return menu_5
        else:
            print('Input hanya pria / wanita !')

def validation_nama(x):
    while True:
        menu_6 = input(x).lower()
        if menu_6.replace(' ','').isalpha() and len(menu_6) >= 4:
            return menu_6
        else:
            print('Input tidak valid ! Silahkan ulangi lagi')

def validation_divisi(x):
    while True:
        menu_7 = input(x).lower()
        if menu_7.replace(' ','').isalpha() and len(menu_7) >= 2:
            return menu_7
        else:
            print('Input tidak valid ! Silahkan ulangi lagi')