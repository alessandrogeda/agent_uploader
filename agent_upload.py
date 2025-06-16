from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def invia_form(email_destinatario, file_path):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://gaatorg222org.preload.site/wp-login.php")
        time.sleep(2)
        driver.find_element(By.ID, "user_login").send_keys("shop@printshoptorino")
        driver.find_element(By.ID, "user_pass").send_keys("Timbuctu1@")
        driver.find_element(By.ID, "wp-submit").click()
        time.sleep(3)

        driver.get("https://gaatorg222org.preload.site/upload-agenti/")
        time.sleep(2)
        driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(email_destinatario)
        driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(file_path)
        driver.find_element(By.XPATH, '//button[contains(text(), "Invia") or @type="submit"]').click()
        time.sleep(3)

        return True, ""
    except Exception as e:
        return False, str(e)
    finally:
        driver.quit()
