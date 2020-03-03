

def fun1 ():
    a = input('Enter a noun: ')
    b = input('Enter a noun(plural): ')
    c = input('Enter a noun: ')
    d = input('Enter a place: ')
    e = input('Enter an adjective: ')
    f = input('Enter a noun: ')

    print('Be kind to your', a, '-footed ', b, '\nFor a duck may be somebody\'s ', c,
          ',\nBe kind to your ', b, ' in ', d, '\nWhere the weather is always ', e,
          '\n\nYou may think that is the ', f, '\nWell it is.')


def fun2():
    a = input('Enter a relative: ')
    b = input('Enter a adjective: ')
    c = input('Enter a adjective: ')
    d = input('Enter a adjective: ')
    e = input('Enter a name of person in room: ')
    f = input('Enter a adjective: ')
    g = input('Enter a adjective: ')
    h = input('Enter a verb ending in "ED": ')
    i = input('Enter a body part: ')
    j = input('Enter a verb ending in "ING": ')
    k = input('Enter a noun(plural): ')
    l = input('Enter a noun: ')
    m = input('Enter a adverb: ')
    n = input('Enter a verb: ')
    o = input('Enter a verb: ')
    p = input('Enter a relative: ')
    q = input('Enter a noun: ')

    print('Dear', a, '\nI am having a(n)', b, 'time at camp. The counselour is',
          c, '\nand the food is', d,'. I met', e, 'and we became', f,' friends. Unfortunately,',
          e, '\nis', g, 'and', i, h, 'my I so we couldn`t go', j, 'like everybody else. I need more',
          k, '\nand a', l, 'sharpener, so please', m , n, 'more when you', o, 'back. \nYour', p,'\n',q)


def which_run(a):
    b = int(a) % 2

    if b == 0:
        fun1()
    else:
        fun2()


a = input('Please input a number: ')
which_run(a)