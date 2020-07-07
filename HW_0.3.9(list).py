hours = int(input('Give me some hours: '))
minutes = int(input('Now, give me some minutes: '))
seconds = (hours * (60**2)) + (minutes * 60)
print('You have %d seconds' %(seconds))
