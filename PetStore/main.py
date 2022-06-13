from selenium import webdriver
def main():
  PATH = 'C:\Program Files (x86)\chromedriver.exe'
  driver = webdriver.Chrome(PATH)

  driver.get('https://petstore.octoperf.com/actions/Catalog.action')
main()
