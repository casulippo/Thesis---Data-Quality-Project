import os
import pandas as pd
import numpy as np
import time
import re
import sys
from datetime import date

sys.path.append ('../../')

# BeautifulSoup e Request

from bs4 import BeautifulSoup
import requests
from getuseragent import UserAgent




# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

useragent = UserAgent()

theuseragent = useragent.Random()
headers = {'User-Agent': theuseragent}
header = {
    "user-agent": theuseragent ,
    'referer':'https://www.google.com/'
}

def allow_cookies(driver) :
    print ('Decline Cookies')
    button_setting_cookies = driver.find_element (By.CSS_SELECTOR , "button.cookie-setting-link")
    button_setting_cookies.click ()
    time.sleep (np.random.choice ([x / 10 for x in range (7 , 22)]))
    button_confirm_cookies = driver.find_element (By.CSS_SELECTOR , "button.save-preference-btn-handler")
    # Conferma le mie scelte
    button_confirm_cookies.click ()


def next_page(driver) :
    print ('Changing page')
    next_button = driver.find_element (By.CSS_SELECTOR , "button.nextButton")
    next_button.click ()
    url = driver.current_url


def parse_url(url) :
    company_name = []
    job_title = []
    location = []
    company_rating = []
    job_age = []
    job_link = []

    r = requests.get (url , headers = header)
    soup = BeautifulSoup (r.text , 'html.parser')
    job_search_div = soup.select ('div#JobSearch') [0]
    a = job_search_div.select ('div#PageBodyContents')
    b = a [0].select ('div#JobResults')
    c = b [0].select ('article#MainCol')
    len_li = len (c [0].find_all ('li' , class_ = 'react-job-listing'))
    lis = c [0].find_all ('li' , class_ = 'react-job-listing')

    len_li = len (lis)
    df = pd.DataFrame ()

    for e in lis [0 :len_li] :
        try :
            company_name.append (e.find ('div').find ('a') ['title'])
        except :
            company_name.append (None)
        try :
            job_title.append (e ['data-normalize-job-title'])
        except :
            job_title.append (None)
        try :
            location.append (e ['data-job-loc'])
        except :
            location.append (None)
        try :
            company_rating.append (e.find ('span' , class_ = 'css-2lqh28'))  ### da controllare
        except :
            company_rating.append (None)
        try :
            job_age.append (e.find ("div" , {"data-test" : "job-age"}).text)
        except :
            job_link.append (None)
        try :
            link = "https://www.glassdoor.it" + e.find ("a" , {"data-test" : "job-link"}).get ("href")
            job_link.append (link)
        except :
            job_link.append (None)

    df ['company'] = company_name
    df ['job_title'] = job_title
    df ['location'] = location
    df ['company_rating'] = company_rating
    df ['job_age'] = job_age
    df ['job_link'] = job_link

    return df


def scraping_job_page(base_url , n_page=None) :
    start_time = time.time ()
    time_sleep = 0
    df_append = pd.DataFrame ()
    driver = webdriver.Chrome (r"C:\Users\Casulippo\Desktop\web_chromedriver\chromedriver.exe")
    # base_url = 'https://www.glassdoor.it/Lavoro/amsterdam-paesi-bassi-lavori-SRCH_IL.0,21_IC3064478.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&typedLocation=Amsterdam%2520(Paesi%2520Bassi)&context=Jobs&dropdown=0'
    driver.get (base_url)
    driver.maximize_window()
    a = np.random.choice ([x for x in range (3 , 5)])
    time_sleep = time_sleep + a
    time.sleep (a)
    url = driver.current_url
    
    allow_cookies (driver)
    a = np.random.choice ([x for x in range (3 , 5)])
    time_sleep = time_sleep + a
    time.sleep (a)
    r = requests.get (url , headers = header)

    text = BeautifulSoup (r.text , 'html.parser').find ('div' , attrs = {'class' : 'paginationFooter'}).text

    int_list = []
    for e in re.findall (r'-?\d+\.?\d*' , text) :
        int_list.append (int (e))

    if n_page == None :
        n_page = max (int_list)
    # n_page = 5
    print ('Numero di pagine sui cui fare scraping: ' + str (n_page))
    a = np.random.choice ([x for x in range (3 , 5)])
    time_sleep = time_sleep + a
    time.sleep (a)

    for page in range (n_page) :
        print (str (page + 1) + '/' + str (n_page))
        a = np.random.choice ([x for x in range (3 , 5)])
        time_sleep = time_sleep + a
        time.sleep (a)
        next_page (driver)
        url = driver.current_url
        if page == 0 :
            time.sleep (5)
            close_button = driver.find_element (By.CSS_SELECTOR , "svg.SVGInline-svg.modal_closeIcon-svg")
            close_button.click ()
        df = parse_url (url)
        df_append = df_append.append (df).reset_index (drop = True)

    driver.quit ()
    end_time = time.time ()
    print ('Done!')
    #print ('Total pages scraped:' , n_page , '\n')
    print ("Runtime:" , round (end_time - start_time) , "seconds" + '\nTime sleep:' , time_sleep , 'seconds')

    return df_append


def scraping_company_page(links , end_n_page=None , start_n_page=None) :
    start_time = time.time ()
    df_append_2 = pd.DataFrame ()
    time_sleep = 0
    n_link = 0
    ## lista dei link

    # base_url = 'https://www.glassdoor.it/job-listing/field-service-engineer-technician-lexas-JV_IC2802269_KO0,33_KE34,39.htm?jl=1008135983566&pos=101&ao=1110586&s=58&guid=000001861873f6d389d965e51ce717e2&src=GD_JOB_AD&t=SR&vt=w&uido=FEB79CBEB143B609D33C645CD13E2F4B&ea=1&cs=1_524e761d&cb=1675447498725&jobListingId=1008135983566&cpc=65CC663E25211861&jrtk=3-0-1goc77to1g2ev801-1goc77tp0i6id800-7cbed71e05432cdf--6NYlbfkN0CVO0F7mWis5ReNIXvK0Cy97GKSpj_H8mHyNoiV7tLwhxrGQFeFbXfrFFwDAnfvPXeiJe5SavTtAEQpKcpYVReYHZsV-4ZX7UeAkoBb0f_WCVWviQdPDhB0WcxVHddsJTu6CPWu9hRPncXvGLdy3ZffF5b3aOd7vp19QcNQdw0qQd1bkijbQHvL2CZX_Cxp4BGS1Sk8JgAjiz75HrAHRuR5hA9kjnxafzWfGAAOJBSKybBbJtFcKCvWC2Py0-IgF36KHcIY5QbFzm8TqI0WJJ75VyN8D93fcG7Ikeu9ECT-vBbPKtsVv7AOpI6elTa0KTJqDzeYeI39a8bHa5BUUOjrQ1rsJFwMGLJrLrbqXOIObHs1pSu_fpr-FcNbNcmvwdLQufgm_hOEka1AR5pS2jw3Kd3MEOLDniaBdQ1tk-tgoNuL5lhZNjQUe648ZgRuUWrLaIX3oHWCh15jyNqf9dfjjRB70aXgFCI2nC397dI72pLnPhLIqqOKxPTEV4El04FFBbjsdOPDp3q0LQurvyiZmQB21o9E3WEoCcol53Fx2g0SIc5ixunqT-a4RIeTz8CzvY7DdPxvqKSbekvmaTBa_UWB3gbtD9Y%253D&ctt=1675447519123'

    if start_n_page == None :
        start_n_page = 0
    if end_n_page == None :
        end_n_page = len (links)

    print ('link to scrape: ' , end_n_page - start_n_page)

    for base_url in links [start_n_page :end_n_page] :
        n_link += 1
        driver = webdriver.Chrome (r"C:\Users\Casulippo\Desktop\web_chromedriver\chromedriver.exe")
        driver.get (base_url)
        a = np.random.choice ([x for x in range (3 , 5)])
        time_sleep = time_sleep + a
        time.sleep (a)
        ## cookies
        allow_cookies (driver)
        a = np.random.choice ([x for x in range (3 , 5)])
        time_sleep = time_sleep + a
        time.sleep (a)
        ## Mapping dei bottoni
        general_button = driver.find_elements (By.CSS_SELECTOR , ".css-dkrzi8.e1eh6fgm0")
        button_mapping = {valore.text : indice for indice , valore in enumerate (general_button)}

        d_valutazione = {}
        d_azienda = {}

        print ('check the buttons-->' , n_link)
        try :
            general_button = driver.find_elements (By.CSS_SELECTOR , ".css-dkrzi8.e1eh6fgm0")

        except :
            print ('no buttons found')
            general_button = []

        if len (general_button) > 0 :

            try :

                azienda = general_button [button_mapping ['Azienda']]  # Azienda
                azienda.click ()
                a = np.random.choice ([x for x in range (3 , 5)])
                time_sleep = time_sleep + a
                time.sleep (a)
                pag_azienda_span = driver.find_elements (By.CSS_SELECTOR , ".css-vugejy.es5l5kg0 span.value")
                pag_azienda_value = driver.find_elements (By.CSS_SELECTOR , ".css-vugejy.es5l5kg0 label")

                azienda_span = []
                azienda_value = []

                for e in pag_azienda_span :
                    azienda_span.append (e.text)

                for e in pag_azienda_value :
                    azienda_value.append (e.text)
                d_azienda = dict (zip (azienda_value , azienda_span))
                print ('scraped company page')


            except :
                pass

            try :
                valutazione = general_button [button_mapping ['Valutazione']]  # Valutazione
                # recensioni = general_button[2] # Recensioni

                ## Cambio foglio
                valutazione.click ()
                pag_valutazione = driver.find_elements (By.CSS_SELECTOR , ".css-a7hxlj.e121l59f1")
                a = np.random.choice ([x for x in range (3 , 5)])
                time_sleep = time_sleep + a
                time.sleep (a)
                valutazione_1 = [pag_valutazione [0].text , pag_valutazione [2].text , pag_valutazione [4].text ,
                                 pag_valutazione [6].text , pag_valutazione [8].text]
                valutazione_2 = [pag_valutazione [1].text , pag_valutazione [3].text , pag_valutazione [5].text ,
                                 pag_valutazione [7].text , pag_valutazione [9].text]
                print ('scraped evaluation page')

                d_valutazione = dict (zip (valutazione_1 , valutazione_2))

            except :
                pass  # to add benefit e stipendio

        d = {**d_valutazione , **d_azienda}

        driver.quit ()

        df2 = pd.DataFrame.from_dict (d , orient = 'index').T
        df2 ['job_link'] = base_url

        df_append_2 = df_append_2.append (df2).reset_index (drop = True)

    end_time = time.time ()
    print ('Total pages scraped:' , len (links) , '\n')
    print ("Runtime:" , round (end_time - start_time) , "seconds" + '\nTime sleep: ' , time_sleep , 'seconds')
    df_append_2 = df_append_2.rename(columns={'Sede centrale':'sede_centrale',
                                    'Dimensioni':'dimensioni',
                                    'Fondata nel' : 'fondata_nel',
                                    'Tipo':'tipo',
                                    'Entrate':'entrate',
                                    # job_link
                                    'Opportunità di carriera': 'oppurtunita_carriera',
                                    'Stipendio e benefit':'stipendio_e_benefit',
                                    'Cultura e valori':'cultura_e_valori',
                                    'Dirigenti senior':'dirigenti_senior',
                                    'Equilibrio lavoro/vita privata':'equilibrio_lavoro_vita_privata',
                                    'Settore':'settore',
                                    'Segmento':'segmento'})

    return df_append_2