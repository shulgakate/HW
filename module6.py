from module5 import News, Advertising, Recipe, Publication
from module4_3 import normalize_text
from os import path, stat, remove
from re import findall, sub
from datetime import datetime, date, timedelta
import argparse


class PublicationFromFile:
    def __init__(self, from_file='LoadNews.txt', file_name='Newsfeed.txt'):
        self.from_file = from_file
        self.file_name = file_name
        self.validator = True
        self.err_msg = ''
        self.err_path = 'Errors_' + self.file_name
        self.record = 1
        self.unpublished = 0
        #self.publish(from_file, file_name)

    def write_error(self, error_type, publication):
        with open(self.err_path, 'a') as file:
            file.write(error_type + ': ' + publication + '\n')

    def publish(self, from_file, file_name):
        if self.from_file is None:
            print('File for reading was not specified')
        else:
            with open(self.from_file, 'r') as file:
                 publications = file.read().split('@@')
            #publications = publications
        i = 0
        j = 0
        while i < len(publications):
            if publications[i] != '':
                publication = publications[i].split('||')
                publication_type = normalize_text(publication[0])
                if publication_type == 'News':
                    tmp = News()
                elif publication_type == 'Advertising':
                    tmp = Advertising()
                elif publication_type == 'Recipe':
                    tmp = Recipe()
                else:
                    self.write_error('Incorrect publication', publication_type)
                    break
                body = normalize_text(publication[1])
                additional_info = normalize_text(publication[2])
                tmp.prepare_publication(body, additional_info)
                tmp.write_to_file()
                self.unpublished += 1
            else:
                self.write_error('Empty publication', publications[i])
            i += 1
        print(str(self.unpublished) + ' of ' + str(i) + ' publications were successfully upload from file')


def main(from_file=None, file_name='Newsfeed.txt'):
    while True:
        try:
            input_line = input("Please enter 1 for News, 2 for Advertisement, 3 for Recipe, 4 for upload from file and E for exit: ")
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


