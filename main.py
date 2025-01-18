import transliterate
from transliterate import translit
from num2words import num2words

print(translit("""Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of f
ame once in a lifetime and I guess that this is mine. People have also t
old me to make these next few minutes escruciatingly embarrassing and to
take vengeance of my enemies. Neither will happen.

More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic
Storage for last 40. When I was 8...""", 'ru'),'\n')


num_1 = (num2words(78, lang='ru'))
num_2 = (num2words(15, lang='ru'))
num_3 = (num2words(3, lang='ru'))
num_4 = (num2words(40, lang='ru'))
num_5 = (num2words(8, lang='ru'))

print("78 -", num_1)
print("15 -", num_2)
print("3 -", num_3)
print("40 -", num_4)
print("8 -", num_5)
