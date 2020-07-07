win = int(input('Wins: '))
draw = int(input('Draws: '))
losse = int(input('Losses: '))
scores = win * 3 + draw * 1 + losse * 0
print('That team has %d points' %(scores))
