import xml.etree.ElementTree as et
import json
from module5 import News, Advertising, Recipe, Publication
from os import remove
from module6 import PublicationFromFile
from module8 import PublicationFromJSON
from module9 import PublicationFromXML
from module4_3 import normalize_text
from module7 import Analytics

source_file_name = 'LoadNews.xml'
target_file_name = 'Newsfeed.txt'


def main(source, target):
    while True:
        try:
            input_line = input("Please enter:"
                               " 1 for News, "
                               " 2 for Advertisement,"
                               " 3 for Recipe,"
                               " 4 for upload from file,"
                               " 5 for upload from JSON,"
                               " 6 for upload from XML,"
                               " and E for exit: \n")
            if input_line == '1' or input_line == '2' or input_line == '3':
                if input_line == '1':
                    tmp = News()
                elif input_line == '2':
                    tmp = Advertising()
                else:
                    tmp = Recipe()
                tmp.add_publication(input_line, target)
                tmp.write_to_db()
            elif input_line == '4' or input_line == '5' or input_line == '6':
                if input_line == '4':
                    tmp = PublicationFromFile()
                    source = source.replace('xml', 'txt')
                elif input_line == '5':
                    tmp = PublicationFromJSON()
                    source = source.replace('xml', 'json')
                else:
                    tmp = PublicationFromXML()
                tmp.get_source_file(source)
                tmp.get_target_file(target)
                tmp.publish()
                if input('Delete source file Y/N? ').upper() == 'Y':
                    remove(tmp.source_file)

            elif input_line.upper() == 'E':
                break
            elif input_line.upper() not in ('1', '2', '3', '4', '5', '6', 'E'):
                raise ValueError
            Analytics(target)
        except ValueError:
            print('Input is incorrect!\n')
        else:
            break


# Script entry point. It will run only if not imported to another module.
if __name__ == '__main__':
    main(source_file_name, target_file_name)
