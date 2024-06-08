from dotenv import load_dotenv
from pprint import pprint 
import requests 
import os 

def get_analysis(country='AGO'): 
    debt_data = "Works "+country
    return debt_data

if __name__ == "__main__": 
    print('\n** Get the City for Debt Analysis**\n')

    country = input('\nPlease enter a country: ')

    debt_data = get_analysis(country)

    print("\n")

    pprint(debt_data)

