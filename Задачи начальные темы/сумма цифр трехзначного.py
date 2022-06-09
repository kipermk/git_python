# n = str(input('ввести фразу: '))
# l = len(n)
n1 = ''
r1  = 'аоуэеяыюёий'
r11 = '123456789ёй'
r2  = 'чсмтбфвпрлджцкнгшщзх'
r22 = 'вслджфчсаоэтбкыъьур№'
r3 = 'ьъ'
n = 'как 22 же это оказалось 149 не просто!ъъъ))'
l = len(n)
for i in range(l):
           
    if n[i] in r1:
        n1 += r11[r1.find(n[i])]
        
    elif n[i] in r2:
        n1 += r22[r2.find(n[i])]
        
    elif n[i] in r3:
        n1 +='&'
    else:
        n1 += n[i]
        
print(n1)










