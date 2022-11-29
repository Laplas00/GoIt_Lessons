

names = ['nbog', 'sos', 'lol']

for i in range(len(names)):
    print(f'| {i+1} - {names[i]}')

print('\n\n')
for i in range(len(names)):
    print('|{:<5}|{:^8}|'.format(i+1, names[i]))
