import random
import string
import re

inputText: string = '''homEwork:

tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

# Replace iz with is
inputText = inputText.lower().replace(' iz ', ' is ')

# Normalize.
# Split text into paragraphs
paragraphs = inputText.lower().splitlines()

# Each paragraphs split into sentences, capitalize each sentence and then join in paragraph again
i = 0
while i < len(paragraphs):
    # remove unnecessary whitespaces
    if len(paragraphs[i]) == 0:
        paragraphs.remove(paragraphs[i])
    else:
        sentences = [j.capitalize() for j in paragraphs[i].strip().split('. ')]
        paragraphs[i] = '. '.join(sentences)
        i += 1
# join paragraph in text again
normalizeText = '\n'.join(paragraphs)

# Create one more sentence
last_words = []
words = normalizeText.split()
for i in range(len(words)):
    if re.findall('[:.]', words[i]):
        last_words.append(re.sub('[:.]', '', words[i]))
print('FINAL NORMALIZED TEXT WITH ADDITIONAL SENTENCE:')
print(normalizeText + '\n' + ' '.join(last_words) + '.')


# Calculate Spaces and whitespaces - done
print('\n' + 'NUMBER OF WHITESPACES:')
print(len(inputText) - len(''.join(inputText.split())))