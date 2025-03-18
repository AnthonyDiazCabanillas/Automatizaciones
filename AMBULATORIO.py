from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configuración del WebDriver para Edge
driver = webdriver.Chrome()

try:

    # Abrir la página de inicio de sesión
    driver.get("https://192.168.42.155:4043/RceQA/Intranet/CuentasUsuario/LoginF.aspx")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "TxtDocIdentidad")))
    #Declaracion de variables para encontrar a los objetos
    usuario=driver.find_element(By.ID,"TxtDocIdentidad")
    password=driver.find_element(By.ID,"TxtClave")
    BtnIniSes=driver.find_element(By.ID,"btnIniciar")
    usuario.send_keys("09874925")
    password.send_keys("1234")
    BtnIniSes.click()
    time.sleep(3.0)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txboxBuscarMedico1")))
    Bus_Num=driver.find_element(By.ID,"txboxBuscarMedico1")
    Bus_Num.send_keys("40626304")
    time.sleep(2.0)
    Ele_Nom=driver.find_element(By.XPATH,"/html/body/ul[1]/li[2]/a")
    Ele_Nom.click()
    time.sleep(2.0)
    OPC_REA=driver.find_element(By.XPATH,"/html/body/form/div[4]/div[1]/div/div[9]/div/div/table/tbody/tr[1]/td[11]/div/a")
    OPC_REA.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/form/div[4]/div[1]/div/div[9]/div/div/table/tbody/tr[1]/td[11]/div/ul/li/a")))   
    REA_CIT=driver.find_element(By.XPATH,"/html/body/form/div[4]/div[1]/div/div[9]/div/div/table/tbody/tr[1]/td[11]/div/ul/li/a")
    REA_CIT.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"IdAceptarReapertura")))
    CON_BTN=driver.find_element(By.ID,"IdAceptarReapertura")
    CON_BTN.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @name='rbReaperturarAtencion' and @value='1']")))
    PAT_OPC=driver.find_element(By.XPATH, "//input[@type='radio' and @name='rbReaperturarAtencion' and @value='1']")
    PAT_OPC.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"IdReaperturarAtencion")))
    ACE_BTN=driver.find_element(By.ID,"IdReaperturarAtencion")
    ACE_BTN.click() 
    time.sleep(3.0)    
    #COMO SE VA A REABRIR UNA CITA NO ES NECESARIO ESTA LINEA YA QUE BUSCA LA OPCION SOLO CUANDO ESTA ABIERTA
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/form/div[4]/div[1]/div/div[9]/div/div/table/tbody/tr/td[9]/a/img")))
    #HC=driver.find_element(By.XPATH,"/html/body/form/div[4]/div[1]/div/div[9]/div/div/table/tbody/tr/td[9]/a/img")
    #HC.click()
    #time.sleep(2.0)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#form1 > div:nth-child(21) > table > tbody > tr:nth-child(2) > td:nth-child(1) > table > tbody > tr:nth-child(1) > td > div > label:nth-child(13)")))
    PRO_MED = driver.find_element(By.CSS_SELECTOR, "#form1 > div:nth-child(21) > table > tbody > tr:nth-child(2) > td:nth-child(1) > table > tbody > tr:nth-child(1) > td > div > label:nth-child(13)")
    PRO_MED.click()
    time.sleep(4.0)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "procedimientomedicov1realizado")))
    REA_PRO = driver.find_element(By.ID, "procedimientomedicov1realizado")
    REA_PRO.click()
    time.sleep(2.0)
    BUS_PRO=driver.find_element(By.ID,"ContentPlaceHolder1_txtProcedimientoMedicoBusqueda")
    BUS_PRO.send_keys("INYECCION")
    time.sleep(2.0)
    BTN_BUS=driver.find_element(By.ID,"ContentPlaceHolder1_imgBuscarProcedimientoMedico2")
    BTN_BUS.click()
    time.sleep(3.0)
    SEL_OPC =driver.find_element(By.CSS_SELECTOR,"#ContentPlaceHolder1_Buscador_ProcedimientoMedico_gvBusqueda > tbody > tr:nth-child(1) > td:nth-child(5)")
    SEL_OPC.click()
    time.sleep(2.0) 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"ContentPlaceHolder1_txtRelato")))
    REL_DES=driver.find_element(By.ID,"ContentPlaceHolder1_txtRelato")
    REL_DES.click()
    time.sleep(1.0)                    
    REL_DES.send_keys("PRUEBA AUTOMATIZADA")
    time.sleep(2.0)
    BTN_IMG=driver.find_element(By.XPATH,"/html/body/form/div[4]/table/tbody/tr[2]/td[1]/table/tbody/tr[1]/td/div/div[7]/div/div[1]/div[1]/div/div[2]/div[4]/div[1]/div[2]/div/input")
    BTN_IMG.click()
    time.sleep(5.0)        
    GUA_PRO=driver.find_element(By.XPATH, '//input[@class="BotonGeneral" and @value="Guardar Procedimiento"]')
    GUA_PRO.click()
    time.sleep(2.0)
    FIN_EVA=driver.find_element(By.ID,"ContentPlaceHolderBotonAcciones_btnEvaluacionFinalizar")
    FIN_EVA.click()
    time.sleep(3.0)
    #WebDriverWait(driver,10).unitl(EC.presence_of_element_located((By.ID,"txtFechaProxCita_")))
    time.sleep(2.0)
    FEC_CIT=driver.find_element(By.ID,"txtFechaProxCita_")
    FEC_CIT.send_keys("20/03/2025")
    time.sleep(3.0)
    #DARLE CLICK EN CUALQUIER PARTE
    actions = ActionChains(driver)
    actions.move_by_offset(100, 200).click().perform()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/footer/input")))
    BTN_ACE=driver.find_element(By.XPATH,"/html/body/div[3]/footer/input")
    BTN_ACE.click()
    BTN_ACE_2=driver.find_element(By.XPATH,"/html/body/div[3]/footer/div/div/input[1]")
    BTN_ACE_2.click()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2.0)
    ACE_FIN=driver.find_element(By.XPATH,"/html/body/div[3]/footer/input[1]")
    ACE_FIN.click()

    #PARA BUSCAR POR FECHAS PERO FALTA BUSCAR EL CALENDARIO FALTA CORREGIR
    
    #btnFechas=driver.find_element(By.ID,"_ckeckActivarrangofecha")
    #btnFechas.click()
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtfechaCitaIni")))
    #campo_fecha = driver.find_element(By.ID, "txtfechaCitaIni")
    #fecha_deseada = "2025-03-01"  # Formato: YYYY-MM-DD
    #driver.execute_script(f'document.querySelector("#txtfechaCitaIni").value = "{fecha_deseada}";')
    time.sleep(10000.0)


finally:
    
    # Cerrar el navegador

    driver.quit()
