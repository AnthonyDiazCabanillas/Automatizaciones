from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuración del WebDriver para Edge
driver = webdriver.Chrome()

try:

    # Abrir la página de inicio de sesión
    driver.get("https://citaweb.clinicasanfelipe.com/CSF_CITAS/")
    driver.maximize_window()
    time.sleep(5.0)
    #Declaracion de variables para encontrar a los objetos
    usuario=driver.find_element(By.ID,"txtDni")
    password=driver.find_element(By.ID,"txtClave")
    BtnIniSes=driver.find_element(By.ID,"btnLogin")
   
   
    #Ingresar datos y procedimientos

    usuario.send_keys("74847349")
    password.send_keys("Tonydc1502%")
    BtnIniSes.click()
    time.sleep(5.0)


finally:
    
    # Cerrar el navegador
    driver.quit()
