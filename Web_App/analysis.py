from dotenv import load_dotenv
from pprint import pprint 
import datetime
import wbdata
import numpy as np
import pandas as pd
import requests 
import os 


def formatNum(x):
    """Creating a function that will change units to billions and round to 0 decimal places"""
    y = x/1000000000
    z = round(y)
    return(z)

def get_analysis(country='AGO'): 
    countries = []
    countries.append(country)
    print(countries)
    indicators = {"DT.DOD.DLXF.CD": "External_Debts","DT.DOD.DIMF.CD":"IMF_Credit","DT.DOD.DSTC.CD":"Short_term_debt","BM.GSR.TOTL.CD": "Income","FI.RES.TOTL.CD":"Total_Reserves","NY.GNP.MKTP.CD":"Gross_income","BX.GSR.TOTL.CD":"Exports","NE.IMP.GNFS.CD":"Imports","NE.DAB.TOTL.CN":"National_Expenditure","BN.GSR.FCTY.CD":"Primary_Income","BN.KLT.DINV.CD":"Foreign_Investment","BX.GRT.EXTA.CD.WD":"Grants","BX.GSR.GNFS.CD":"Exports","DT.NFL.SDGF.CD":"SDGFUND","DT.NFL.SPRP.CD":"SPRP","DT.NFL.UNAI.CD":"UNAIDS","DT.NFL.UNCD.CD":"UNCDF","DT.NFL.UNCF.CD":"UNICEF","DT.NFL.UNCR.CD":"UNHCR","DT.NFL.UNCTAD.CD":"UNCTAD","DT.NFL.UNCV.CD":"UNCOVID","DT.NFL.UNDP.CD":"UNDP","DT.NFL.UNEC.CD":"UNECE","DT.NFL.UNEP.CD":"UNEP","DT.NFL.UNFP.CD":"UNFPA","DT.NFL.UNID.CD":"UNIDIR","DT.NFL.UNIDO.CD":"UNIDO","DT.NFL.UNPB.CD":"UNPBF","DT.NFL.UNRW.CD":"UNRWA","DT.NFL.UNTA.CD":"UNTA","DT.NFL.UNWN.CD":"UNWOMEN","DT.NFL.UNWT.CD":"UNWTO","DT.NFL.WFPG.CD":"WFP","DT.NFL.WHOL.CD":"WHO","DT.NFL.WITC.CD":"WTO-ITC"}
    df = wbdata.get_dataframe(indicators, country=countries, parse_dates=True, keep_levels =True)
    df = pd.DataFrame(df.to_records())

    df = df.replace(np.nan, 0)
    df['Income'] = df['Income'].apply(formatNum)
    df['External_Debts'] = df['External_Debts'].apply(formatNum)
    df['Total_Reserves'] = df['Total_Reserves'].apply(formatNum)
    df['IMF_Credit'] = df['IMF_Credit'].apply(formatNum)
    df['Short_term_debt'] = df['Short_term_debt'].apply(formatNum)
    df['Gross_income'] = df['Gross_income'].apply(formatNum)
    df['Exports'] = df['Exports'].apply(formatNum)
    df['Imports'] = df['Imports'].apply(formatNum)
    df['National_Expenditure'] = df['National_Expenditure'].apply(formatNum)
    df['Primary_Income'] = df['Primary_Income'].apply(formatNum)
    df['Foreign_Investment'] = df['Foreign_Investment'].apply(formatNum)
    df['Grants'] = df['Grants'].apply(formatNum)
    print(df.head())
    
    # Use render_template to pass graphJSON to html
    return df

if __name__ == "__main__": 
    print('\n** Get the City for Debt Analysis**\n')

    country = input('\nPlease enter a country: ')

    debt_data = get_analysis(country)

    print("\n")

    pprint(debt_data)

