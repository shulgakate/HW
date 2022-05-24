import json
from module5 import News, Advertising, Recipe, Publication
from os import remove
from module6 import PublicationFromFile
from module4_3 import normalize_text
from module7 import Analytics

source_file_name = 'LoadNews.json'
target_file_name = 'Newsfeed.txt'


class PublicationFromJSON(PublicationFromFile):
    def __init__(self):
        super().__init__()

    def publish(self):
        publications: dict = {}
        publications = json.load(open(self.source_file, 'r'))
        try:
            for i in publications:
                if i['type'] != '':
                    if normalize_text(i['type']).lower() == 'news':
                        tmp = News(self.target_file)
                        tmp.publication_text = normalize_text(i['text'])
                        tmp.prepare_publication(normalize_text(i['city']))
                    elif normalize_text(i['type']).lower() == 'advertising':
                        tmp = Advertising(self.target_file)
                        tmp.publication_text = normalize_text(i['text'])
                        tmp.prepare_publication(normalize_text(i['expiration_date']))
                    elif normalize_text(i['type']).lower() == 'recipe':
                        tmp = Recipe(self.target_file)
                        tmp.publication_text = normalize_text(i['text'])
                        tmp.prepare_publication(normalize_text(i['calories']))
                    else:
                        self.write_error('Incorrect publication', i['type'])
                        self.unpublished += 1
                        break
                    if tmp.error is not None:
                        self.write_error(tmp.error, i['type'])
                        self.unpublished += 1
                    else:
                        tmp.write_to_file()
                else:
                    self.unpublished += 1
                    self.write_error('Empty publication', i['type'])
            print(str(len(publications) - self.unpublished) + ' of '
                  + str(len(publications)) + ' publications were successfully upload from file')
        except KeyError:
            self.write_error('Incorrect Key value')

def main(source, target):
    while True:
        try:
            input_line = input("Please enter:"
                                   " 1 for News, "
                                   " 2 for Advertisement,"
                                   " 3 for Recipe,"
                                   " 4 for upload from file, "
                                   " 5 for upload from JSON, "
                                   " and E for exit: \n")
            if input_line == '1' or input_line == '2' or input_line == '3':
                Publication().add_publication(input_line, target)
            elif input_line == '4' or input_line == '5':
                if input_line == '4':
                    tmp = PublicationFromFile()
                    source = source.replace('json', 'txt')
                else:
                    tmp = PublicationFromJSON()
                tmp.get_source_file(source)
                tmp.get_target_file(target)
                tmp.publish()
                if input('Delete source file Y/N? ').upper() == 'Y':
                    remove(tmp.source_file)

            elif input_line.upper() == 'E':
                break
            elif input_line.upper() not in ('1', '2', '3', '4', '5', 'E'):
                raise ValueError
            Analytics(target)
        except ValueError:
            print('Input is incorrect!\n')
        else:
            break


# Script entry point. It will run only if not imported to another module.
if __name__ == '__main__':
    main(source_file_name, target_file_name)