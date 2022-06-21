from selenium import webdriver
from selenium.webdriver.common.by import By

def saveResult (offers, page):
    fileCsv = open(f'seminovos_{page}.csv', 'a')
    fileCsv.write('make;model;version;year_manufacture;year_model;km;price;location\n')

    i = 1

    for eachOffer in offers:
        makeModel = eachOffer.find_element(By.CSS_SELECTOR, 'a.font-roboto-700-20px').text.split(' ', 1)
        version = eachOffer.find_element(By.CSS_SELECTOR, 'div.font-roboto-400-12px').text
        years = eachOffer.find_element(By.CSS_SELECTOR, 'span.ano_fabricacao_modelo').text.split('/')
        km = eachOffer.find_element(By.CSS_SELECTOR, 'span.quilometragem').text
        price = eachOffer.find_element(By.CSS_SELECTOR, 'div.font-roboto-700').text
        location = eachOffer.find_element(By.CSS_SELECTOR, 'span.font-roboto-400').text

        print ("\n===========================")
        print (f"== PAGE {page} | Offer {i}/100")
        print ("===========================")
        print (f'Make: {makeModel[0]}')
        print (f'Model: {makeModel[1]}')
        print (f'Version: {version}')
        print (f'Year: {years[0]} / {years[1]}')
        print (f'Km: {km}')
        print (f'Price: {price}')
        print (f'Location: {location}')
        print ("===========================\n")

        fileCsv.write(f'{makeModel[0]};{makeModel[1]};{version};{years[0]};{years[1]};{km};{price};{location}\n')
        i += 1

    fileCsv.close()


driver = webdriver.Chrome() 

for page in range(2, 26):
    driver.get('https://seminovos.unidas.com.br/veiculos?page={}&perpage=100&layout=grid'.format(page)) 
    driver.maximize_window() 

    driver.implicitly_wait(10) 

    resultOffers = driver.find_elements(By.CSS_SELECTOR, "div.veiculo") 

    saveResult(resultOffers, page)


driver.quit()


