from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd


def acesso_usuario(user, senha):
    options = Options()
    options.headless = True #executar de forma visivel ou oculta

    navegador = webdriver.Firefox(options=options)

    link = "https://siga.cps.sp.gov.br/aluno/login.aspx"

    navegador.get(url=link)
    sleep(1)

    inputUsuario = navegador.find_element(by=By.ID, value="vSIS_USUARIOID")
    inputUsuario.send_keys(user)
    sleep(1)

    inputSenha = navegador.find_element(by=By.ID, value="vSIS_USUARIOSENHA")
    inputSenha.send_keys(senha)
    sleep(1)

    buttonLogin = navegador.find_element(by=By.NAME, value="BTCONFIRMA")
    buttonLogin.click()
    sleep(2)

    return navegador

def horario(navegador):
    try:
        linkHorario = navegador.find_element(by=By.ID, value="ygtvlabelel9")
        linkHorario.click()
        sleep(2)

        sobre = navegador.find_element(by=By.ID, value="MPW0041TABLE2")
        grade = navegador.find_element(by=By.ID, value="Grid1ContainerTbl")
        segunda  = navegador.find_element(by=By.ID, value="Grid2ContainerTbl")
        terca  = navegador.find_element(by=By.ID, value="Grid3ContainerTbl")
        quarta  = navegador.find_element(by=By.ID, value="Grid4ContainerTbl")
        quinta  = navegador.find_element(by=By.ID, value="Grid5ContainerTbl")
        sexta  = navegador.find_element(by=By.ID, value="Grid6ContainerTbl")
        sabado  = navegador.find_element(by=By.ID, value="Grid7ContainerTbl")

        dias_tables = [sobre, grade, segunda, terca, quarta, quinta, sexta, sabado]
        semana = ["sobre", "grade", "segunda","terca","quarta","quinta","sexta","sabado"]
        d = 0 

        for dia in dias_tables:
            conteudo_html = dia.get_attribute("outerHTML")
            soup = BeautifulSoup(conteudo_html, "html.parser")
            tabela = soup.find(name="table")
            df = pd.read_html(str(tabela))[0]
            df = df.dropna(axis=1)
            df.to_csv("FatecCalendar/grade/" + str(semana[d]) + ".csv", encoding="UTF-8", sep=",", index=False)
            d = d + 1
        
    except WebDriverException as erro:
        #print("Erro - exceção Webdriverexception: ", erro, file=sys.stderr)
        respostaLogin = navegador.find_element(by=By.ID, value="span_vSAIDA")
        return respostaLogin.text
        
def sobre(navegador):
    try:
        
        nome_completo = navegador.find_element(by=By.ID, value="span_MPW0041vPRO_PESSOALNOME")
        ra_sem = navegador.find_element(by=By.ID, value="MPW0041TABLE7")
        rendimento = navegador.find_element(by=By.ID, value="MPW0041TEXTBLOCK9")
        pr = navegador.find_element(by=By.ID, value="MPW0041TABLE8")
        prazo_in = navegador.find_element(by=By.ID, value="MPW0041TEXTBLOCK4")
        curs_max_falt = navegador.find_element(by=By.ID, value="MPW0041TABLE9")
        titulo_email = navegador.find_element(by=By.ID, value="MPW0041TEXTBLOCK15")
        email = navegador.find_element(by=By.ID, value="MPW0041TABLE10")


        informacoes_aluno = [ nome_completo, ra_sem, rendimento, pr, prazo_in, curs_max_falt, titulo_email, email]
        lista = ["nome_completo", "ra_sem", "rendimento", "pr", "prazo_in", "curs_max_falt", "titulo_email", "email"]
        d = 0 

        for i in informacoes_aluno:
            conteudo_html = i.get_attribute("outerHTML")
            soup = BeautifulSoup(conteudo_html, "html.parser")
            tabela = soup.find(name="table")
            df = pd.read_html(str(tabela))[0]
            df = df.dropna(axis=1)
            df.to_csv("FatecCalendar/infoAluno/" + str(lista[d]) + ".csv", encoding="UTF-8", sep=",", index=False)
            d = d + 1
        
    except WebDriverException as erro:
        #print("Erro - exceção Webdriverexception: ", erro, file=sys.stderr)
        respostaLogin = navegador.find_element(by=By.ID, value="span_vSAIDA")
        return respostaLogin.text
