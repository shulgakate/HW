import random
import string
print([{random.choice(string.ascii_lowercase): random.randint(1,100) for y in range(random.randint(3,10))} for x in range(random.randint(2,10))])
