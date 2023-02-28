num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Inpuvt')
        continue
        
    num = num + 1
    tot = tot + fval

print('ALL DONE!\n')
print(tot, num, tot/num)