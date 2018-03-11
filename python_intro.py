print('Hello Django girls!')
if 3 > 2:
    print('funguje to!')
if 5 > 2:
    print('5 je vacsie ako 2')
else:
    print('5 nie je vacsie ako 2')
meno = 'Kika'
if meno == 'Sara':
    print('ahoj Sara')
elif meno == 'Kika':
    print('ahoj Kika')
else:print('cauko neznama')
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
# Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")
def hi():
    print('ahoj')
    print('ako sa mas?')

hi()

def hi(meno):
    if meno == 'Sara':
        print('ahoj Sara')
    elif meno == 'Kika':
        print('ahoj Kika')
    else:
        print('cauko neznama')

hi('Kika')


def hi(meno):
    print('ahoj '+ meno +'!')

dievcata = ['Kika', 'Monika', 'Zuzka', 'Ola', 'Ty']
for meno in dievcata:
    hi(meno)
    print('dalsie dievca')

for i in range(1,6):
    print(i)
