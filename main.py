# NOTE: ByteBank is fictional bank used only for examples purposes
# url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar'

# splitting base from the parameters:
qmark_index = url.find('?')
url_base = url[:qmark_index]
url_parameters = url[qmark_index + 1:]
print(url_parameters)

# Searching value from a parameter:
search_parameter = 'moedaDestino'
index_parameter = url_parameters.find(search_parameter)
index_value = index_parameter + len(search_parameter) + 1
ampersand_index = url_parameters.find('&', index_value)
if ampersand_index == -1:
    value = url_parameters[index_value:]
else:
    value = url_parameters[index_value:ampersand_index]
print(value)

