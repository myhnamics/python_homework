#6.2
guess_me = 7
number = 1
while 1:
    if number < guess_me:
        print('too low')
    elif guess_me>number:
        print('oops')
        break
    else:
        print('found it')
        break
    number += 1

#6.3
guess_me = 5
for i in range(10):
    if i < guess_me:
        print('too low')
    elif guess_me > i:
        print('oops')
        break
    else:
        print('found it')
        break
    number += 1