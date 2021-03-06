import random

import requests


def __utils__(array):
    size = len(array) - 1
    index = int(random.uniform(0, size))
    if index > size:
        return array[0]
    return array[index]


def __generate__city__():
    resp = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios')
    array = []
    if resp.status_code == 200:
        for json in resp.json():
            name = json['microrregiao']['nome']
            uf = json['microrregiao']['mesorregiao']['UF']['sigla']
            obj = {
                "city": name,
                "uf": uf
            }
            array.append(obj)
    return __utils__(array=array)


def __generate__values__phone__(values, is_len):
    if is_len:
        total = int(random.uniform(1, 20))
        value = ""
        for i in range(0, total):
            value += str(__utils__(array=values))
        return value
    value = ""
    for i in range(0, 11):
        value += str(__utils__(array=values))
    return value


def __generate__chars__():
    chars = ['a', __generate__number__(), 'b', __generate__number__(), 'c', __generate__number__(), 'd',
             __generate__number__(), 'e', __generate__number__(), 'f', __generate__number__(), 'g',
             __generate__number__(),
             'h', __generate__number__(), 'i', __generate__number__()]
    return __utils__(array=chars)


def __generate__number__():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return __utils__(array=numbers)


def __generate__district__():
    return f'Av. {__generate__name__().capitalize()} {__generate__name__last__()}'


def __generate__road__():
    return f'Rua {__generate__name__().capitalize()} {__generate__name__last__()}'


def __generate__name__():
    resp = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes')
    array = []
    if resp.status_code == 200:
        for json in resp.json():
            name = json['nome']
            array.append(name)
        return __utils__(array=array)
    array = [
    "Alice",
    "Miguel",
    "Sophia",
    "Arthur",
    "Helena",
    "Bernardo",
    "Valentina",
    "Heitor",
    "Laura",
    "Davi",
    "Isabella",
    "Lorenzo",
    "Manuela",
    "Th??o",
    "J??lia",
    "Pedro",
    "Helo??sa",
    "Gabriel",
    "Luiza",
    "Enzo",
    "Maria Luiza",
    "Matheus",
    "Lorena",
    "Lucas",
    "L??via",
    "Benjamin",
    "Giovanna",
    "Nicolas",
    "Maria Eduarda",
    "Guilherme",
    "Beatriz",
    "Rafael",
    "Maria Clara",
    "Joaquim",
    "Cec??lia",
    "Samuel",
    "Elo??",
    "Enzo Gabriel",
    "Lara",
    "Jo??o Miguel",
    "Maria J??lia",
    "Henrique",
    "Isadora",
    "Gustavo",
    "Mariana",
    "Murilo",
    "Emanuelly",
    "Pedro Henrique",
    "Ana J??lia",
    "Pietro",
    "Ana Luiza",
    "Lucca",
    "Ana Clara",
    "Felipe",
    "Melissa",
    "Jo??o Pedro",
    "Yasmin",
    "Isaac",
    "Maria Alice",
    "Ben??cio",
    "Isabelly",
    "Daniel",
    "Lav??nia",
    "Anthony",
    "Esther",
    "Leonardo",
    "Sarah",
    "Davi Lucca",
    "Elisa",
    "Bryan",
    "Antonella",
    "Eduardo",
    "Rafaela",
    "Jo??o Lucas",
    "Maria Cec??lia",
    "Victor",
    "Liz",
    "Jo??o",
    "Marina",
    "Cau??",
    "Nicole",
    "Ant??nio",
    "Mait??",
    "Vicente",
    "Isis",
    "Caleb",
    "Al??cia",
    "Gael",
    "Luna",
    "Bento",
    "Rebeca",
    "Caio",
    "Agatha",
    "Emanuel",
    "Let??cia",
    "Vin??cius",
    "Maria-",
    "Jo??o Guilherme",
    "Gabriela",
    "Davi Lucas",
    "Ana Laura",
    "Noah",
    "Catarina",
    "Jo??o Gabriel",
    "Clara",
    "Jo??o Victor",
    "Ana Beatriz",
    "Luiz Miguel",
    "Vit??ria",
    "Francisco",
    "Ol??via",
    "Kaique",
    "Maria Fernanda",
    "Ot??vio",
    "Emilly",
    "Augusto",
    "Maria Valentina",
    "Levi",
    "Milena",
    "Yuri",
    "Maria Helena",
    "Enrico",
    "Bianca",
    "Thiago",
    "Larissa",
    "Ian",
    "Mirella",
    "Victor Hugo",
    "Maria Flor",
    "Thomas",
    "Allana",
    "Henry",
    "Ana Sophia",
    "Luiz Felipe",
    "Clarice",
    "Ryan",
    "Pietra",
    "Arthur Miguel",
    "Maria Vit??ria",
    "Davi Luiz",
    "Maya",
    "Nathan",
    "La??s",
    "Pedro Lucas",
    "Ayla",
    "Davi Miguel",
    "Ana L??via",
    "Raul",
    "Eduarda",
    "Pedro Miguel",
    "Mariah",
    "Luiz Henrique",
    "Stella",
    "Luan",
    "Ana",
    "Erick",
    "Gabrielly",
    "Martin",
    "Sophie",
    "Bruno",
    "Carolina",
    "Rodrigo",
    "Maria Laura",
    "Luiz Gustavo",
    "Maria Helo??sa",
    "Arthur Gabriel",
    "Maria Sophia",
    "Breno",
    "Fernanda",
    "Kau??",
    "Malu",
    "Enzo Miguel",
    "Analu",
    "Fernando",
    "Amanda",
    "Arthur Henrique",
    "Aurora",
    "Luiz Ot??vio",
    "Maria Isis",
    "Carlos Eduardo",
    "Louise",
    "Tom??s",
    "Heloise",
    "Lucas Gabriel",
    "Ana Vit??ria",
    "Andr??",
    "Ana Cec??lia",
    "Jos??",
    "Ana Liz",
    "Yago",
    "Joana",
    "Danilo",
    "Luana",
    "Anthony Gabriel",
    "Ant??nia",
    "Ruan",
    "Isabel",
    "Miguel Henrique",
    "Bruna",
    "Oliver"
]
    return __utils__(array=array)


def __generate__name__last__():
    names_last = [
        "Da silva",
        "Dos santos",
        "Pereira",
        "Alves",
        "Ferreira",
        "De oliveira",
        "Silva",
        "Rodrigues",
        "De souza",
        "Gomes",
        "Santos",
        "Oliveira",
        "Ribeiro",
        "Martins",
        "Soares",
        "Barbosa",
        "Lopes",
        "Vieira",
        "Souza",
        "Fernandes",
        "Lima",
        "Costa",
        "Batista",
        "Dias",
        "Moreira",
        "Nunes",
        "De lima",
        "De sousa",
        "Da costa",
        "De almeida",
        "Mendes",
        "Carvalho",
        "Araujo",
        "Cardoso",
        "Teixeira",
        "Marques",
        "Do nascimento",
        "Almeida",
        "Ramos",
        "Machado",
        "Rocha",
        "Nascimento",
        "De araujo",
        "Bezerra",
        "Sousa",
        "Borges",
        "Santana",
        "De carvalho",
        "Aparecido",
        "Pinto",
        "Pinheiro",
        "Monteiro",
        "Andrade",
        "Leite",
        "Correa",
        "Nogueira",
        "Garcia",
        "De freitas",
        "Henrique",
        "Tavares",
        "Coelho",
        "Pires",
        "De paula",
        "Correia",
        "Miranda",
        "De jesus",
        "Duarte",
        "Freitas",
        "Barros",
        "De andrade",
        "Campos",
        "De melo",
        "Da cruz",
        "Reis",
        "Moraes",
        "Do carmo",
        "Gon??alves",
        "Guimaraes",
        "Dos reis",
        "Viana",
        "De castro",
        "Silveira",
        "Moura",
        "Brito",
        "Neves",
        "Carneiro",
        "Melo",
        "Medeiros",
        "Cordeiro",
        "Farias",
        "Dantas",
        "Cavalcante",
        "Da rocha",
        "De assis",
        "Braga",
        "Cruz",
        "De lourdes",
        "Siqueira",
        "Macedo",
        "Antunes",
        "Castro",
        "Maciel",
        "Cunha",
        "Morais",
        "Fonseca",
        "Menezes",
        "De moraes",
        "Maia",
        "De moura",
        "Barreto",
        "Dacunha",
        "Chaves",
        "Magalhaes",
        "Azevedo",
        "Matos",
        "Torres",
        "Queiroz",
        "Freire",
        "Domingos",
        "Mota",
        "Sales",
        "Cabral",
        "Sampaio",
        "Amaral",
        "Leal",
        "Caetano",
        "Bueno",
        "Guedes",
        "Bispo",
        "Vasconcelos",
        "Amorim",
        "Franco",
        "De santana",
        "De brito",
        "Das gracas",
        "Marinho",
        "Aguiar",
        "Figueiredo",
        "Rosa",
        "Bastos",
        "Franca",
        "Inacio",
        "De barros",
        "Evangelista",
        "Pacheco",
        "Diniz",
        "Camargo",
        "Lemos",
        "Faria",
        "Bento",
        "Dos anjos",
        "Da silveira",
        "Mendonca",
        "De azevedo",
        "S??ntos",
        "Filho",
        "Neto",
        "Dutra",
        "Paiva",
        "De morais",
        "Matias",
        "Muniz",
        "Simoes",
        "Domingues",
        "Santiago",
        "Da rosa",
        "Gonzaga",
        "Feitosa",
        "Coutinho",
        "Ferraz",
        "De abreu",
        "Peixoto",
        "Chagas",
        "Albuquerque",
        "Vaz",
        "Brandao",
        "Trindade",
        "De campos",
        "Rezende",
        "Nonato",
        "Assis",
        "De medeiros",
        "Afonso",
        "Abreu",
        "Teles",
        "De matos",
        "Pessoa",
        "Cavalcanti",
        "Furtado",
        "Pimentel",
        "Lacerda",
        "Braz",
        "Mesquita",
        "Messias",
        "Pontes",
        "Fagundes",
        "Da luz",
        "Cezar",
        "Arruda",
        "Da fonseca",
        "Saraiva",
        "Xavier",
        "Sanches",
        "Prado",
        "De sa",
        "Do amaral",
        "De cassia",
        "Sena",
        "Peres",
        "Passos",
        "Alencar",
        "De faria",
        "Rodrigu??s",
        "Lira",
        "Custodio",
        "Galvao",
        "Porto",
        "De queiroz",
        "Damasceno",
        "Cerqueira",
        "Deaguiar",
        "Firmino",
        "De mello",
        "Das dores",
        "Roque",
        "Pedroso",
        "Barroso",
        "De paiva",
        "Das chagas",
        "Das",
        "Lisboa",
        "Bernardes",
        "Vargas",
        "Lins",
        "Rabelo",
        "Do socorro",
        "Demiranda",
        "Barboza",
        "Paes",
        "Bandeira",
        "De albuquerque",
        "Resende",
        "Gama",
        "Baptista",
        "De farias",
        "Mello",
        "De franca",
        "Ramalho",
        "Vilela",
        "Pimenta",
        "De macedo",
        "Vidal",
        "Rangel",
        "Couto",
        "Amaro",
        "Francisco",
        "De menezes",
        "Veloso",
        "Lemes",
        "Flores",
        "Guerra",
        "Rossi",
        "Padilha",
        "Tomaz",
        "De camargo",
        "Moreno",
        "Esteves",
        "Brasil",
        "Henrique da silva",
        "Do rosario",
        "Muller",
        "Botelho",
        "Tenorio",
        "De arruda",
        "Serafim",
        "Fontes",
        "Do prado",
        "Leao",
        "De amorim",
        "De siqueira",
        "Goulart",
        "Dasneves",
        "Ventura",
        "Ferrari",
        "De vasconcelos",
        "Sobrinho",
        "Aquino",
        "Assuncao",
        "Nobre",
        "Simao",
        "Motta",
        "Bonfim",
        "De aquino",
        "Alcantara",
        "Da penha",
        "Novaes",
        "De deus",
        "Gouveia",
        "Toledo",
        "Holanda"
    ]
    return __utils__(array=names_last)


def __generate__phone__(is_number, is_len):
    if is_number:
        values = []
        for i in range(0, 9):
            values.append(i)
        return __generate__values__phone__(values=values, is_len=is_len)
    values = []
    for i in range(0, 12):
        values.append(__generate__chars__())
    return __generate__values__phone__(values=values, is_len=is_len)


def __generate__email__(value):
    dominios = ['@gmail.com', '@hotmail.com', '@outlook.com.br', '@outlook.com']
    return value.lower() + __utils__(dominios)


def __generate__password__(value, is_valid):
    password = "@" + value.lower()
    if len(password) < 6 and is_valid:
        password += __generate__name__()
    return password


def __generate__(is_valid_password=False):# esse False eh o valor default da funcao
    name = __generate__name__()
    last_name = __generate__name__last__()
    objCity = __generate__city__()
    obj = {
        "first_name": name.capitalize(),  # primeiro nome
        "last_name": last_name,  # segundo nome
        "name_complete": name.capitalize() + " " + last_name,  # nome completo
        "email": __generate__email__(name),  # email
        "password": __generate__password__(value=name, is_valid=is_valid_password),  # senha
        "username": name.lower(),  # username
        "city": objCity['city'],  # cidade
        "uf": objCity['uf'],  # UF
        "phone": __generate__phone__(is_number=True, is_len=False),
        # o is_number for igual a True, ele vai gerar somente n??meros e o is_len for igual a True ele vai gerar uma quantidade maior ou menor que o 11
        # o is_number for igual a False, ele vai gerar n??meros e letras e o is_len for igual a True ele vai gerar uma quantidade maior ou menor que o 11
        # o is_number for igual a True, ele vai gerar somente n??meros e o is_len for igual a False ele vai gerar uma quantidade at?? 11
        # o is_number for igual a False, ele vai gerar n??meros e letras e o is_len for igual a False ele vai gerar uma quantidade at?? 11
        "district": __generate__district__(),  # bairro
        "road": __generate__road__(),  # rua
    }
    return obj
