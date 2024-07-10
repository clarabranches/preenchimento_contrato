def converter_centenas(n):
    Unidade = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    Dezena = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    Centena = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
    
    centenas = n // 100
    dezenas = (n % 100) // 10
    unidades = n % 10

    if n == 100:
        return "cem"
    
    result = ""
    
    if centenas > 0:
        result += Centena[centenas]
    
    if dezenas > 1:
        if result:
            result += " e "
        result += Dezena[dezenas]
        if unidades > 0:
            result += " e " + Unidade[unidades]
    elif dezenas == 1:
        if result:
            result += " e "
        result += Unidade[n % 100]
    else:
        if unidades > 0:
            if result:
                result += " e "
            result += Unidade[unidades]

    return result

def num_por_extenso(n):
    Unidade = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    Dezena = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    Centena = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    partes = str(n).split('.')
    parte_inteira = int(partes[0])
    parte_decimal = int(partes[1]) if len(partes) > 1 else 0

    trilhoes = parte_inteira // 1_000_000_000_000
    bilhoes = (parte_inteira // 1_000_000_000) % 1_000
    milhoes = (parte_inteira // 1_000_000) % 1_000
    milhares = (parte_inteira // 1_000) % 1_000
    centenas = parte_inteira % 1_000

    result = ""

    if trilhoes > 0:
        result += converter_centenas(trilhoes) + " trilhão" + ("s" if trilhoes > 1 else "") + " "
    if bilhoes > 0:
        result += converter_centenas(bilhoes) + " bilhão" + ("s" if bilhoes > 1 else "") + " "
    if milhoes > 0:
        result += converter_centenas(milhoes) + " milhão" + ("s" if milhoes > 1 else "") + " "
    if milhares > 0:
        result += converter_centenas(milhares) + " mil "
    if centenas > 0:
        result += converter_centenas(centenas)

    if not result:
        result = "zero"

    if parte_decimal > 0:
        result += " e " + converter_centenas(parte_decimal) + " centavos"

    return result.strip() + " reais"

# Exemplo de uso
n = 1234567890.25
print(num_por_extenso(n))