
engalphabet = 'abcdefghijklmnopqrstuvwxyzabc'
armalphabet = 'աբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքևօֆաբգ'
rusalphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабв'

text = input("Enter a text: ").lower()
key = int(input("Enter a key (For English 1-25, For Armenian 1-35, For Russian 1-32): "))
encrypted_text = ''

for i in text:
    if i in engalphabet:
        encrypted_text += engalphabet[(engalphabet.index(i) + key)]
    elif i in armalphabet:
        encrypted_text += armalphabet[(armalphabet.index(i) + key)]
    elif i in rusalphabet:
        encrypted_text += rusalphabet[(rusalphabet.index(i) + key)]
    elif i == ' ':
        encrypted_text += ' '  

print(encrypted_text)