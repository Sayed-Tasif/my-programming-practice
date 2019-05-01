from typing import Set, Union

s = {'alpha', 'orange', 'apple', 'sleep', 'light', 'cloud', 'alpha', 'sleep', 'orange'}
print(s)  # no matter how many time you use the same word, the set will show you only one for the rest of other words.
b = set()  # to create a blank set, you have to use a set() function.
print(b)
print(type(b))
x = {}  # you can't create a blank set in python by just adding 2 curved bracket
print(x)
print(type(x))
# you can not access the items in the set like the list and tuple.
# s = {'alpha', 'orange', 'apple', 'sleep', 'light', 'cloud', 'alpha', 'sleep', 'orange'}
# print(s[0])
# the program you can try to see the result. It will give you a error.

# adding item to a set.
s: Set[Union[str, int]] = {'alpha', 'orange', 'apple', 'sleep', 'light', 'cloud', 'alpha', 'sleep', 'orange'}
s.add('beta')
s.add(1)  # the function _add() let you add one item each time.
print(s)
b.update('selena', 'gomez')  # to add multiple items, you have to use _.update() function.
print(b)  # this will add turn the words into individual character instead of a single word.
b.update({'selena', 'gomez'})  # you have to use the carved bracket to solve that problem.
print(b)

# remove item from the set
s.remove('alpha')  # this function will remove the item from the set. But if the item is not in the set, you will get an
# error
print(s)
s.discard('orange')  # this function will also remove the item you want. But if the item is not in the set, you won't
# get an error
print(s)
s.pop()  # _.pop() function removes the first item of the set.
print(s)
s.clear()  # _.clear() function removes all the item in the set.
print(s)

g = {3, 4, 34, 43, 66, 54}
h = {1, 2, 12, 21, 66, 54}
print(g.union(h))  # you use union function to "union" the sets.
print(h.union(g))

print(g.intersection(h))  # you use intersection function to "intersection" the sets.
print(h.intersection(g))

print(g.difference(h))  # you use difference function to see the difference between 2 sets.
print(h.difference(g))
# you will always get the result for the first set.
