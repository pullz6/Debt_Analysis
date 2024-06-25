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
    indicators = {"DT.DOD.DLXF.CD": "External_Debts",
              "DT.DOD.DIMF.CD":"IMF_Credit",
              "DT.DOD.DSTC.CD":"Short_term_debt",
              "BM.GSR.TOTL.CD": "Income",
              "FI.RES.TOTL.CD":"Total_Reserves",
              "NY.GNP.MKTP.CD":"Gross_income",
              "BX.GSR.TOTL.CD":"Exports",
              "NE.IMP.GNFS.CD":"Imports",
              "NE.DAB.TOTL.CN":"National_Expenditure",
              "BN.GSR.FCTY.CD":"Primary_Income",
              "BN.KLT.DINV.CD":"Foreign_Investment",
              "BX.GRT.EXTA.CD.WD":"Grants",
              "BX.GSR.GNFS.CD":"Exports",
              "DT.NFL.SDGF.CD":"SDGFUND",
              "DT.NFL.SPRP.CD":"SPRP",
              "DT.NFL.UNAI.CD":"UNAIDS",
              "DT.NFL.UNCD.CD":"UNCDF",
              "DT.NFL.UNCF.CD":"UNICEF",
              "DT.NFL.UNCR.CD":"UNHCR",
              "DT.NFL.UNCTAD.CD":"UNCTAD",
              "DT.NFL.UNCV.CD":"UNCOVID",
              "DT.NFL.UNDP.CD":"UNDP",
              "DT.NFL.UNEC.CD":"UNECE",
              "DT.NFL.UNEP.CD":"UNEP",
              "DT.NFL.UNFP.CD":"UNFPA",
              "DT.NFL.UNID.CD":"UNIDIR",
              "DT.NFL.UNIDO.CD":"UNIDO",
              "DT.NFL.UNPB.CD":"UNPBF",
              "DT.NFL.UNRW.CD":"UNRWA",
              "DT.NFL.UNTA.CD":"UNTA",
              "DT.NFL.UNWN.CD":"UNWOMEN",
              "DT.NFL.UNWT.CD":"UNWTO",
              "DT.NFL.WFPG.CD":"WFP",
              "DT.NFL.WHOL.CD":"WHO",
              "DT.NFL.WITC.CD":"WTO-ITC",
              "BM.GSR.MRCH.CD":"Goods_imports",
              "BM.GSR.NFSV.CD":"Service_imports",
              "BX.GSR.MRCH.CD":"Goods_exports",
              "BX.GSR.NFSV.CD":"Service_exports",
              "TM.VAL.AGRI.ZS.UN":"Agri_raw_materials_imports",
              "TM.VAL.FOOD.ZS.UN":"Food_imports",
              "TM.VAL.FUEL.ZS.UN":"Fuel_imports",
              "TM.VAL.MANF.ZS.UN":"Manufacturing_imports",
              "TM.VAL.MMTL.ZS.UN":"Ores_metal_imports",
              "TX.VAL.AGRI.ZS.UN":"Agri_raw_materials_exports",
              "TX.VAL.FOOD.ZS.UN":"Food_exports",
              "TX.VAL.FUEL.ZS.UN":"Fuel_exports",
              "TX.VAL.MANF.ZS.UN":"Manufacturing_exports",
              "TX.VAL.MMTL.ZS.UN":"Ores_metal_exports",
              "MS.MIL.XPND.CD":"Military_expenditure",
              "NY.ADJ.AEDU.CD":"Education_expenditure",
              "ST.INT.XPND.CD":"Tourism_expenditure",
              "SH.XPD.CHEX.PC.CD":"Health_expenditure",
              "SH.XPD.OOPC.PC.CD":"Out_of_pocket_expenditure",
              "SH.XPD.PVTD.PC.CD":"Private_expenditure_health",
              "NE.CON.PRVT.CD":"Household_expenditure"
             }
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

    #Funds 
    df['SDGFUND'] = df['SDGFUND'].apply(formatNum)
    df['SPRP'] = df['SPRP'].apply(formatNum)
    df['UNAIDS'] = df['UNAIDS'].apply(formatNum)
    df['UNCDF'] = df['UNCDF'].apply(formatNum)
    df['UNICEF'] = df['UNICEF'].apply(formatNum)
    df['UNHCR'] = df['UNHCR'].apply(formatNum)
    df['UNCTAD'] = df['UNCTAD'].apply(formatNum)
    df['UNCOVID'] = df['UNCOVID'].apply(formatNum)
    df['UNDP'] = df['UNDP'].apply(formatNum)
    df['UNECE'] = df['UNECE'].apply(formatNum)
    df['UNEP'] = df['UNEP'].apply(formatNum)
    df['UNFPA'] = df['UNFPA'].apply(formatNum)
    df['UNIDIR'] = df['UNIDIR'].apply(formatNum)
    df['UNRWA'] = df['UNRWA'].apply(formatNum)
    df['UNTA'] = df['UNTA'].apply(formatNum)
    df['UNWOMEN'] = df['UNWOMEN'].apply(formatNum)
    df['UNWTO'] = df['UNWTO'].apply(formatNum)
    df['WFP'] = df['WFP'].apply(formatNum)
    df['WHO'] = df['WHO'].apply(formatNum)
    df['WTO-ITC'] = df['WTO-ITC'].apply(formatNum)
    df['Military_expenditure'] = df['Military_expenditure'].apply(formatNum)
    df['Education_expenditure'] = df['Education_expenditure'].apply(formatNum)
    df['Tourism_expenditure'] = df['Tourism_expenditure'].apply(formatNum)
    df['Health_expenditure'] = df['Health_expenditure'].apply(formatNum)
    df['Private_expenditure_health'] = df['Private_expenditure_health'].apply(formatNum)
    df['Household_expenditure'] = df['Household_expenditure'].apply(formatNum)
    df['Out_of_pocket_expenditure'] = df['Out_of_pocket_expenditure'].apply(formatNum)

    df['UN_FUNDS'] = df['SDGFUND']+df['SPRP']+df['UNAIDS']+df['UNCDF']+df['UNICEF']+df['UNHCR']+df['UNCTAD']+df['UNCOVID']+df['UNDP']+df['UNECE']+df['UNEP']+df['UNFPA']+df['UNIDIR']+df['UNRWA']+df['UNTA']+df['UNWOMEN']+df['UNWTO']+df['WFP']+df['WHO']+df['WTO-ITC']
    
    print(df.head())
    
    # Use render_template to pass graphJSON to html
    return df

if __name__ == "__main__": 
    print('\n** Get the City for Debt Analysis**\n')

    country = input('\nPlease enter a country: ')

    debt_data = get_analysis(country)

    print("\n")

    pprint(debt_data)

