# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

data = pd.read_csv(url, parse_dates=['date'], index_col=['iso_code', 'date'])
data.sort_index(axis='index', level=[0, 1], inplace=True)
h_plot = data.loc['COL'].new_deaths.plot()

 