import pandas as pd
import numpy as np
import re

def find_fuel(x):
    x = str(x)
    text = re.findall(r'petrol|diesel|electric|hybrid|cng|lpg',x)

    if text:
        return text[0]
    else:
        return "Not Found"

def find_body_type(x):
    x = str(x)
    text = re.findall(r'hatchback|sedan|suv|luxury sedan|luxury suv',x)

    if text:
        return text[0]
    else:
        return "Not Found"    

def clean():
    df = pd.read_csv('dump/results.csv',header=0,names=['CAR','Details','Price','URL'],error_bad_lines=False)
    df['Car_model'] = df['CAR'].apply(lambda x:x.split(' ')[2])
    df['BRAND'] = df['CAR'].apply(lambda x:x.split(' ')[1])
    df['Year_Manufacture'] = df['CAR'].apply(lambda x: re.findall(r'\d{4}',x)[0])
    df['Km_Driven'] =  df['Details'].apply(lambda x: re.findall(r'\d+',str(x))[0])
    df['Owners'] = df['Details'].apply(lambda x: re.findall(r'\d+',str(x))[1])
    df['Fuel'] = df['URL'].apply(lambda x : find_fuel(x))
    df['Body_Type'] = df['URL'].apply(lambda x : find_body_type(x))
    df_new=df[['BRAND','Car_model','Fuel','Body_Type','Year_Manufacture','Owners','Km_Driven','Price']]            
    df_new.to_csv('final_scraped/results.csv',index=False)
