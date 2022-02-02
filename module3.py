import random
import string

a: string = '''homEwork:

tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

# Normalize. TODO
print(a.split('\n'))

# Replace iz with is
print(a.lower().replace(' iz ', ' is '))

# Calculate Spaces and whitespaces
print("Number of spaces:", len(a) - len(''.join(a.split())))

# Create one more sentence