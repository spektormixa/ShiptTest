from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class PartnerForm():

    def form_test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        base_url = "https://www.shipt.com/"
        driver.get(base_url)
        driver.implicitly_wait(10)

        # Scroll to footer
        driver.execute_script("window.scrollBy(0, 750);")
        # Adding sleep just for demo!
        time.sleep(1)

        partner_us = driver.find_element(By.XPATH, "//a[@href = '/partner/']")
        partner_us.click()

        # Scroll to partner form
        driver.execute_script("window.scrollBy(0, 700);")
        # Adding sleep just for demo!
        time.sleep(1)

        # Input valid name
        name = driver.find_element_by_id("your-name")
        name.click()
        name.send_keys("John Doe")

        # Input valid email
        email = driver.find_element_by_id("email")
        email.click()
        email.send_keys("john.doe@gmail.com")

        # Company name imput
        company = driver.find_element_by_id("company-name")
        company.click()
        company.send_keys("Boring Company")

        # Type of Company
        type_company = driver.find_element_by_id("company-type")
        type_company.click()
        type_company.send_keys("Infrastructure and tunnel construction company")

        # How we can work description
        work_description = driver.find_element_by_id("message")
        work_description.click()
        work_description.send_keys("Usage of tunnels for grocery delivery")

        # Sending request
        send_data = driver.find_element(By.XPATH, "//input[@type = 'submit']")
        send_data.click()

        result = driver.find_element(By.XPATH,
                                     "//div[@class = 'wpcf7-response-output wpcf7-display-none wpcf7-mail-sent-ok']")
        if result:
            print("Your message was sent successfully")
        else:
            print("Your message was not send")

        driver.close()


ff = PartnerForm()
ff.form_test()