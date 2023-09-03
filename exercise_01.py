# ng is number grade. Manually set in line below
ng = 100


#series of else if statements to determine value of letter grade(lg)
if ng > 90:
    lg = 'A'

elif ng >= 80:
    lg = 'B'
elif ng >= 70:
    lg = 'C'
elif ng >= 60:
    lg = 'D'
elif ng <= 50:
    lg = 'F'


#print final message to terminal. lg is letter grade
print('Your grade is: ' + lg)

