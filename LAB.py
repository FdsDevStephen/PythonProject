def square():
    a=int(input('Enter the side of a:'))
    print('The area is:',a*a)
def rect():
    a=int(input('Enter the hieght:'))
    b=int(input('Enter the width:'))
    print('The area is:',a*b)
def circle():
    a=int(input('Enter the hieght:'))
    print('Aarea of circle is',3.14*(a*a))

print('''1.square
      2.rectangle
      3.circle
      ''')

f=int(input())

if f==1:
    square()
elif f==2:
    rect()
elif f==3:
    circle()
else:
    print('No area')

