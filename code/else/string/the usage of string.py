# raw string : keep blanks and don't automatically delete  or use the escape character "\" to reach the same output
print(r'\n means new line')
print('\\n means new line')
print(r"print('\\n means newline')")
print("print('\\\\n means newline')")
t = 'hello' 'world'
print(t)
n = 122345678
print('%d is %x hex,%o octal' %(n,n,n))
print('%#08x' %(0x23))  # "#" is means format as 8 - character hex including 0x
print('%+9.2f' % 1234567899999000.45)  # 9 in %9.2f means at least 9 positions total  and it can be more than 9
                                      # the .2f means quarateed 2 positions after decimal point  #the length of the float is beyond the limit of python accuracy limit so it change to /
                                       #the nearly the same float
# print("%.*f" %(5-s,m))  ，m is the float and 5-s is the* because the thing in front of the f can only numbers
# print("%*.*f" %(9,5-s,m)) , that means there are nine digits in front of "." and 5-s digits behind the "." 
# e has a type of float AAAAA.0
#format string
s = 'Hello {}, your ID is {}'
print(s.format('Harry','12345'))


x = 'Hello {0}, your ID is {1}'
print(x.format('Harry','12345'))


v = 'Hello {name:s}, your ID is {ID:08d}'
print(v.format(name = "Herry",ID = 123456))

f = 'Hello {:<20s}, your ID is {:08d}'
print(f.format("Herry", 123456))


y = 'Hello {name:>20s}, your ID is {ID:08d}'
print(y.format(name = "Herry",ID = 123456))



z = 'Hello {name:A^20s}, your ID is {ID:08d}'
print(z.format(name = "Herry",ID = 123456))


# from mult_table import *
# L = range(9,12)
# R = range(8,11)
# print(mult_table(L,R))


name = 'Herry'
id = 12345
print(f'Hello {name:s}, your ID is {id:06d}')

x = 10 
y = 20
print(f'{x}+{y}={x+y}')


L = ['a','b','c']
print(f'L = {L}, len(L) = {len(L)}')



print([f"{i:3d} x {j:3d} = {i*j} " for i in range(5) for j in range(5)])