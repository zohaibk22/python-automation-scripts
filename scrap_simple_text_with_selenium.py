from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


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


def clean_text(text):
    """Extracts only the temperature from text
    """
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    time.sleep(2)
    # element = driver.find_element_by_xpath('/html/body/div[1]/div/h1[1]')
    element = driver.find_element(by="xpath", value='/html/body/div[1]/div/h1[2]')
    print(clean_text(element.text))
    return clean_text(element.text)

main()


