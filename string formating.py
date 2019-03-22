a: str = "Tasif"
print('my name is %s' % a)
num: float = 3.141596
print("value of pi is %d" % num)  # this will show you only the decimal number before the point.
print('value of pi is %f' % num)  # if you use just %f then it will show all digits after point.
print('value of pi is %.4f' % num)  # it will show you 4 digits after point.
print('value of pi is %.2f' % num)  # it will show you 2 digits after point.
b: str = "Sayed"
c: str = "Salehin"
print('my name is %s %s %s' % (b, c, a))
