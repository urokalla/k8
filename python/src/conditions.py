l = input('enter value of length:')
b = input('enter value of breadth:')
if l == b:
    print('its is square')
else:
    print('rectangle')


x = int(input('enter the number for x= '))

y = int(input('enter the number for y= '))

if x < y:
    print('y is greater than x')
elif x > y: 
        print('x is greater than y')
else:
    print('x and y are equal')
    

q = int(input('enter the quantity:'))
if q*100 > 1000:
    print("cost is", ((q*100)-(0.1*q*100)))
else:
    print("cost is", q*100)
    
    
s = int(input('Enter the salary:'))
yoe = int(input('Enter the no.of years of experience:'))

if yoe > 5:
    print("Salary is increase by 5% which is", (s*0.05))
else:
    print("no bonus")
    
n = []
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        print(n.append(x))

 







    
