from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import xlrd
from time import sleep

### Usar diccionarios en vez de matrices
path = r"C:\Users\Salvador\Downloads\chromedrive\chromedriver.exe"

trabajos = []
empresas = []
class indeedBot():
    def __init__(self):
        self.driver = webdriver.Chrome(path)

    def lookup(self):
        self.driver.get('https://www.indeed.com.mx/')

    def search(self):
        #oficio = input("Ingresa el trabajo que quieras buscar: ")
        lookbar = self.driver.find_element_by_xpath('//*[@id="text-input-what"]')
        lookbar.send_keys('Discapacidad') #oficio
        #lugar = input("Ingrese la zona que desea buscar: ")
        lookzone = self.driver.find_element_by_xpath('//*[@id="text-input-where"]')
        lookzone.send_keys('Zapopan') #lugar
        lookbutton = self.driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
        lookbutton.click()

    def scrap(self):
        location = self.driver.current_url
        str(location)
        source = requests.get(location).text
        soup = BeautifulSoup(source, 'lxml')
        #titulos = soup.find_all("div", class_ = 'summary')
        for ultag in soup.find_all('div', {'class': 'summary'}):
            for litag in ultag.find_all('li'):
                print(litag.text)
        #print(titulos)
        #title = self.driver.find_element_by_xpath('//*[@id="sja0"]')
        #title.getText()
        #trabajos.append(title)
        #empresas = self.driver.find_element_by_xpath('//*[@id="pj_8d3c8881c4f155ca"]/div[2]/div[1]/span[1]/a')
        #empresas.getText()
        #empresas.append(empresas)
        #print(trabajos)
        #print(empresas)

bot = indeedBot()
bot.lookup()
bot.search()
bot.scrap()
