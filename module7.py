#CSV parsing
import csv
from re import sub, compile
from string import ascii_uppercase
from module6 import PublicationFromFile


class Analytics:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name) as file:
            self.text = file.read()
        self.letters_analytic()
        self.words_count()

    def words_count(self):
        words = self.text.lower().split()
        for i in range(len(words)):
            words[i] = compile('[^a-zA-Z]').sub('', words[i])
        words = list(filter(None, words))
        words_dictionary = dict()
        for j in words:
            if j in words_dictionary:
                words_dictionary[j] += 1
            else:
                words_dictionary[j] = 1

        with open('Word_count.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Word', 'Count'], delimiter='-')
            writer.writeheader()

            for key, value in words_dictionary.items():
                writer.writerow({'Word': key, 'Count': value})

    def letters_analytic(self):
        letter_dictionary = dict()
        upper_letters = []
        letters = compile('[^a-zA-Z]').sub('', self.text)

        for i in letters:
            if i.lower() in letter_dictionary:
                letter_dictionary[i.lower()] += 1
            else:
                letter_dictionary[i.lower()] = 1
            if i in ascii_uppercase:
                upper_letters.append(i.lower())

        with open('Letter count.csv', 'w') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for k, v in letter_dictionary.items():
                percentage = round(int(v) / len(letters) * 100, 2)
                writer.writerow({'letter': k, 'count_all': v,
                                 'count_uppercase': upper_letters.count(k),
                                 'percentage': percentage})


def main(file_name='Newsfeed.txt'):
    PublicationFromFile()
    Analytics(file_name)


if __name__ == '__main__':
    main()
