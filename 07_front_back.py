"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
import math

def front_back(a, b):
    # +++ SUA SOLUÇÃO +++

    '''
    # Solução programática
    i1 = len(a)/2
    i2 = len(b)/2

    if i1.is_integer():
        a1, a2 = a[:int(i1)], a[int(i1):]
    else:
        a1, a2 = a[:(int(i1)+1)], a[int(i1)+1:]
    if i2.is_integer():
        b1, b2 = b[:int(i2)], b[int(i2):]
    else:
        b1, b2 = b[:(int(i2)+1)], b[int(i2)+1:]
    '''
    
    # Solução otimizada com slice_srt()
    a1, a2 = slice_srt(a)
    b1, b2 = slice_srt(b)

    text = ''.join([a1, b1, a2, b2])

    return text

def slice_srt(x):
    ''''
    # solução sem o math.ceil()
    i = len(x)/2

    if i.is_integer():
        x1, x2 = x[:int(i)], x[int(i):]
    else:
        x1, x2 = x[:(int(i)+1)], x[int(i)+1:]
    '''

    # solução com math.ceil()
    i = math.ceil(len(x)/2)
    x1, x2 = x[:i], x[i:]

    return x1, x2


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
