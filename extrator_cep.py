endereco = "Rua das flores 72, apartamento 1002, Laranjeiras, RJ, 23440120"

import re #Regular expression

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #Match
if busca:
    cep = busca.group()
    print(cep)