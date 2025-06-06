from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Configuración del WebDriver para Edge
driver = webdriver.Chrome()

try:

    # Abrir la página de inicio de sesión   
    driver.get("https://pruebas.clinicasanfelipe.com/CSF_CITASWEB_QA/")
    driver.maximize_window()
    time.sleep(5.0)
    #Declaracion de variables para encontrar a los objetos
    usuario=driver.find_element(By.ID,"txt_LO_Usuario")
    password=driver.find_element(By.ID,"txt_LO_Contrasena")
    BtnIniSes=driver.find_element(By.ID,"btn_LO_Ingresar")
    usuario.send_keys("jdiaz")
    password.send_keys("Tonydc090624")
    BtnIniSes.click()
    time.sleep(5.0)
    flecha=driver.find_element(By.ID,"btn_LA_Toggle")
    flecha.click()
    time.sleep(1.0)
    Gestion_Proc=driver.find_element(By.LINK_TEXT,"Gestión de Procedimientos")
    Gestion_Proc.click()
    time.sleep(3.0)
    sede=driver.find_element(By.ID,"cboGPSedeFiltro")
    sede.click()
    select = Select(sede)
    select.select_by_visible_text("La Molina")
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    servicio=driver.find_element(By.ID,"cboGPServicioFiltro")
    servicio.click()
    select = Select(servicio)
    select.select_by_visible_text("Medicina del deporte")
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    especialidad=driver.find_element(By.ID,"cboGPEspecialidadFiltro")
    especialidad.click()
    select = Select(especialidad)
    select.select_by_visible_text("CARDIOLOGIA")
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    tecnologo=driver.find_element(By.ID,"txt_GP_Tecnologo")
    tecnologo.click()
    tecnologo.send_keys("PRUEBAAPE PRUEBAMAT PRUEBA (CTMP-1111111111)")
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    box_gim=driver.find_element(By.ID,"cboGPSalaFiltro")
    box_gim.click()
    select = Select(box_gim)
    select.select_by_visible_text("Gimnasio 1")
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    time.sleep(2.0)
    BtnBuscar = driver.find_element(By.ID,"btnBuscar")
    BtnBuscar.click()
    time.sleep(12.0)
    horario=driver.find_element(By.CSS_SELECTOR,"div[data-idserviciohorario='16'][data-fecha='15/03/2025'][data-horainiciocelda='08:00']")
    horario.click()
    time.sleep(4.0)
    Txt_dni=driver.find_element(By.ID,"txt_GP_MdlCC_NumeroDocumento")
    Txt_dni.send_keys(74847349)
    time.sleep(2.0)
    COD_ATE=driver.find_element(By.ID,"txt_GP_MdlCC_CodigoAtencion")
    COD_ATE.send_keys("MFHJELO2134")
    Tip_Pac=driver.find_element(By.ID,"cbo_GP_MdlCC_TipoPaciente")
    Tip_Pac.click()
    select = Select(Tip_Pac)
    select.select_by_visible_text("Particular")
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    tip_ter=driver.find_element(By.ID,"cbo_GP_MdlCC_TipoTerapia")
    tip_ter.click
    tip_ter.click()
    select = Select(tip_ter)
    select.select_by_visible_text("Readaptación")
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    Obs_Txt=driver.find_element(By.ID,"txa_GP_MdlCC_Observaciones")
    Obs_Txt.send_keys("PRUEBAS AUTOMATIADAS EQUIPO QA")
    time.sleep(2.0)
    Btn_Conf=driver.find_element(By.ID,"mdl_GP_ConfirmaCita_Boton_1")
    Btn_Conf.click()
    time.sleep(2.0)
    time.sleep(10000.0)


finally:
    
    # Cerrar el navegador
    driver.quit()
