import re
import sys
from datetime import datetime


class Publication:
    def __init__(self):
        self.publication_text = input(f"Please, enter details about your {self.__class__.__name__}: ")
        self.current_date = datetime.now()

    def write_to_file(self):
        with open('newsfeed.txt', 'a') as file:
            file.write(self.publication_block + '\n\n')
        print('Publication was successfully added to the file')

    def get_publication_header(self):
        return str(self.__class__.__name__) + (30 - len(str(self.__class__.__name__)) - 1) * '-'  + '\n'

    def get_publication_body(self, additional_info):
        return self.publication_text + '\n' + additional_info + '\n'

    def get_publication_footer(self):
        return 30 * '-'

    def get_publication_text(self, additional_info):
        return self.get_publication_header() + self.get_publication_body(additional_info) + self.get_publication_footer()


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city = input("Please enter New's city name: ").capitalize()
        self.current_date = ', ' + datetime.now().strftime('%Y-%m-%d %H:%M')
        self.additional_info = self.city + self.current_date
        self.publication_block = Publication.get_publication_text(self, self.additional_info )


class Advertising(Publication):
    def __init__(self):
        super().__init__()
        self.expiration_date = self.get_expiration_date()
        date_diff = (self.expiration_date - self.current_date).days
        self.additional_info = 'Actual until: ' + str(self.expiration_date.strftime('%Y-%m-%d')) + ',' + str(
            date_diff) + ' days left'
        self.publication_block = Publication.get_publication_text(self, self.additional_info)

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


class Recipe(Publication):
    def __init__(self):
        super().__init__()
        self.calories = self.get_recipe_calories()
        self.calories_rate = self.get_recipe_calories_rate(self.calories)
        self.additional_info = 'Amount of calories: ' + str(self.calories) + ', Calories Rate: ' + str(self.calories_rate)
        self.publication_block = Publication.get_publication_text(self, self.additional_info)

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


def main():
    while True:
        try:
            input_line = input("Please enter 1 for News, 2 for Advertisement, 3 for Weather and E for exit: ")
            if input_line == '1':
                News().write_to_file()
            elif input_line == '2':
                Advertising().write_to_file()
            elif input_line == '3':
                Recipe().write_to_file()
            elif input_line == 'e':
                break
            elif input_line not in ('1','2','3','e'):
                raise ValueError
        except ValueError:
            print('Input is incorrect!')
        else:
            break

main()