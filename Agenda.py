from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
# Configuración del WebDriver para Edge
driver = webdriver.Chrome() 
try:
    # Abrir la página de inicio de sesión
    driver.get("https://192.168.42.155:4043/CSF_SIRI_PREQA/")
    driver.maximize_window()
    time.sleep(2.0)
    #Declaracion de variables para encontrar a los objetos
    BtnRepInc= driver.find_element(By.ID,"btn_LO_Ingresar_Reporta_Inicidente")
    BtnRepInc.click()
    time.sleep(1.0)
    BtnDoc= driver.find_element(By.ID,"FORM_ID_DOCUMENT_TYPE_SELECT")
    BtnDoc.click()
    select = Select(BtnDoc)
    select.select_by_visible_text("DNI")
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    time.sleep(2.0)
    TxtDoc=driver.find_element(By.ID,"FORM_ID_DOCUMENT_NUMBER_INPUT")
    TxtDoc.send_keys("000999111")
    time.sleep(0.5)
    TxtNom=driver.find_element(By.ID,"FORM_ID_FULL_NAME_INPUT")
    TxtNom.send_keys("Tony was here")





    #Luego de ingresar a la opcion de reportar incidente
    time.sleep(15.0)


finally:
    
    # Cerrar el navegador
    driver.quit()
