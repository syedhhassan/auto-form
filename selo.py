from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import pandas as pd
import time

path = "cdr/chromedriver"
serve = Service(path)
website = 'https://forms.gle/Qv6zJxrWsR5ahuaQ6'
driver = webdriver.Chrome(service = serve)

df = pd.read_csv("data.csv")
driver.get(website)
time.sleep(5)

for i in range(0, len(df)):
    for column in df.columns:
        text_input = driver.find_element(by='xpath', value=f'//div[contains(@data-params, "{column}")]//input |'
                                        f'//div[contains(@data-params, "{column}")]//textarea')
        text_input.send_keys(df.loc[i, column])
    submit_button = driver.find_element(by='xpath', value='//div[@role="button"]//span[text()="Submit"]')
    submit_button.click()

driver.quit()