import pandas as pd
import re

def converter(arquivo):
    """ Converte um arquivo.txt para arquivo.csv com separadores por espaços.
    """
    
    dataframe1 = pd.read_csv(arquivo,                    
                    header=1,                    
                    delim_whitespace=True)
    
    dataframe1 = dataframe1.iloc[0:]

    return dataframe1.to_csv(index = None)
    

def validate(cpf: str) -> bool:

    """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.
    Parâmetros:
        cpf (str): CPF a ser validado
    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.
    Exemplos:
    >>> validate('529.982.247-25')
    True
    >>> validate('52998224725')
    False
    >>> validate('111.111.111-11')
    False
    """

    # Verifica a formatação do CPF
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True


def limpa_dado(dado):
    """ Remove simbolos mantendo apenas os números.

    Args:
        dado = '529.982.247-25'
        limpa_dado(dado): 

    Returns:
        52998224725
    """
    
    return re.sub('[^0-9]', '', dado)
