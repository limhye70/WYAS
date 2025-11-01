from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
import pickle
from constant import URL

XPATH_PARAMS = {
    'timestamp': '//*[@id="trend-table"]/div[1]/table/thead/tr/th[1]/div/span',
    'body': '//*[@id="trend-table"]/div[1]/table/tbody[2]',
    'all': '//*[@id="trend-table"]'
    }


def scrapper(xpath_params=XPATH_PARAMS):
    # output dictionary
    scrapping_output = {}

    # scrapping
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-blink-features=AutomationControlled") # Hide automation traces

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        print(URL)
        driver.get(URL)
        time.sleep(5)

        for key, xpath in xpath_params.items():
            elem = driver.find_element(By.XPATH, xpath)
            text = elem.text.replace('\u202f', ' ').replace('–', '-')
            with open(f"data/{key}.txt", "w", encoding='utf-8') as file:
                file.write(text)

            lines = text.split('\n')
            scrapping_output[key] = lines

        # save output as .pickle
        with open(f'data/scrapping_output.pickle', 'wb') as file:
            pickle.dump(scrapping_output, file)
        return scrapping_output

    except Exception as e:
        print(f"Error: {e}")
        return None


def read_trends(xpath_params=XPATH_PARAMS):
    scrapping_output = scrapper(xpath_params=XPATH_PARAMS)
    with open('data/scrapping_output.pickle', 'rb') as file:
        scrapping_output = pickle.load(file)

    print(f'Data has been pulled {scrapping_output['timestamp'][0]}')

    # reshape data into a dataframe
    headers = ['Keywords', 'Search Volume', 'Trend Indicator', 'Increase %', 'Started', 'Status', 'Duration']
    table_body = scrapping_output['body']

    data = []
    for i in range(0, len(table_body), 7):
        row = [table_body[i], table_body[i+1], table_body[i+2], table_body[i+3], table_body[i+4], table_body[i+5], table_body[i+6]]
        data.append(row)

    df = pd.DataFrame(data, columns=headers)
    df.to_csv('data/trends_table.csv', index=False, encoding='utf-8-sig')


if __name__ == "__main__":
    read_trends()

    