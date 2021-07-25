from selenium import webdriver
import os

driver_path = os.path.join('chromedriver','chromedriver')
brave_path = '/usr/bin/brave-browser'
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
# options.binary_location = brave_path
# browser = webdriver.Chrome(executable_path=driver_path, options=options)
browser.get("https://www.rappi.com.co/login")
browser.implicitly_wait(20)
phone_number_field = browser.find_elements_by_css_selector('div.input-phone input')[0]
if phone_number_field.is_enabled():
    phone_number = input('Input phone number to use: ')
    phone_number_field.send_keys(phone_number)
    browser.find_element_by_css_selector('.secondary-button-outlined.auth-btn.sms-button div.btn-auth-title.f-caption-1').click()
    received_code = input(f'Input the code received by SMS to the phone number {phone_number}: ')
    received_code_field = browser.find_element_by_css_selector('input.number.ng-pristine.ng-invalid.ng-touched')
    received_code_field.send_keys(received_code)
    browser.find_element_by_css_selector('button.primary-button-filled.btn-check-auth').click()
    browser.find_element_by_css_selector('i.iconf-more-stores').click()
    browser.find_element_by_xpath('//a[@title="Licores"]').click()
    seach_field = browser.execute_script("document.querySelector('header-gema').shadowRoot.querySelector('.header-container div.search-container.focus input')")
    seach_field.send_keys('ron')
    print('script finished!')
else:
    print('phone number field not enabled')
# browser.maximize_window()

# login_button = browser.execute_script("return document.querySelector('header-gema').shadowRoot.querySelector('.login-btn')")
# login_button.click()
# browser.close()