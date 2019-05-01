a = [1234, 'valid', 'ball', 'nice', 'man', 'quick', 123, 'one', 'two', 'alpha', 'alone', 'dark', 'night', 'tiger']
del a[5]  # this will delete the 6th item from the list.
print(a)
a = [1234, 'valid', 'ball', 'nice', 'man', 'quick', 123, 'one', 'two', 'alpha', 'alone', 'dark', 'night', 'tiger']
a.remove(123)  # this will remove item "123"
print(a)
a = [1234, 'valid', 'ball', 'nice', 'man', 'quick', 123, 'one', 'two', 'alpha', 'alone', 'dark', 'night', 'tiger']
del a[-0]  # if you type 0 this will delete the first item of the list. Even if you add minus.
print(a)
del a[-1]  # this will delete the first item from the last of the list.
print(a)
a = [1234, 'valid', 'ball', 'nice', 'man', 'quick', 123, 'one', 'two', 'alpha', 'alone', 'dark', 'night', 'tiger']
a.pop()  # if you don't use the index No. , it will delete the last item of the list.
a.pop(2)  # this will delete the 3rd item from the list.
print(a)
