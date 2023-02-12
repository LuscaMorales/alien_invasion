alien_0 = {'cor':'green','point':5,}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
new_points=alien_0['point']
if new_points > 0:
    print('Great, you just earned {} points'.format(int(new_points)))
else:
    print("You don't have points")
alien_0['cor'] = 'blue'
print('\nNow the alien has a blue color\n')

alien_0['speed'] = 'medium'

print("\nOriginal x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print('\n O novo valor de x-position é ' + str(alien_0['x_position']))

del alien_0['point']





print(alien_0)