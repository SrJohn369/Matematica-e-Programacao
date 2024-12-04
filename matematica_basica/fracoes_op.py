from typing import List
# As intenções com este código é tentar enraizar meus conhecimentos em matemática aplicando as formulas e operações 
# em código programável
# função para verificr se todosos numeros são iguais
def todos_iguais(lista: List[int]):
    return len(set(lista)) == 1


def fatora(list_atual: List[int], divisor_atual: int):
    """
    Fatora uma lista de números inteiros pelo divisor fornecido.

    Parâmetros:
    list_atual : List[int]
        A lista de números inteiros a ser fatorada.
    divisor_atual : int
        O divisor pelo qual os números da lista serão verificados e, se possível, divididos.

    Retorna:
    Tuple[List[float], int, bool]
        Uma tupla contendo:
        - nova_lista: A lista resultante após a fatoração.
        - divisor_atual: O divisor utilizado.
        - bool: Indica se a nova lista é igual à lista original.
    """
    nova_lista = []
    for dividendo in list_atual:
        if dividendo % divisor_atual == 0:
            nova_lista.append(dividendo / divisor_atual)
        else:
            nova_lista.append(dividendo)
    return nova_lista, divisor_atual, nova_lista == list_atual


#função caulculo de mmc
def mmc(*args):
    """
    Calcula o mínimo múltiplo comum (MMC) de um conjunto de números inteiros.
    Parâmetros:
    *args : int
        Um ou mais números inteiros dos quais se deseja calcular o MMC.
    Retorna:
    int
        O mínimo múltiplo comum dos números fornecidos.
    """
    primos = [2,3,5,7,11,13]
    result, div = 1, 1
    aux_list = args[0] if type(args[0]) == list else args
    while not todos_iguais(aux_list): # verifica se todos foram fatorados
        for i, dividendo in enumerate(primos):
            new_list, div_atual, valor = fatora(aux_list, dividendo)
            if not valor: 
                div = div_atual
                aux_list = new_list
                break
        args = aux_list
        result *= div
    
    return result


def comparador(n_f1, n_f2, d_f1, d_f2):
    if n_f1 > n_f2:
        return f"Resultado: {n_f1}/{d_f1} > {n_f2}/{d_f2}"
    else:
        return f"Resultado: {n_f1}/{d_f1} < {n_f2}/{d_f2}"


# funções de calculo de num misto e comparação de fração
def compara_fracao(fracao_1: List[int], fracao_2: List[int]):
    """
    Compara duas frações e determina qual é maior.

    Parâmetros:
    fracao_1 : List[int]
        A primeira fração representada como uma lista onde o primeiro elemento é o numerador e o segundo é o denominador.
    fracao_2 : List[int]
        A segunda fração representada como uma lista onde o primeiro elemento é o numerador e o segundo é o denominador.

    Retorna:
    str
        Uma string indicando a relação entre as duas frações e suas equivalências.
    """
    # denominadores
    denominador_f1 = fracao_1[1]
    denominador_f2 = fracao_2[1]
    # numeradores
    numerador_f1 = fracao_1[0]
    numerador_f2 = fracao_2[0]
    # compara se os denominadores são iguais
    if denominador_f1 == denominador_f2:
        comparador(numerador_f1, numerador_f2, denominador_f1, denominador_f2)
    else:
        calc = mmc(denominador_f1, denominador_f2)
        # tratando da equivalencia da F1
        mult_1 = calc / denominador_f1
        numerador_f1 *= mult_1
        # tratando da equivalencia da F2
        mult_2 = calc / denominador_f2
        numerador_f2 *= mult_2
        # compara e imprime os itens
        if numerador_f1 > numerador_f2:
            return f"""
        Resultado: {fracao_1[0]}/{fracao_1[1]} > {fracao_2[0]}/{fracao_2[1]}
        Equivalência: {int(numerador_f1)}/{calc} > {int(numerador_f2)}/{calc}"""
        else:
            return f"""
        Resultado: {fracao_1[0]}/{fracao_2[1]} < {fracao_2[0]}/{fracao_2[1]}
        Equivalência: {int(numerador_f1)}/{calc} < {int(numerador_f2)}/{calc}"""
        

def calculo_num_misto(num_misto: list):
    """
    Calcula o novo dividendo a partir de um número misto.

    Parâmetros:
    num_misto : list
        Uma lista contendo:
        - num_misto[0]: parte inteira do número misto.
        - num_misto[1]: operador (pode ser "+" ou "-").
        - num_misto[2]: dividendo da fração.
        - num_misto[3]: divisor da fração.

    Retorna:
    tuple
        Uma tupla contendo:
        - novo_dividendo: O novo dividendo calculado.
        - divisor: O divisor original.
    """
    num_inteiro = num_misto[0]
    operador = num_misto[1]
    dividendo = num_misto[2]
    divisor = num_misto[3]
    
    novo_dividendo = divisor * num_inteiro
    if operador == "+":
        novo_dividendo += dividendo
        return novo_dividendo, divisor
    elif operador == "-":
        novo_dividendo -= dividendo
        return novo_dividendo, divisor


def soma_sub_fracoes(*args):
    # faz a separação dos dados denominando cada uma das lista
    numeradores = []
    denominadores = []
    operadores = []
    
    for fracao in args:
        for i, num in enumerate(fracao):
            if i == 0:
                numeradores.append(num)
            elif i == 1: 
                denominadores.append(num)
            elif num == "+" or num == "-":
                operadores.append(num)
    # garante a integridade do algoritimo
    # para evitar erro de "fora do alcance" durante o calculo
    operadores.append("-") if operadores[-1] == "-" else operadores.append("+") 
    # pega o MMC
    denominador_mmc = mmc(denominadores)
    numerador_result = 0
    aux = 1
    # calcula fração por fração
    for i, denominador in enumerate(denominadores):
        aux = (denominador_mmc / denominador) * numeradores[i]
        if operadores[i] == "+":
            numerador_result += aux
        elif operadores[i] == "-":
            numerador_result -= aux
    
    return numerador_result, denominador_mmc


if __name__ == "__main__":
    print("Comparando as frações 5/8 e 7/12")
    print(compara_fracao([5, 8], [7, 12]))
    print("\nCalculo da fração mista 3-4/6 e 4+25/3")
    f_mista_1 = calculo_num_misto([3, "-", 4, 6])
    f_mista_2 = calculo_num_misto([4, "+", 25, 3])
    print(f"Result: 3-4/6 = {f_mista_1[0]}/{f_mista_1[1]}")
    print(f"\nResult: 4+25/3 = {f_mista_2[0]}/{f_mista_2[1]}")
    # soma_f = soma_sub_fracoes([3, 10, "+"],[5, 6])
    # print(f"""
    #       A soma das frações : 3/10+5/6 é {soma_f[0]}/{soma_f[1]} 
    #       """)
    expressao_1 = soma_sub_fracoes([3, 10, "+"], [5, 6, "-"], [3, 13])
    print(f"O resultado da expressão: 3/10 + 5/6 + 3/13 é {expressao_1[0]}/{expressao_1[1]}")
    