# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import pycountry


def downloaddb(url=None):
    if url is None:
        url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    data = pd.read_csv(url, parse_dates=['date'],
                       index_col=['iso_code', 'date'])
    return data


def country(dataframe, name='COL'):
    iso_code = pycountry.countries.lookup(name).alpha_3
    return dataframe.loc[iso_code]


if __name__ == '__main__':
    db = downloaddb()
    selected_country = country(db, 'COL')
    selected_country.total_cases.plot()
