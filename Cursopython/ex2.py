a = input('Digite algo:')
print('O tipo primitivo desse valor é',type(a))
print('Só tem espaços?',a.isspace())
print('Tem número?',a.isnumeric())
print('Tem letras?',a.isalpha())
print('Ele é alfanumerico?',a.isalnum())