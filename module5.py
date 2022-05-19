import re
import sys
from datetime import datetime


class Publication:
    def __init__(self, file_name='Newsfeed.txt'):
        self.current_date = datetime.now()
        self.file_name = file_name

    def write_to_file(self):
        with open(self.file_name, 'a') as file:
            file.write(self.publication_block + '\n\n')


    def get_publication_text(self, text, additional_info):
        header = str(self.__class__.__name__) + (30 - len(str(self.__class__.__name__)) - 1) * '-'  + '\n'
        body = text + '\n' + additional_info + '\n'
        footer = 30 * '-'
        return header + body + footer


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city = None
        self.publication_text = None
        self.publication_block = None
        self.additional_info = None

    def get_additional_info(self):
        self.publication_text = input(f"Please, enter details about your {self.__class__.__name__}: ")
        self.city = input("Please enter New's city name: ").capitalize()
        self.prepare_publication(self.publication_text, self.city)

    def prepare_publication(self, body, city):
        self.additional_info = city + ', ' + datetime.now().strftime('%Y-%m-%d %H:%M')
        self.publication_block = super().get_publication_text(body, self.additional_info)


class Advertising(Publication):
    def __init__(self):
        super().__init__()
        self.publication_block = None
        self.additional_info = None
        self.publication_text = None
        self.expiration_date = None

    def get_expiration_date(self):
        while True:
            try:
                date = input("Please enter Advertising expiration date in format yyyy-mm-dd: ")
                date = datetime.strptime(date, '%Y-%m-%d')
                if (date - self.current_date).days < 0:
                    raise ValueError
            except ValueError:
                print('Date format is incorrect or Date is in past. Please try again')
            else:
                return date
            
    def get_additional_info(self):
        self.publication_text = input(f"Please, enter details about your {self.__class__.__name__}: ")
        self.expiration_date = self.get_expiration_date()
        self.prepare_publication(self.publication_text, self.expiration_date)
        
    def prepare_publication(self, body, expiration_date):
        expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d')
        date_diff = (expiration_date - self.current_date).days
        self.additional_info = 'Actual until: ' + str(expiration_date.strftime('%Y-%m-%d')) + ', ' + str(
            date_diff) + ' days left'
        self.publication_block = super().get_publication_text(body, self.additional_info)


class Recipe(Publication):
    def __init__(self):
        super().__init__()
        self.publication_text = None
        self.calories = None
        self.calories_rate = None
        self.additional_info = None
        self.publication_block = None

    def get_additional_info(self):
        self.publication_text = input(f"Please, enter details about your {self.__class__.__name__}: ")
        self.calories = self.get_recipe_calories()
        self.prepare_publication(self.publication_text, self.calories)

    def prepare_publication(self, body, calories):
        self.calories_rate = self.get_recipe_calories_rate(int(calories))
        self.additional_info = 'Amount of calories: ' + str(calories) + ', Calories Rate: ' + str(self.calories_rate)
        self.publication_block = super().get_publication_text(body, self.additional_info)

    def get_recipe_calories(self):
        while True:
            try:
                calories = int(input('Please enter recipe''s calories as integer number: '))
            except ValueError:
                print('Format is incorrect. Please try again')
            else:
                return calories

    def get_recipe_calories_rate(self, calories):
        if calories < 100:
            return 'Low'
        elif calories < 500:
            return 'Medium'
        else:
            return 'High'


def main(file_name='Newsfeed.txt'):
    while True:
        try:
            input_line = input("Please enter 1 for News, 2 for Advertisement, 3 for Recipe and E for exit: ")
            if input_line == '1' or input_line == '2' or input_line == '3':
                if input_line == '1':
                    tmp = News()
                elif input_line == '2':
                    tmp = Advertising()
                elif input_line == '3':
                    tmp = Recipe()
                tmp.get_additional_info()
                tmp.write_to_file()
                print(f"{tmp.__class__.__name__} was successfully added to the file")
            elif input_line == 'e':
                break
            elif input_line not in ('1','2','3','e'):
                raise ValueError
        except ValueError:
            print('Input is incorrect!')
        else:
            break

if __name__ == '__main__':
    main()