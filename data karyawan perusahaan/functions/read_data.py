from tabulate import tabulate
from .database import *

def read_data():
    print(tabulate(data,headers='keys',tablefmt='fancy_grid'))