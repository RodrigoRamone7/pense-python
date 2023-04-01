import math

def print_twice(bruce):
    print(bruce)
    print(bruce)
    
print_twice(42)
print_twice(math.pi)
print_twice('spam '*4)
print_twice(math.cos(math.pi))

michael = 'Eric, the half a bee.'

print_twice(michael)

def cat_twice(part1, part2):
    cat=part1+part2
    print_twice(cat)
    
line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)