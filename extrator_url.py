import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("URL inválida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        return self.url[:indice_interrogacao]

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        return self.url[indice_interrogacao + 1:]

    def get_valor_parametro(self, parametro):
        indice_parametro = self.get_url_parametros().find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return (self.url + "\n" + "Parâmetros: " + self.get_url_parametros()
                                    + "\n" + "URL Base" + self.get_url_base())

    def __eq__(self, other):
        return self.url == other.url


url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
extrator_url_1 = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print("O tamanho da URL é: ", len(extrator_url_1))
print(extrator_url_1)
valor_quantidade = extrator_url_1.get_valor_parametro("quantidade")
print(valor_quantidade)

print(id(extrator_url_1))
print(id(extrator_url_2))
print(extrator_url_1 == extrator_url_2)
