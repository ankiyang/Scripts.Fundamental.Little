"""
Build Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ',
  ' *** ',
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]
test.assert_equals(tower_builder(1), ['*', ])
test.assert_equals(tower_builder(2), [' * ', '***'])
test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])
"""

def tower_builder(n_floors):
    space = ' '
    star = '*'
    result = []
    space_num_side = n_floors - 1
    for i in range(n_floors):
        start_num = (i + 1) * 2 - 1
        line = space * space_num_side + star * start_num + space * space_num_side
        print line
        space_num_side -= 1
        result.append(line)
    return result

def tower_builder2(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


print tower_builder(6)