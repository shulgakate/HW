from datetime import datetime

try:
    date = input("Please enter Advertising expiration date in format yyyy-mm-dd: ")
    date1 = datetime.strptime(date, '%Y-%m-%d')
    print(date1)
except ValueError:
    print('Value is incorrect')
