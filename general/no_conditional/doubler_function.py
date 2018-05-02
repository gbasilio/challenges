# from: https://medium.com/@samerbuna/coding-tip-try-to-code-without-if-statements-d06799eed231
#
# Solve the problem without using if-statements (or ternary operators, or switch statements).
#
# Challenge #3: The doubler function (here be dragons)
# Write the doubler function which, based on the type of its input, would do the following:
#
#   When the input is a number, it doubles it (i.e. 5 => 10, -10 => -20).
#   When the input is a string, it repeats every letter (i.e. 'hello' => 'hheelloo').
#   When the input is a function, it calls it twice.
#   When the input is an array, it calls itself on all elements of that array.
#   When the input is an object, it calls itself on all the values of that object.


def doubler_number(n):
  return n+n

def doubler_str(s):
  r = ''
  for char in s:
    r += char + char
  return r

def doubler_function(f):
  f()
  f()

def doubler_list(l):
  l_ret = []
  for e in l:
    l_ret.append(doubler(e))
  return l_ret

def doubler_instance(o):
  for attr in o.__dict__.keys():
    setattr(o, attr, doubler(o.__dict__[attr]))
  return o

operations = {
  'int': doubler_number,
  'float': doubler_number,
  'str': doubler_str,
  'function': doubler_function,
  'list': doubler_list,
  'instance': doubler_instance
}


def doubler(o):
  return operations[type(o).__name__](o)

# test number
print("Testing doubler(10) = " + str(doubler(10)))
print("Testing doubler(119.33) = " + str(doubler(119.33)))

# test string
print("Testing doubler('Gustavo') = " + doubler('Gustavo'))

# test function
print("Testing doubler(function)")
def f():
  print 'This is a function!'

doubler(f)

# test array
print("Testing doubler([1, 2, 3, 4, 5])")
l = [1, 2, 3, 4, 5]
print(doubler(l))

# test object
print("Testing doubler(object)")
class Person:
    name = ""
    age = 0
    gender = ""

p = Person()
p.name = 'Gustavo'
p.age = 40
p.gender = 'M'

print("object.name = " + p.name + " / object.age = " + str(p.age) + " / object.gender = " + p.gender)
doubler(p)
print("object.name = " + p.name + " / object.age = " + str(p.age) + " / object.gender = " + p.gender)
