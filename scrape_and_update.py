import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

def extract_text(soup, tag, class_name):
    element = soup.find(tag, class_=class_name)
    return element.text.strip() if element else None

def scrape_data():
    url = "https://www.crunchbase.com/organization/stripe"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    revenue = extract_text(soup, 'span', 'component--field-formatter field-type-money')
    valuation = extract_text(soup, 'span', 'component--field-formatter field-type-money')
    funding_rounds_elements = soup.find_all('span', 'component--field-formatter field-type-money')
    funding_data = [elem.text.strip() for elem in funding_rounds_elements]
    employee_count = extract_text(soup, 'span', 'component--field-formatter field-type-enumeration')
    market_presence = extract_text(soup, 'span', 'component--field-formatter field-type-text_long')

    company_data = {
        'Company': 'Stripe',
        'Revenue': revenue,
        'Valuation': valuation,
        'Funding Rounds': funding_data,
        'Employee Count': employee_count,
        'Market Presence': market_presence
    }

    df = pd.DataFrame([company_data])
    df['Revenue'] = df['Revenue'].str.replace('$', '').astype(float)
    df['Valuation'] = df['Valuation'].str.replace('$', '').astype(float)
    df['Employee Count'] = df['Employee Count'].str.replace(',', '').astype(int)
    df['Funding Rounds'] = df['Funding Rounds'].apply(lambda x: [float(fund.replace('$', '').replace(',', '')) for fund in x])

    df.to_csv('company_data.csv', mode='a', header=False, index=False)
    print("Data scraped and updated")

# Schedule the script to run daily
schedule.every().day.at("00:00").do(scrape_data)

while True:
    schedule.run_pending()
    time.sleep(1)
