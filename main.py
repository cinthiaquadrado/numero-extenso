# Define as listas de palavras para os números de 0 a 19, dezenas, centenas e milhares
unidades = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dezenas = ['', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenas = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
milhares = ['', 'mil']

# Função para converter números em extenso
def converter_numero_extenso(numero):
    if numero < 20:
        return unidades[numero]
    elif numero < 100:
        dezena = dezenas[numero // 10]
        unidade = unidades[numero % 10]
        if unidade == '':
            return dezena
        else:
            return dezena + ' e ' + unidade
    elif numero < 1000:
        centena = centenas[numero // 100]
        dezena = numero % 100
        if dezena == 0:
            return centena
        else:
            return centena + ' e ' + converter_numero_extenso(dezena)
    elif numero < 10000:
        milhar = milhares[numero // 1000]
        centena = numero % 1000
        if centena == 0:
            return milhar + ' ' + milhares[0]
        else:
            return milhar + ' ' + converter_numero_extenso(centena)

# Testando a função
numero = 1978
extenso = converter_numero_extenso(numero)
print(f'{numero} em extenso: {extenso}')
