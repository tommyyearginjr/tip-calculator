print('  TIP CALCULATOR'+'\n  '+((len('TIP CALCULATOR'))*'-'))

i = input('How much is your bill? ')
i = float(i)
t = '{:.2f}'.format(round((i*.15),2))
print('\nYour tip amount is ${}.'.format(t))
t = float(t)
print('\nYour total bill, including tip, is ${:.2f}.'.format(i+t))
