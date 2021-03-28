alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

print_value = alien_0.get('points', 'No point value assigned.')
print(print_value)

print_value = alien_0.get('points')
print(print_value)

print(alien_0)
