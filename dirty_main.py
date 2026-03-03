from datetime import datetime

from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    print(f"Текущая дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    calculate_salary()

    print(f"Текущая дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    get_employees()
