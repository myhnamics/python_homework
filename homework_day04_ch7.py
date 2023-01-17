# 7.1
years_lists = [1999,2000,2001,2002,2003,2004]

# 7.2
print(years_lists[2])

# 7.3
print(years_lists[-1])

# 7.8
surprise = ['Groucho','Chico','Harpo']

# 7.9
surprise[-1] = surprise[-1].lower()
surprise_list = list(surprise[-1])
surprise_list.reverse()
surprise_list[0] = surprise_list[0].upper()
surprise[-1] = ''.join(surprise_list)
print(surprise)

# 7.10
odd_lists = [number for number in range(10) if number % 2 == 0 and number != 0]
print(odd_lists)

# 7.11
x=2
start1 = ['fee', 'fie', 'foe']
rhymes = [
    ('flop','get a mop'),
    ('fope','turn the rope'),
    ('fa','get your ma'),
    ('fudge','call the judge'),
    ('fat', 'pet the cat'),
    ('fog', 'walk the dog'),
    ('fun',"say we're don")
]
start2 = 'Someone better'

start3 = [i.capitalize() for i in start1]
start3.append(rhymes[x][0].capitalize())
start3 = '! '.join(start3)
print(start3,'\b!')
print(rhymes[x][1].capitalize(),'\b.')