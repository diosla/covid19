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


def country(database_complete, name='COL'):
    iso_code = pycountry.countries.lookup(name).alpha_3
    return database_complete.loc[iso_code]


def plot(database, *args, **kwargs):
    if len(args) == 1:
        plot_handler = database.loc[:, args[0]].plot(**kwargs)
    elif len(args) == 2:
        plot_handler = database.plot(x=args[0], y=args[1], **kwargs)
    else:
        error_message = (
            f'plot() takes either 1 or 2 arguments after'
            f' the database ({len(args)} given)'
        )
        raise TypeError(error_message)
    return plot_handler


if __name__ == '__main__':
    db = downloaddb()
    selected_country = country(db, 'COL')
    plot(selected_country, 'total_cases')
