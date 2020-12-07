# Aula que trata sobre tratamento de strings

frase = 'Curso em Video Python'
print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase1 = '   Aprenda Python  '
print(frase1.strip())
print(frase1.rstrip())
print(frase1.lstrip())
frase2 = frase.split()
print(frase2)
print('-'.join(frase2))
