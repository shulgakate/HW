from module5 import News, Advertising, Recipe, Publication
from module4_3 import normalize_text
from os import path, stat, remove
from re import findall, sub
from datetime import datetime, date, timedelta

source_file_name = 'LoadNews.txt'
target_file_name = 'Newsfeed.txt'


class PublicationFromFile(Publication):
    def __init__(self):
        super().__init__()
        self.validator = True
        self.err_msg = ''
        self.err_path = 'Errors_log.txt'
        self.record = 1
        self.unpublished = 0

    def write_error(self, error_type, publication):
        with open(self.err_path, 'a') as file:
            file.write(error_type + ': ' + publication + '\n')

    def publish(self):
        with open(self.source_file, 'r') as file:
            publications = file.read().split('@@')
        i = 0
        j = 0
        while i < len(publications):
            if publications[i] != '':
                publication = publications[i].split('||')
                publication_type = normalize_text(publication[0])
                if publication_type == 'News':
                    tmp = News(self.target_file)
                elif publication_type == 'Advertising':
                    tmp = Advertising(self.target_file)
                elif publication_type == 'Recipe':
                    tmp = Recipe(self.target_file)
                else:
                    self.write_error('Incorrect publication', publication_type)
                    self.unpublished += 1
                    break
                tmp.publication_text = normalize_text(publication[1])
                tmp.prepare_publication(normalize_text(publication[2]))
                if tmp.error is not None:
                    self.write_error(tmp.error, publications[i])
                    self.unpublished += 1
                else:
                    tmp.write_to_file()
            else:
                self.unpublished += 1
                self.write_error('Empty publication', publications[i])
            i += 1
        print(str(len(publications) - self.unpublished) + ' of '
              + str(len(publications)) + ' publications were successfully upload from file')

    def get_source_file(self, file_name):
        try:
            confirmation = input('Is source file for upload ' + file_name + ':'
                                 " Y - yes, "
                                 " N - for type new file path"
                                 " E - for exit: \n")
            if confirmation.upper() == 'E':
                exit()
            elif confirmation.upper() == 'N':
                file_name = input('Please enter the path to the new source file: ')
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
            file = open(file_name, 'r')
            self.source_file = file_name
        except FileNotFoundError:
            print('File is not found')
            exit()


def main(source, target):
    while True:
        try:
            input_line = input("Please enter:"
                               " 1 for News, "
                               " 2 for Advertisement,"
                               " 3 for Recipe,"
                               " 4 for upload from file"
                               " and E for exit: \n")
            if input_line == '1' or input_line == '2' or input_line == '3':
                Publication().add_publication(input_line, target)
            elif input_line == '4':
                tmp = PublicationFromFile()
                tmp.get_source_file(source)
                tmp.get_target_file(target)
                tmp.publish()
                if input('Delete source file Y/N? ').upper() == 'Y':
                    remove(tmp.source_file)
            elif input_line.upper() == 'E':
                break
            elif input_line.upper() not in ('1', '2', '3', '4', 'E'):
                raise ValueError
        except ValueError:
            print('Input is incorrect!\n')
        else:
            break

if __name__ == '__main__':
    main(source_file_name, target_file_name)


