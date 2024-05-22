import random
import string

def pk(angka: int) -> str:
    letters = string.ascii_uppercase
    numbers = string.digits
    hasil_pk = ''.join(random.choice(letters) for _ in range(2)) + ''.join(random.choice(numbers) for _ in range(4))
    return hasil_pk

data = [
    {'No.':'','NIK':pk(6),'Nama': 'John Doe', 'Umur': 25, 'Jenis Kelamin': 'Pria', 'Alamat': 'Jakarta', 'Divisi': 'IT', 'Level': 'Manager', 'Jabatan': 'Developer', 'Gaji': 200000},
    {'No.':'','NIK':pk(6),'Nama': 'Jane Doe', 'Umur': 30, 'Jenis Kelamin': 'Wanita', 'Alamat': 'Surabaya', 'Divisi': 'HRD', 'Level': 'Staf', 'Jabatan': 'HR Manager', 'Gaji': 150000},
    {'No.':'','NIK':pk(6),'Nama': 'Alice Wonderland', 'Umur': 28, 'Jenis Kelamin': 'Wanita', 'Alamat': 'Bandung', 'Divisi': 'IT', 'Level': 'Manager', 'Jabatan': 'Developer', 'Gaji': 180000},
    {'No.':'','NIK':pk(6),'Nama': 'Bob Builder', 'Umur': 35, 'Jenis Kelamin': 'Pria', 'Alamat': 'Jakarta', 'Divisi': 'Marketing', 'Level': 'Staf', 'Jabatan': 'Analyst', 'Gaji': 120000},
    {'No.':'','NIK':pk(6),'Nama': 'Charlie Chaplin', 'Umur': 32, 'Jenis Kelamin': 'Pria', 'Alamat': 'Surabaya', 'Divisi': 'Finance', 'Level': 'Manager', 'Jabatan': 'Accountant', 'Gaji': 220000},
    {'No.':'','NIK':pk(6),'Nama': 'Daisy Duke', 'Umur': 29, 'Jenis Kelamin': 'Wanita', 'Alamat': 'Bandung', 'Divisi': 'HRD', 'Level': 'Staf', 'Jabatan': 'HR Specialist', 'Gaji': 150000},
    {'No.':'','NIK':pk(6),'Nama': 'Edward Scissorhands', 'Umur': 40, 'Jenis Kelamin': 'Pria', 'Alamat': 'Jakarta', 'Divisi': 'IT', 'Level': 'Manager', 'Jabatan': 'SysAdmin', 'Gaji': 250000},
    {'No.':'','NIK':pk(6),'Nama': 'Fiona Fair', 'Umur': 26, 'Jenis Kelamin': 'Wanita', 'Alamat': 'Surabaya', 'Divisi': 'Marketing', 'Level': 'Staf', 'Jabatan': 'Content Writer', 'Gaji': 100000},
    {'No.':'','NIK':pk(6),'Nama': 'George Humble', 'Umur': 31, 'Jenis Kelamin': 'Pria', 'Alamat': 'Bandung', 'Divisi': 'Finance', 'Level': 'Manager', 'Jabatan': 'Controller', 'Gaji': 210000},
    {'No.':'','NIK':pk(6),'Nama': 'Holly Happy', 'Umur': 27, 'Jenis Kelamin': 'Wanita', 'Alamat': 'Jakarta', 'Divisi': 'IT', 'Level': 'Staf', 'Jabatan': 'Developer', 'Gaji': 180000},
    {'No.':'','NIK':pk(6),'Nama': 'Igor Inventor', 'Umur': 36, 'Jenis Kelamin': 'Pria', 'Alamat': 'Surabaya', 'Divisi': 'Marketing', 'Level': 'Manager', 'Jabatan': 'Researcher', 'Gaji': 240000},
    {'No.':'','NIK':pk(6),'Nama': 'Jack Sparrow', 'Umur': 34, 'Jenis Kelamin': 'Pria', 'Alamat': 'Bandung', 'Divisi': 'Marketing', 'Level': 'Staf', 'Jabatan': 'SEO Specialist', 'Gaji': 150000},
    {'No.':'','NIK':pk(6),'Nama': 'Karen Smart', 'Umur': 23, 'Jenis Kelamin': 'Wanita', 'Alamat': 'Jakarta', 'Divisi': 'IT', 'Level': 'Staf', 'Jabatan': 'Developer', 'Gaji': 170000},
    {'No.':'','NIK':pk(6),'Nama': 'Larry Keen', 'Umur': 30, 'Jenis Kelamin': 'Pria', 'Alamat': 'Surabaya', 'Divisi': 'HRD', 'Level': 'Manager', 'Jabatan': 'Recruiter', 'Gaji': 200000},
    {'No.':'','NIK':pk(6),'Nama': 'Mia Mighty', 'Umur': 28, 'Jenis Kelamin': 'Wanita', 'Alamat': 'Bandung', 'Divisi': 'Finance', 'Level': 'Staf', 'Jabatan': 'Accountant', 'Gaji': 140000},
    {'No.':'','NIK':pk(6),'Nama': 'Nathan Hayes', 'Umur': 37, 'Jenis Kelamin': 'Pria', 'Alamat': 'Jakarta', 'Divisi': 'Marketing', 'Level': 'Manager', 'Jabatan': 'Scientist', 'Gaji': 280000},
    {'No.':'','NIK':pk(6),'Nama': 'Olivia Norm', 'Umur': 24, 'Jenis Kelamin': 'Wanita', 'Alamat': 'Surabaya', 'Divisi': 'Marketing', 'Level': 'Staf', 'Jabatan': 'Digital Marketing', 'Gaji': 110000},
    {'No.':'','NIK':pk(6),'Nama': 'Patrick Wise', 'Umur': 33, 'Jenis Kelamin': 'Pria', 'Alamat': 'Bandung', 'Divisi': 'IT', 'Level': 'Manager', 'Jabatan': 'Developer', 'Gaji': 200000},
    {'No.':'','NIK':pk(6),'Nama': 'Queenie Queen', 'Umur': 29, 'Jenis Kelamin': 'Wanita', 'Alamat': 'Jakarta', 'Divisi': 'Finance', 'Level': 'Manager', 'Jabatan': 'Financial Analyst', 'Gaji': 230000},
    {'No.':'','NIK':pk(6),'Nama': 'Roy Robertson', 'Umur': 26, 'Jenis Kelamin': 'Pria', 'Alamat': 'Surabaya', 'Divisi': 'Marketing', 'Level': 'Staf', 'Jabatan': 'Associate', 'Gaji': 130000}
]
        
for index, value in enumerate(data, 1):
    value['No.'] = index
