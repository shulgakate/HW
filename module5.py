import re
import sys
from datetime import datetime
import pyodbc

target_file_name = 'Newsfeed.txt'

server = '127.0.0.1'
database = 'PythonDB'
username = 'sa'
password = 'Waterpolo1'


class Publication:
    def __init__(self, file_name=target_file_name):
        self.current_date = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.target_file = file_name
        self.error = None
        self.publication_text = ''
        self.additional_info = ''
        self.publication_block = ''
        self.db_server = server
        self.db_name = database
        self.db_user = username
        self.db_password = password

    def write_to_file(self):
        with open(self.target_file, 'a') as file:
            file.write(self.publication_block + '\n\n')

    def get_publication_text(self):
        header = str(self.__class__.__name__) + (30 - len(str(self.__class__.__name__)) - 1) * '-' + '\n'
        body = self.publication_text + '\n' + self.additional_info + '\n'
        footer = 30 * '-'
        return header + body + footer

    def add_publication(self, input_line, target_file):
        self.get_additional_info()
        self.get_target_file(target_file)
        self.write_to_file()
        print(f"{self.__class__.__name__} was successfully added to the {self.target_file}")

    def get_target_file(self, file_name):
        try:
            confirmation = input('Is target file ' + file_name + ':'
                                                                 " Y - yes, "
                                                                 " N - for type new file path"
                                                                 " E - for exit\n")
            if confirmation.upper() == 'E':
                exit()
            elif confirmation.upper() == 'N':
                file_name = input('Please enter the path to the new target file: ')
                if file_name == '':
                    print('File name is empty')
                    exit()
            elif confirmation.upper() == 'Y':
                print('')
            else:
                raise ValueError
        except ValueError:
            print('Input is incorrect!')
        try:
            file = open(file_name, 'a')
            self.target_file = file_name
        except FileNotFoundError:
            print('File is not found')
            exit()


class News(Publication):
    def __init__(self, file_name=target_file_name):
        super().__init__(file_name)
        self.city = None

    def get_additional_info(self):
        self.publication_text = input(f"Please, enter details about your {self.__class__.__name__}: ")
        self.city = input("Please enter New's city name: ").capitalize()
        self.prepare_publication()
        if self.error is not None:
            print(self.error)
            exit()

    def prepare_publication(self, param=None):
        try:
            if param is not None:
                self.city = param
            if self.publication_text != '' and self.city != '':
                self.additional_info = self.city + ', ' + self.current_date
                self.publication_block = self.get_publication_text()
            else:
                raise ValueError
        except ValueError:
            self.error = 'Publication text or City could is empty'

    def write_to_db(self):
        with pyodbc.connect('DRIVER={SQL Server Native Client 11.0};'
                            f'SERVER={self.db_server};'
                            f'DATABASE={self.db_name};'
                            f'UID={self.db_user};'
                            f'PWD={self.db_password}') as connection:
            with connection.cursor() as cursor:
                cursor.execute(f'USE {self.db_name};')
                cursor.execute("IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='News' and xtype='U') \
                    CREATE TABLE News("
                               "Text varchar(MAX) NOT NULL, "
                               "City varchar(58) NOT NULL, "
                               "Publication_Date datetime2 NOT NULL)")
                cursor.execute(f"SELECT * FROM News "
                               f"WHERE Text = '{self.publication_text}' "
                               f"  AND City = '{self.city}';")
                query = cursor.fetchall()
                if not query:
                    cursor.execute(f"INSERT INTO News "
                                   f"VALUES('{self.publication_text}', '{self.city}', '{self.current_date}');")
                    print("Record was successfully added into News table!")
                else:
                    print("Record is already existed in News table!")


class Advertising(Publication):
    def __init__(self, file_name=target_file_name):
        super().__init__(file_name)
        self.expiration_date = None
        self.days_until_expired = ''

    def get_additional_info(self):
        self.publication_text = input(f"Please, enter details about your {self.__class__.__name__}: ")
        self.expiration_date = input("Please enter Advertising expiration date in format yyyy-mm-dd: ")
        self.prepare_publication()
        if self.error is not None:
            print(self.error)
            exit()

    def prepare_publication(self, param=None):
        try:
            if param is not None:
                self.expiration_date = param
            if (datetime.strptime(self.expiration_date, '%Y-%m-%d') - datetime.now()).days < 0 \
                    or self.publication_text == '':
                raise ValueError
        except ValueError:
            self.error = 'Publication text is empty or Date format is incorrect or Date is in the past'
        else:
            self.days_until_expired = str(
                (datetime.strptime(self.expiration_date, '%Y-%m-%d') - datetime.now()).days)
            self.additional_info = 'Actual until: ' + self.expiration_date + ', ' \
                                   + self.days_until_expired + ' days left'
            self.publication_block = self.get_publication_text()

    def write_to_db(self):
        with pyodbc.connect('DRIVER={SQL Server Native Client 11.0};'
                            f'SERVER={self.db_server};'
                            f'DATABASE={self.db_name};'
                            f'UID={self.db_user};'
                            f'PWD={self.db_password}') as connection:
            with connection.cursor() as cursor:
                cursor.execute(f'USE {self.db_name};')
                cursor.execute("IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Advertising' and xtype='U') \
                    CREATE TABLE Advertising("
                               "Text varchar(MAX) NOT NULL, "
                               "Expiration_date datetime2 NOT NULL,"
                               "Days_until_expired integer)")
                cursor.execute(f"SELECT * FROM Advertising "
                               f"WHERE Text='{self.publication_text}' "
                               f"  AND Expiration_Date='{self.expiration_date}'"
                               f"  AND Days_until_expired='{self.days_until_expired}'")
                query = cursor.fetchall()
                if not query:
                    cursor.execute(f"INSERT INTO Advertising "
                                   f"VALUES('{self.publication_text}', '{self.expiration_date}',"
                                   f" '{self.days_until_expired}');")
                    print("Record was successfully added into Advertising table!")
                else:
                    print("Record is already existed in Advertising table!")


class Recipe(Publication):
    def __init__(self, file_name=target_file_name):
        super().__init__(file_name)
        self.calories = None
        self.calories_rate = None

    def get_additional_info(self):
        self.publication_text = input(f"Please, enter details about your {self.__class__.__name__}: ")
        self.calories = input('Please enter recipe''s calories as integer number: ')
        self.prepare_publication()
        if self.error is not None:
            print(self.error)
            exit()

    def prepare_publication(self, param=None):
        try:
            if param is not None:
                self.calories = param
            if self.publication_text != '' and int(self.calories) > 0:
                self.get_recipe_calories_rate()
                self.additional_info = 'Amount of calories: ' + self.calories + \
                                       ', Calories Rate: ' + str(self.calories_rate)
                self.publication_block = self.get_publication_text()
            else:
                raise ValueError
        except ValueError:
            self.error = 'Publication text or Calories is empty or Calories isn''t an integer'

    def get_recipe_calories_rate(self):
        if int(self.calories) < 100:
            self.calories_rate = 'Low'
        elif int(self.calories) < 500:
            self.calories_rate = 'Medium'
        else:
            self.calories_rate = 'High'

    def write_to_db(self):
        with pyodbc.connect('DRIVER={SQL Server Native Client 11.0};'
                            f'SERVER={self.db_server};'
                            f'DATABASE={self.db_name};'
                            f'UID={self.db_user};'
                            f'PWD={self.db_password}') as connection:
            with connection.cursor() as cursor:
                cursor.execute(f'USE {self.db_name};')
                cursor.execute("IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Recipe' and xtype='U') \
                                    CREATE TABLE Recipe("
                               "Text varchar(MAX) NOT NULL, "
                               "Calories integer NOT NULL, "
                               "Calories_Rate varchar(10) NOT NULL)")
                cursor.execute(f"SELECT * FROM Recipe "
                               f"WHERE Text='{self.publication_text}' "
                               f"  AND Calories={self.calories}"
                               f"  AND Calories_Rate='{self.calories_rate}'")
                query = cursor.fetchall()
                if not query:
                    cursor.execute(f"INSERT INTO Recipe "
                                   f"VALUES('{self.publication_text}', {self.calories},"
                                   f" '{self.calories_rate}');")
                    print("Record was successfully added into Recipe table!")
                else:
                    print("Record is already existed in Recipe table!")


def main(target):
    while True:
        try:
            input_line = input("Please enter 1 for News, 2 for Advertisement, 3 for Recipe and E for exit: ")
            if input_line == '1' or input_line == '2' or input_line == '3':
                tmp = Publication()
                tmp.add_publication(input_line, target)
            elif input_line.upper() == 'E':
                break
            elif input_line.upper() not in ('1', '2', '3', 'E'):
                raise ValueError
        except ValueError:
            print('Input is incorrect!')
        else:
            break


if __name__ == '__main__':
    main(target_file_name)
