# 5.4~5.5
salutation = 'hello'
name = 'kim'
product = 'fan'
verbed = 'unfit'
room = 'room'
animals = 'fly'
amount = 'one'
percent = 30
spokesman = 'Park'
job_title = 'CEO'
letter = '''   Dear {} {}
    Thank you for you letter. We are sorry that our {} {} in your
{}. Please note that it should never be used in a {}, especially near any {}.

    Send us your receipt and {} for shipping and handling. We well send you
another {} that, in our tests, is {}% less likely to have {}.

    Thank you for your support.
    Sincerely,
    {}
    {}'''.format(salutation,name,product,verbed,room,room,animals,amount,product,percent,verbed,spokesman,job_title)
print(letter)

#5.6
duck = 'duck'
gourd = 'gourd'
spitz = 'spitz'
you = input('your name')

for i in [duck,gourd,spitz, you]:
    Duck = i.capitalize()
    duck_list = Duck.split()
    duck_list.append('y Mc%sface'% i)
    ducky = ''.join(duck_list)
    print(ducky)

#5.7
duck = 'duck'
gourd = 'gourd'
spitz = 'spitz'
you = input('your name')

for i in [duck,gourd,spitz, you]:
    Duck = i.capitalize()
    duck_list = Duck.split()
    duck_list.append('y Mc{}face'.format(i))
    ducky = ''.join(duck_list)
    print(ducky)

#5.8
duck = 'duck'
gourd = 'gourd'
spitz = 'spitz'
you = input('your name')

for i in [duck,gourd,spitz, you]:
    Duck = i.capitalize()
    duck_list = Duck.split()
    duck_list.append(f'y Mc{i}face')
    ducky = ''.join(duck_list)
    print(ducky)

