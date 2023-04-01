line1 = 'Bing tiddle '
line2 = 'tiddle bang.'

def cat_twice(part1, part2):
    cat=part1+part2
    print_twice(cat)
    
def print_twice(bruce):
    print(bruce)
    print(bruce)
    
cat_twice(line1, line2)