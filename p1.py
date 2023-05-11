from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

repeat = int(input("Enter number of times to refresh: "))
vid_link = input("Enter video link: ")

with open('file.txt', 'r') as f:
    data = f.read().strip()
    

email_password_pairs = data.split('\n')
emails = []
passwords = []
recovery_emails = []

for pair in email_password_pairs:
    email, password, recovery_email = pair.split(',')
    emails.append(email.strip())
    passwords.append(password.strip())
    recovery_emails.append(recovery_email.strip())

#PATH = "chromedriver.exe"
options = Options()
options.add_argument("--incognito")
stay = int(input("How long do you want to stay at the ads page: "))


for j in range(len(emails)):

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S436374091%3A1679685918790258&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AQMjQ7Tos8bu5al_oag8obsSoUTPD2llnWo0NICjAkFIMgTCtr6vQ1aZG6nuCciL9Zo3y5IQhLZ5eA&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin")


    email_field = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/span[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    email_field.send_keys(emails[j])

    wait = WebDriverWait(driver, 50)

    next_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]')))
    next_button.click()


    password_field = wait.until(EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/span[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')))
    password_field.click()
    password_field.send_keys(passwords[j])

    sleep(1)

    next_button2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    next_button2.click()
    sleep(5)
    try:
        wait = WebDriverWait(driver, 8)
        confirm_recovery = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > ul > li:nth-child(3) > div > div.vxx8jf")))
        confirm_recovery.click()
        sleep(4)
        recovery_email_field = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input")))

        recovery_email_field.send_keys(recovery_emails[j])
        sleep(1)
        next_button = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
        next_button.click()
        sleep(3)
    except:
        pass
    try:
        driver.get('https://myaccount.google.com/notifications')
        wait = WebDriverWait(driver, 5)
        first = wait.until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/c-wiz[1]/div[1]/div[2]/div[2]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[2]/div[1]/div[1]")))
        first.click()
        sleep(5)
        wait = WebDriverWait(driver, 10)
        second = wait.until(EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/c-wiz[1]/div[1]/div[2]/div[2]/c-wiz[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/button[2]/span[1]")))
        second.click()  
        sleep(8)

    except:
        pass
    sleep(5)
    driver.get(vid_link)
    for i in range(repeat):
        try:
            sleep(5)
            ad1 = driver.find_element(By.CSS_SELECTOR,"#action > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill")
            ad1.click()
        except:
            try:
                ad2 = driver.find_element(By.CSS_SELECTOR,"#action-button > ytd-button-renderer > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill")
                ad2.click()
            except:
                driver.refresh()
                sleep(6)
                continue

        sleep(stay)
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
 
    driver.quit()


#https://www.youtube.com/watch?v=aS7OyTgpgCQ