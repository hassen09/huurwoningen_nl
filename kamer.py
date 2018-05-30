# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from selenium import webdriver
from urllib.parse import urljoin
from huurwoningen.items import HuurwoningenItem
import time
import re
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')

class huurwoningenSpider(scrapy.Spider):
    handle_httpstatus_list = [405, 456]
    name = "huurwoningen_mai"
    allowed_domains = ['huurwoningen.nl']
    start_urls = ['https://www.huurwoningen.nl/stedenoverzicht/']

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        driver=self.driver
        def parse_page(driver, page_url):
            base_url = "https://www.huurwoningen.nl"
            #options = webdriver.chrome.options.Options()
            #options.add_argument("--disable-extensions")
            #driver = webdriver.Chrome()
            driver.get(page_url)    
            link=''
            try:
                link=driver.find_element_by_xpath('//div[@class="listing__body"]/a').get_attribute("href")
            except:
                pass
            while link=='':
                time.sleep(2)
                try:
                    link=driver.find_element_by_xpath('//div[@class="listing__body"]/a').get_attribute("href")
                except:
                    pass
            hxs = Selector(text=driver.page_source)
            data = hxs.xpath('//a[@class="listing__link"]')
            items = []
            try:
                next_page=driver.find_element_by_xpath('//span[@class="pagination__label"][text()="Volgende"]/parent::span/parent::a').get_attribute("href")
                if next_page is not None:
                    next_page=urljoin(base_url, next_page)
            except:
                next_page=''
            for datum in data:
                item = HuurwoningenItem()
                #d = {}
                href=datum.xpath('./@href').extract()[0]
                url=urljoin(base_url, href)
                driver.get(url)
                link=''
                try:
                    link=driver.find_element_by_xpath('//link[@rel="canonical"]').get_attribute("href")
                except:
                    pass
                while link=='':
                    time.sleep(2)
                    try:
                        link=driver.find_element_by_xpath('//link[@rel="canonical"]').get_attribute("href")
                    except:
                        pass
                link = urljoin(base_url, link)
                id_client=re.findall(r'[0-9]+', link)[0]
                try:
                    prix=driver.find_element_by_xpath('//div[@class="price price--hero"]/span[@class="price__value"]').text
                    prix=re.findall(r'[0-9\.]+', prix)[0]
                except:
                    prix=''
                print("--------------------------------------",prix)
                #try:
                    #annonce_date=driver.find_element_by_xpath('//td[text()="Te huur vanaf"]/following-sibling::td').text
                #except:
                    #annonce_date=''
                try:
                    nom=driver.find_element_by_xpath('//h1[@class="title__listing"]').text
                except:
                    nom=''
                try:
                    local=driver.find_element_by_xpath('//p[@class="title__sub"]').text
                    cp=re.findall(r'[0-9]+ [A-Z]+', local)[0]
                    province=re.findall(r'\((.*)\)', local)[0]
                    ville=re.findall(r'([a-zA-Z]+) \(', local)[0]
                except:
                    local=''
                    cp=''
                    province=''
                    ville=''
                try:
                    adresse=driver.find_element_by_xpath('//dt[text()="Adres"]/following-sibling::dd/a').text
                except:
                    adresse=''
                try:
                    latitude=driver.find_element_by_xpath('//meta[@itemprop="latitude"]').get_attribute("content")
                except:
                    latitude=''
                try:
                    longitude=driver.find_element_by_xpath('//meta[@itemprop="longitude"]').get_attribute("content")
                except:
                    longitude=''
                try:
                    categorie=driver.find_element_by_xpath('//dt[text()="Type aanbod"]/following-sibling::dd').text
                except:
                    categorie=''
                if "Huis" in categorie:
                    maison_apt="1"
                elif "Appartement" in categorie:
                    maison_apt="2"
                elif "Kamer" in categorie:
                    maison_apt="3"
                elif "Bedrijfsruimte" in categorie:
                    maison_apt="5"
                else:
                    maison_apt="8"
                try:
                    annonce_text=driver.find_element_by_xpath('//section[@class="widget widget--listing-description"]/section[@class="widget__body"]').text
                    annonce_text=annonce_text.replace('\n', '')
                    annonce_text=annonce_text.replace('Meer informatie? Of direct contact met de verhuurder?', '')
                except:
                    annonce_text=''
                try:
                    m2_total=driver.find_element_by_xpath('//dt[text()="Woonoppervlakte"]/following-sibling::dd').text
                    m2_total=re.findall(r'[0-9\.]+', m2_total)[0]
                except:
                    m2_total=''
                try:
                    piece=driver.find_element_by_xpath('//dt[text()="Aantal kamers"]/following-sibling::dd').text
                except:
                    piece=''
                try:
                    photo=driver.find_element_by_xpath('//span[@class="icon icon--slider"]/following-sibling::span').text
                    photo=re.findall(r'[0-9]+', photo)[0]
                except:
                    photo=''
                #d = {'ANNONCE_LINK': link, 'FROM_SITE': 'kamers', 'ID_CLIENT': id_client, 'ANNONCE_DATE': annonce_date, 'ACHAT_LOC': '2', 'MAISON_APT': maison_apt,     'CATEGORIE': categorie, 'NEUF_IND': '', 'NOM': nom, 'ADRESSE': adresse, 'CP': '', 'VILLE': ville, 'QUARTIER': '', 'DEPARTEMENT': '', 'REGION': '', 'PROVINCE': '',     'ANNONCE_TEXT': annonce_text, 'ETAGE': '', 'NB_ETAGE': '', 'LATITUDE': '', 'LONGITUDE': '', 'M2_TOTALE': m2_total, 'SURFACE_TERRAIN': '', 'NB_GARAGE': '', 'PHOTO': photo, 'PIECE': piece, 'PRIX': prix, 'PRIX_M2': '', 'URL_PROMO': '', 'PAYS_AD': 'NL', 'PRO_IND': '', 'SELLERTYPE': '', 'MINI_SITE_URL': '', 'MINI_SITE_ID': '', 'AGENCE_NOM': '', 'AGENCE_ADRESSE': '', 'AGENCE_CP': '', 'AGENCE_VILLE': '', 'AGENCE_DEPARTEMENT': '', 'EMAIL': '', 'WEBSITE': '', 'AGENCE_TEL': '', 'AGENCE_TEL_2': '', 'AGENCE_TEL_3': '', 'AGENCE_TEL_4': '', 'AGENCE_FAX': '', 'AGENCE_CONTACT': '', 'PAYS_DEALER': '', 'FLUX': '', 'SITE_SOCIETE_URL': '', 'SITE_SOCIETE_ID': '', 'SITE_SOCIETE_NAME': '', 'AGENCE_RCS': '', 'SPIR_ID': ''}
                item['ANNONCE_LINK'] = link
                item['FROM_SITE'] = 'huurwoningen'
                item['ID_CLIENT'] = id_client
                item['ANNONCE_DATE'] = ''
                item['ACHAT_LOC'] =  '2'
                item['MAISON_APT'] = maison_apt
                item['CATEGORIE'] = categorie
                item['NEUF_IND'] = ''
                item['NOM'] = nom
                item['ADRESSE'] = adresse
                item['CP'] = cp
                item['VILLE'] = ville
                item['QUARTIER'] = ''
                item['DEPARTEMENT'] = ''
                item['REGION'] = ''
                item['PROVINCE'] = province
                item['ANNONCE_TEXT'] = annonce_text
                item['ETAGE'] = ''
                item['NB_ETAGE'] = ''
                item['LATITUDE'] = latitude
                item['LONGITUDE'] = longitude
                item['M2_TOTALE'] = m2_total
                item['SURFACE_TERRAIN'] = ''
                item['NB_GARAGE'] = ''
                item['PHOTO'] = photo
                item['PIECE'] = piece
                item['PRIX'] = prix
                item['PRIX_M2'] = ''
                item['URL_PROMO'] = ''
                item['PAYS_AD'] = 'NL'
                item['PRO_IND'] = ''
                item['SELLERTYPE'] = ''
                item['MINI_SITE_URL'] = ''
                item['MINI_SITE_ID'] = ''
                item['AGENCE_NOM'] = ''
                item['AGENCE_ADRESSE'] = ''
                item['AGENCE_CP'] = ''
                item['AGENCE_VILLE'] = ''
                item['AGENCE_DEPARTEMENT'] = ''
                item['EMAIL'] = ''
                item['WEBSITE'] = ''
                item['AGENCE_TEL'] = ''
                item['AGENCE_TEL_2'] = ''
                item['AGENCE_TEL_3'] = ''
                item['AGENCE_TEL_4'] = ''
                item['AGENCE_FAX'] = ''
                item['AGENCE_CONTACT'] = ''
                item['PAYS_DEALER'] = ''
                item['FLUX'] = ''
                item['SITE_SOCIETE_URL'] = ''
                item['SITE_SOCIETE_ID'] = ''
                item['SITE_SOCIETE_NAME'] = ''
                item['AGENCE_RCS'] = ''
                item['SPIR_ID'] = ''
                items.append(item)


            try:
                next_itmes = parse_page(driver, next_page)
                items = items + next_itmes

            except:
                pass
            return items
            #driver.stop_client()
            #driver.close()
            #try:
            #if next_page is not None:
            #return parse_page(next_page)
            #except:
                #pass


        #return parse_page(driver, response.url)
        items = []
        base_url = "https://www.huurwoningen.nl"

        for i in response.xpath('//div[@class="grid__body"]//a[@class="list__link"]'):
                #d = {}
          
            href=i.xpath('./@href').extract()[0]
            city_url=urljoin(base_url, href)
            city_items = parse_page(driver, city_url)
            items = items + city_items
         
        return items


