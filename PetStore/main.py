from selenium import webdriver
# Purpose: To start the testing environment
# NOTA: Ejecutar desde CMD o Windows Terminal con [python main.py] (tiene que estar ubicado en la carpeta C:\PetStore\)
def main():
        PATH = 'C:\PetStore\chromedriver.exe'
        driver = webdriver.Chrome(PATH)
        driver.get('https://petstore.octoperf.com/actions/Catalog.action')

main()
