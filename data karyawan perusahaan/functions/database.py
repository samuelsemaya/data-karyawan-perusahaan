import random
import string

def pk(angka: int) -> str:
    letters = string.ascii_uppercase
    numbers = string.digits
    hasil_pk = ''.join(random.choice(letters) for _ in range(2)) + ''.join(random.choice(numbers) for _ in range(4))
    return hasil_pk

data = [
        {'No.':'','NIK':pk(6),'Nama':'John','Umur':25,'Jenis Kelamin':'Pria','Alamat':'Jakarta','Divisi':'IT','Level':'Manager','Jabatan':'Developer','Gaji':200000},
        {'No.':'','NIK':pk(6),'Nama':'Diana','Umur':30,'Jenis Kelamin':'Wanita','Alamat':'Surabaya','Divisi':'HRD','Level':'Staf','Jabatan':'HR Manager','Gaji':100000},
        {'No.':'','NIK':pk(6),'Nama':'Bob','Umur':22,'Jenis Kelamin':'Pria','Alamat':'Bandung','Divisi':'IT','Level':'Manager','Jabatan':'Developer','Gaji':150000},
        {'No.':'','NIK':pk(6),'Nama':'Budi Santoso','Umur':22,'Jenis Kelamin':'Pria','Alamat':'Bandung','Divisi':'IT','Level':'Staf','Jabatan':'Developer','Gaji':150000},
        {'No.':'','NIK':pk(6),'Nama':'Lala','Umur':22,'Jenis Kelamin':'Wanita','Alamat':'Jakarta','Divisi':'Marketing','Level':'Staf','Jabatan':'Digital Marketing','Gaji':100000},
        {'No.':'','NIK':pk(6),'Nama':'Budi Rahmat','Umur':30,'Jenis Kelamin':'Pria','Alamat':'Jakarta','Divisi':'Marketing','Level':'Manager','Jabatan':'Digital Marketing','Gaji':250000}
        ]
        
for index, value in enumerate(data, 1):
    value['No.'] = index
