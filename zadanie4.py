#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

d = {'name': ['Gabriela', 'Jakub', 'Julia', 'Dominika', 'Tomasz'],
     'surname': ['Bocheńska', 'Kowalski', 'Nowak', 'Wiśniewska', 'Kowalczyk'],
     'age': [21, 20, 19, 18, 17], 'sex': ['female', 'male', 'female', 'female', 'male']}
df = pd.DataFrame(data=d)

print(df)
print(df.info())
print(df.describe())
print(df.head(3))
