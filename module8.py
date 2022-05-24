import json
from module5 import News, Advertising, Recipe, Publication
from os import path, stat, remove
from HW7 import ArticleFromFile, CSVStatistic
from HW5 import News, PrivateAd, Review
from datetime import datetime
import argparse


class PublicationFromJSON(PublicationFromFile):
    def __init__(self, from_file=None, file_name='Newsfeed.txt'):
        self.from_file = from_file
        self.file_name = file_name
        self.validator = True
        self.err_msg = ''
        self.err_path = 'Errors_' + self.file_name
        self.record = 1
        self.unpublished = 0
        super().__init__(from_file, file_name)

    def publish(self):
        if self.from_file is None:
            print('File for reading was not specified')
            exit()
        else:
            with open(self.from_file, 'r') as jsonfile:
                tmp = json.load(jsonfile)

                for i in tmp:
                    try:
                        if i['type'] == 'news':
                            try:
                                if not i['text'] is None and i['text'] != '':
                                    self.text = i['text']
                                else:
                                    self.validator = False
                                    self.err_msg += 'Missing news text.\n'

                                if not i['city'] is None and i['city'] != '':
                                    self.city = i['city']

                                else:
                                    self.validator = False
                                    self.err_msg += 'Missing city.\n'

                                self.time = self.get_time()

                            except KeyError:
                                self.validator = False
                                self.err_msg += 'One of the required news components is missing.\n'

                            if self.validator:
                                if not path.exists(self.file_name):
                                    with open(self.file_name, 'w+') as file:
                                        file.write(
                                            f'News feed:\n\n\n-----News:-----\n{self.text}\n{self.city}, {self.time}')

                                else:
                                    if stat(self.file_name).st_size != 0:
                                        with open(self.file_name, 'a') as file:
                                            file.write(f'\n\n\n-----News:-----\n{self.text}\n{self.city}, {self.time}')

                                    else:
                                        with open(self.file_name, 'w') as file:
                                            file.write(
                                                f'News feed:\n\n\n-----News:-----\n{self.text}\n{self.city}, {self.time}')
                                self.record += 1

                            else:
                                self.unpublished += 1

                                if not path.exists(self.err_path):
                                    with open(self.err_path, 'w+') as file:
                                        file.write(
                                            f'Errors log:\nRecord #{self.record}\nType: News\nIssues: {self.err_msg}')

                                else:
                                    if stat(self.err_path).st_size != 0:
                                        with open(self.err_path, 'a') as file:
                                            file.write(
                                                f'\n\n\nRecord #{self.record}\nType: News\nIssues: {self.err_msg}')

                                    else:
                                        with open(self.err_path, 'w') as file:
                                            file.write(
                                                f'Errors log:\n\n\nRecord #{self.record}\nType: News\nIssues: {self.err_msg}')
                                self.validator = True
                                self.err_msg = ''
                                self.record += 1
                                continue

                        elif i['type'] == 'ad':
                            try:
                                if not i['text'] is None and i['text'] != '':
                                    self.text = i['text']
                                else:
                                    self.validator = False
                                    self.err_msg += 'Missing private ad text.\n'

                                if not i['expiration'] is None and i['expiration'] != '':
                                    self.exp_date = datetime.strptime(i['expiration'], '%d/%m/%Y').date()
                                    self.expire_count = self.get_days_till_expire(custom_date=self.exp_date)

                                else:
                                    self.validator = False
                                    self.err_msg += 'Missing or invalid private ad expiration date.\n'

                            except KeyError:
                                self.validator = False
                                self.err_msg += 'One of the required private ad components is missing.\n'

                            if self.validator:
                                if not path.exists(self.file_name):
                                    with open(self.file_name, 'w+') as file:
                                        file.write(
                                            f'News feed:\n\n\n-----Private ad:-----\n{self.text}\nActual until: {self.exp_date}, {self.expire_count}')

                                else:
                                    if stat(self.file_name).st_size != 0:
                                        with open(self.file_name, 'a') as file:
                                            file.write(
                                                f'\n\n\n-----Private ad:-----\n{self.text}\nActual until: {self.exp_date.strftime("%d/%m/%Y")}, {self.expire_count}')
                                    else:
                                        with open(self.file_name, 'w') as file:
                                            file.write(
                                                f'News feed:\n\n\n-----Private ad:-----\n{self.text}\nActual until: {self.exp_date.strftime("%d/%m/%Y")}, {self.expire_count}')
                                self.record += 1

                            else:
                                self.unpublished += 1

                                if not path.exists(self.err_path):
                                    with open(self.err_path, 'w+') as file:
                                        file.write(
                                            f'Errors log:\nRecord #{self.record}\nType: Private Ad\nIssues: {self.err_msg}')

                                else:
                                    if stat(self.err_path).st_size != 0:
                                        with open(self.err_path, 'a') as file:
                                            file.write(
                                                f'\n\n\nRecord #{self.record}\nType: Private Ad\nIssues: {self.err_msg}')

                                    else:
                                        with open(self.err_path, 'w') as file:
                                            file.write(
                                                f'Errors log:\n\n\nRecord #{self.record}\nType: Private Ad\nIssues: {self.err_msg}')
                                self.validator = True
                                self.err_msg = ''
                                self.record += 1
                                continue

                        elif i['type'] == 'review':
                            try:
                                if not i['title'] is None and i['title'] != '':
                                    self.title = i['title']

                                else:
                                    self.validator = False
                                    self.err_msg += 'Missing review title.\n'

                                if not i['text'] is None and i['text'] != '':
                                    self.text = i['text']

                                else:
                                    self.validator = False
                                    self.err_msg += 'Missing review text.\n'

                                if not i['rate'] is None and i['rate'] != '':
                                    if 1 <= int(i['rate']) <= 10:
                                        self.rate = i['rate']

                                    else:
                                        self.validator = False
                                        self.err_msg += 'Review rate out of range.\n'

                                else:
                                    self.validator = False
                                    self.err_msg += 'Missing review rate.\n'

                                if not i['author'] is None and i['author'] != '':
                                    self.author = i['author']

                                else:
                                    self.validator = False
                                    self.err_msg += 'Missing review author.\n'

                                self.time = self.get_time()

                            except KeyError:
                                self.validator = False
                                self.err_msg += 'One of the required review components is missing.\n'

                            if self.validator:
                                if not path.exists(self.file_name):
                                    with open(self.file_name, 'w+') as file:
                                        file.write(
                                            f'News feed:\n\n\n-----Review:-----\n{self.title}\n{self.text}\nFinal score: {self.rate}/10,\n{self.author}, {self.time}')

                                else:
                                    if stat(self.file_name).st_size != 0:
                                        with open(self.file_name, 'a') as file:
                                            file.write(
                                                f'\n\n\n-----Review:-----\n{self.title}\n{self.text}\nFinal score: {self.rate}/10,\n{self.author}, {self.time}')
                                    else:
                                        with open(self.file_name, 'w') as file:
                                            file.write(
                                                f'News feed:\n\n\n-----Review:-----\n{self.title}\n{self.text}\nFinal score: {self.rate}/10,\n{self.author}, {self.time}')
                                self.record += 1

                            else:
                                self.unpublished += 1

                                if not path.exists(self.err_path):
                                    with open(self.err_path, 'w+') as file:
                                        file.write(
                                            f'Errors log:\nRecord #{self.record}\nType: Review\nIssues: {self.err_msg}')

                                else:
                                    if stat(self.err_path).st_size != 0:
                                        with open(self.err_path, 'a') as file:
                                            file.write(
                                                f'\n\n\nRecord #{self.record}\nType: Review\nIssues: {self.err_msg}')

                                    else:
                                        with open(self.err_path, 'w') as file:
                                            file.write(
                                                f'Errors log:\n\n\nRecord #{self.record}\nType: Review\nIssues: {self.err_msg}')
                                self.validator = True
                                self.err_msg = ''
                                self.record += 1
                                continue

                        else:
                            self.unpublished += 1
                            self.err_msg += 'Unknown article type.\n'

                            if not path.exists(self.err_path):
                                with open(self.err_path, 'w+') as file:
                                    file.write(
                                        f'Errors log:\nRecord #{self.record}\nType: Unknown\nIssues: {self.err_msg}')

                            else:
                                if stat(self.err_path).st_size != 0:
                                    with open(self.err_path, 'a') as file:
                                        file.write(
                                            f'\n\n\nRecord #{self.record}\nType: Unknown\nIssues: {self.err_msg}')

                                else:
                                    with open(self.err_path, 'w') as file:
                                        file.write(
                                            f'Errors log:\n\n\nRecord #{self.record}\nType: Unknown\nIssues: {self.err_msg}')
                            self.validator = True
                            self.err_msg = ''
                            self.record += 1
                            continue

                    except KeyError:
                        self.unpublished += 1
                        self.err_msg += 'Unknown article type.\n'

                        if not path.exists(self.err_path):
                            with open(self.err_path, 'w+') as file:
                                file.write(f'Errors log:\nRecord #{self.record}\nType: Unknown\nIssues: {self.err_msg}')

                        else:
                            if stat(self.err_path).st_size != 0:
                                with open(self.err_path, 'a') as file:
                                    file.write(f'\n\n\nRecord #{self.record}\nType: Unknown\nIssues: {self.err_msg}')

                            else:
                                with open(self.err_path, 'w') as file:
                                    file.write(
                                        f'Errors log:\n\n\nRecord #{self.record}\nType: Unknown\nIssues: {self.err_msg}')
                        self.validator = True
                        self.err_msg = ''
                        self.record += 1
                        continue

                if self.unpublished == 0:
                    print('Success.')
                    remove(self.from_file)

                else:
                    print(self.unpublished,
                          f'publications skipped due to errors in the source file. See all of the issues in the {self.err_path} file')


def main(from_file=None, file_name='Newsfeed.txt'):
    while True:
        try:
            input_line = input(
                "Please enter:"
                "   1 for News, "
                "   2 for Advertisement, "
                "   3 for Recipe, "
                "   4 for upload from file "
                "   5 for upload from JSON "
                "   E for exit: ")
            if input_line == '1' or input_line == '2' or input_line == '3':
                Publication().add_publication(input_line)
            elif input_line == '4':
                    if from_file is None:
                        print('File not found. Use -s or --source argument to specify path')
                        exit()
                    else:
                        print('------------Uploading------------')
                        PublicationFromFile().publish(from_file, file_name)
                elif input_line == 'e':
                    break
                elif input_line not in ('1', '2', '3', '4', 'e'):
                    raise ValueError
            except ValueError:
                print('Input is incorrect!')
            else:
                break

    main('LoadNews.txt')

    try:
        article = input("""Please choose the type of article you want to add and press Enter button:
        1 - News
        2 - Private ad
        3 - Review
        4 - Upload from the file
        5 - Upload from JSON\n""")

        if article == '1':
            print('------------Adding news------------')
            News(file_name)
            CSVStatistic(file_name)

        elif article == '2':
            print('------------Adding private ad------------')
            PrivateAd(file_name)
            CSVStatistic(file_name)

        elif article == '3':
            print('------------Adding review------------')
            Review(file_name)
            CSVStatistic(file_name)

        elif article == '4':
            if from_file is None:
                print('File for reading was not specified. Use -s or --source argument to specify path')
                exit()
            else:
                print('------------Uploading------------')
                ArticleFromFile(from_file, file_name)
                CSVStatistic(file_name)

        elif article == '5':
            if from_file is None:
                print('File for reading was not specified. Use -s or --source argument to specify path')
                exit()
            else:
                print('------------Uploading------------')
                ArticleFromJSON(from_file, file_name)
                CSVStatistic(file_name)

        else:
            print('Incorrect article type\n')
            main(file_name)

        # KeyboardInterrupt error handling
    except KeyboardInterrupt:
        print('\nTerminated.')
        exit()

    # Additional article confirmation
    if article == '4' or article == '5':
        try:
            confirm = input(
                'Do you want to upload another file? (Input y to confirm, input any other button to exit)\n')

            if confirm.lower().strip() == 'y':
                try:
                    from_file = input('Please enter the path to the new source file: ')

                    if from_file == '':
                        from_file = None

                except KeyboardInterrupt:
                    print('\nTerminated')
                    exit()

                main(from_file, file_name)

            else:
                exit()

        # KeyboardInterrupt error handling
        except KeyboardInterrupt:
            print('\nTerminated.')
            exit()

    else:
        try:
            confirm = input(
                'Do you want to add another article? (Input y to add another article, input any other button to exit)\n')

            if confirm.lower().strip() == 'y':
                main(file_name)

            else:
                exit()

        # KeyboardInterrupt error handling
        except KeyboardInterrupt:
            print('\nTerminated.')
            exit()


# Script entry point. It will run only if not imported to another module.
if __name__ == '__main__':
    main(from_file)