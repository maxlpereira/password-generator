import string
import random

numb = list(range(0,10))
for i in numb:
    numb[i] = str(i)

alpha_l = list(string.ascii_lowercase)
alpha_h = list(string.ascii_uppercase)
library = alpha_l+alpha_h+numb
gen = ''
count = 0

for p in range(16):
    count += 1
    gen += random.choice(library)
    if p == 15:
        continue  
    elif count == 4:
        gen += '-'
        count = 0

print(gen)
