from .database import *
from .validation import validation_digit,validation_umur,validation_kelamin,validation_nama,validation_divisi

def create_data():
    while True:
        nama = validation_nama('Masukkan nama: ')
        name_exists = False

        for entry in data:
            if entry['Nama'].lower() == nama.lower():
                name_exists = True
                print('Nama sudah ada di database !')

        if name_exists == True:
            continue
        else:
            break
    umur = validation_umur('Masukkan umur: ')
    jenis_kelamin = validation_kelamin('Masukkan jenis kelamin (pria/wanita): ')
    alamat = validation_nama('Masukkan alamat: ')
    divisi = validation_divisi('Masukkan divisi: ')
    level = validation_nama('Masukkan level: ')
    jabatan = validation_nama('Masukkan jabatan: ')
    gaji = validation_digit('Masukkan gaji: ')

    if divisi.lower() == 'it' or divisi.lower() == 'hrd':
        divisi = divisi.upper()
    else:
        divisi = divisi.capitalize()

    data.append({'No.':'','NIK':pk(6),'Nama':nama.title(),'Umur':umur,'Jenis Kelamin':jenis_kelamin.capitalize(),'Alamat':alamat.title(),'Divisi':divisi,'Level':level.title(),'Jabatan':jabatan.title(),'Gaji':gaji})
    
    for index, value in enumerate(data,1):
        value['No.'] = index