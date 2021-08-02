from selenium import webdriver
import os

# driver_path = os.path.join('chromedriver','chromedriver')
# brave_path = '/usr/bin/brave-driver'
def access_page():

    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
    driver.get("https://www.rappi.com.co/login")
    driver.implicitly_wait(20)
    return driver

def input_phone_number(driver, phone_number):

    phone_number_field = driver.find_elements_by_css_selector('div.input-phone input')[0]
    if phone_number_field.is_enabled():
        phone_number_field.send_keys(phone_number)
        driver.find_element_by_css_selector(
            '.secondary-button-outlined.auth-btn.sms-button div.btn-auth-title.f-caption-1'
         ).click()
    return driver 

def input_code(driver, received_code):

    received_code_field = driver.find_element_by_css_selector(
        'input.number.ng-pristine.ng-invalid.ng-touched'
    )
    received_code_field.send_keys(received_code)
    driver.find_element_by_css_selector(
        'button.primary-button-filled.btn-check-auth'
    ).click()
        
def access_liquors_section(driver):
    
    driver.find_element_by_css_selector('i.iconf-more-stores').click()
    driver.find_element_by_xpath('//a[@title="Licores"]').click()
    search_field = driver.execute_script("document.querySelector('header-gema').shadowRoot.querySelector('.header-container div.search-container.focus input')")
    return search_field

def search_products(search_field, products):

    search_field.send_keys(products)
