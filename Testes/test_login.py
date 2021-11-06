import random
import unittest
import webbrowser

import allure
import time

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Utils:

    def __utils__(self, array):
        size = len(array) - 1
        return array[int(random.uniform(0, size))]

    def generate(self):
        def __generate__city():
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
            return self.__utils__(array=array)

        def __generate__district():
            return f'Av. {__generate__name().capitalize()} {__generate__name__last()}'

        def __generate__road():
            return f'Rua {__generate__name().capitalize()} {__generate__name__last()}'

        def __generate__name():
            resp = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes')
            array = []
            if resp.status_code == 200:
                for json in resp.json():
                    name = json['nome']
                    array.append(name)
            return self.__utils__(array=array)

        def __generate__name__last():
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
                "Gonçalves",
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
                "Sántos",
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
                "Rodriguês",
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
            return self.__utils__(array=names_last)

        def __generate__email(value):
            dominios = ['@gmail.com', '@hotmail.com', '@outlook.com.br', '@outlook.com']
            return value.lower() + self.__utils__(dominios)

        name = __generate__name()
        last_name = __generate__name__last()
        objCity = __generate__city()
        obj = {
            "first_name": name.capitalize(),  # primeiro nome
            "last_name": last_name,  # segundo nome
            "name_complete": name.capitalize() + " " + last_name,  # nome completo
            "email": __generate__email(name),  # email
            "password": "@" + name.lower(),  # senha
            "username": name.lower(),  # username
            "city": objCity['city'],  # cidade
            "uf": objCity['uf'],  # UF
            "district": __generate__district(),  # bairro
            "road": __generate__road(),  # rua
        }
        return obj


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @allure.testcase("Testando o login valido")
    def test_login_valido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("test")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)  # ele vai pausar por 2 segundos
        driver.forward()
        result = ""
        try:
            result = driver.find_element_by_class_name('alert-success').text
            print("RESULT -> ", result)
        except NoSuchElementException:
            print('Error')

        assert "Login Efetuado Sucesso!" in result

    @allure.testcase("Testando o login invalido")
    def test_login_invalido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)  # ele vai pausar por 2 segundos
        #driver.forward()
        result2 = ""
        # result = driver.get("http://127.0.0.1:8000/listarProfissional")
        try:
            result2 = driver.find_element_by_class_name('alert-danger').text
            print("RESULT -> ", result2)
        except NoSuchElementException:
            print('Error')

        assert "Usuário ou senha inválido." in result2