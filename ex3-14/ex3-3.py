def plus(): #printa o sinal de mais em linha contínua
    print('+', end=' ')
    
def dash(): #Printa o traço em linha contínua
    print('-', end=' ')
    
def bar(): #Printa o pin em linha contínua
    print('|', end=' ')
    
def space(): #Printa o espaço em linha contínua
    print(' ', end=' ')
    
def nothing(): #Não faz nada
    'nada'
    
def end(): #Fim da linha
    print('')
    
def do_twice(f): #Função para fazer duas vezes a função
    f()
    f()
    
def do_four(f): #Função que faz quatro vezes a função usando a função do_twice
    do_twice(f)
    do_twice(f)
    
def one_four_one(o,f,e): #Faz a função uma vez, quatro e depois mais uma vez
    o()
    do_four(f)
    e()
    
def line(c,m,f): #faz 3 funções e termina a linha
    c()
    m()
    f()
    end()
    
def plus1_dash4(): # '+ - - - -'
    one_four_one(plus,dash,nothing)

def plus1_dash4_plus1(): # '+ - - - - +'
    one_four_one(plus,dash,plus)

def dash4_plus1(): # '- - - - +' 
    one_four_one(nothing,dash,plus)
    
def bar1_space4(): # '|         '
    one_four_one(bar,space,nothing)
    
def bar1_space4_bar1():# '|         |'
    one_four_one(bar,space,bar)
    
def space4_bar1():# '        |'
    one_four_one(nothing,space,bar)

def line1(): # '+ - - - - + - - - - + - - - - + '
    one_four_one(nothing,plus1_dash4,plus)
    end()
    
def line2(): # '|         |         |         | '
    one_four_one(nothing,bar1_space4,bar)
    end()

def grid_one():
    one_four_one(line1,line2,nothing)
    
def grid():
    one_four_one(nothing,grid_one,line1)
    
grid()
    
    
    


    


