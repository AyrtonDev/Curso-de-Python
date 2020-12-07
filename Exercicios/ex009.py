print('='*20)
print('TABUADA')
print('='*20)

num = int(input('Digite um número: '))
count = 1
while (count < 11):
    print(count, 'x', num , '=',(count*num))
    count = 1 + count    
else:
    print('Tabuada de {} calculada com sucesso!'.format(num))
