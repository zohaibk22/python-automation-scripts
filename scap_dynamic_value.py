from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service('/Users/zohaibkhan/Downloads/chromedriver')

# set options to make browsing easier
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-inforbars')
# ^^ disable info bars that show up in the browser, whcih can interfere with our script
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
# ^^ Browsers uses
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-feature=AutomationControlled')

    driver = webdriver.Chrome(service=service, options = options);
    driver.get('http://automated.pythonanywhere.com')
    return driver


def main():
    driver = get_driver()
    # element = driver.find_element_by_xpath('/html/body/div[1]/div/h1[1]')
    element = driver.find_element(by="xpath", value='/html/body/div[1]/div/h1[1]')
    print(element.text)
    return element

main()


