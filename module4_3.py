import random
import string
import re

input_text: string = '''homEwork:

tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''


# Replace iz with is
def replace_text(text, orig = '', rep = ''):
    return text.lower().replace(orig, rep)

def normalize_text(text):
    paragraphs = text.lower().splitlines()
    i: int = 0
    while i < len(paragraphs):
        # remove unnecessary whitespaces
        if len(paragraphs[i]) == 0:
            paragraphs.remove(paragraphs[i])
        else:
            sentences = [j.capitalize() for j in paragraphs[i].strip().split('. ')]
            paragraphs[i] = '. '.join(sentences)
            i += 1
    # join paragraph in text again
    return '\n'.join(paragraphs)

def add_sentence_with_last_words(text):
    last_words = []
    words = text.split()
    for i in range(len(words)):
        if re.findall('[:.]', words[i]):
            last_words.append(re.sub('[:.]', '', words[i]))
    return text + '\n' + ' '.join(last_words) + '.'

def calculate_whitespaces(text):
    return len(text) - len(''.join(text.split()))

input_text = replace_text(input_text, ' iz ', ' is ')
normalize_text = normalize_text(input_text)

print('FINAL NORMALIZED TEXT WITH ADDITIONAL SENTENCE:')
print(add_sentence_with_last_words(normalize_text))

# Calculate Spaces and whitespaces - done
print('\n' + 'NUMBER OF WHITESPACES:')
print(calculate_whitespaces(input_text))