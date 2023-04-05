def topo():
    print('+', ' - '*4, '+', ' - '*4,'+')
    
def corpo():
    print('|', '   '*4, '|','   '*4,'|')
    
def do_twice(f):
    f()
    f()
    
def do_four(f):
    do_twice(f)
    do_twice(f)

def grade():
    topo()
    do_four(corpo)
    topo()
    do_four(corpo)
    topo()
    
grade()