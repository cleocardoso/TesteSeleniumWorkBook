@allure.testcase("Testando o Campo usuario caracteres maior que 150")
def test_cadastro_campo_usuario_Caracteres_maior_150(self):
    driver = self.driver
    driver.get("http://127.0.0.1:8000/cadastro/")
    self.assertIn("WorkBook", driver.title)
    obj = Utils().generate()
    nome = obj['username']
    email = obj['email']
    cidade = obj['city']
    rua = obj['road']
    uf = obj['uf']
    bairro = obj['district']
    senha = obj['password']
    # Preencher usuario
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(
        nome + nome + nome + nome + nome + nome + nome + nome + nome)
    # Preencher nome
    driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
    # Preencher email
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    # Preencher telefone
    driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("99999999999")
    # Preencher cidade
    driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
    # Preencher rua
    driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
    # Preencher uf
    driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
    # Preencher bairro
    driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
    # Preencher senha
    driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
    # Preencher confirmar senha
    driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
    # botao
    driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

    # result = driver.find_element_by_class_name('alert-danger').text
    # print("RESULT -> ", result)
    # print("W3C ", driver.get_log(driver.log_types))
    print('\n Test ', webdriver.Proxy.httpProxy)
    assert "teste" in 'teste'