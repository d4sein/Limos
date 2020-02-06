# Source: http://www.nepa.unicamp.br/taco/home.php

import os

import pandas as pd
from sqlalchemy import create_engine

# Configuring ORM
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(BASE_DIR, 'data.db'))


# Defining labels for columns
cols = ['Número do Alimento (qnt)', 'Descrição', 'Umidade (%)', 'Energia (kcal)', 'Energia (kJ)', 'Proteína (g)',
        'Lipídeos (g)', 'Colesterol (mg)', 'Carboidrato (g)', 'Fibra Alimentar (g)', 'Cinzas (g)', 'Cálcio (mg)',
        'Magnésio (mg)', 'Número do Alimento (id)', 'Manganés (mg)', 'Fósforo (mg)', 'Ferro (mg)', 'Sódio (mg)',
        'Potássio (mg)', 'Cobre (mg)', 'Zinco (mg)', 'Retinol (mcg)', 'RE (mcg)', 'RAE (mcg)',
        'Tiamina (mg)', 'Riboflavina (mg)', 'Piridoxina (mg)', 'Niacina (mg)', 'Vitamina C (mg)']


csv_files = os.listdir('data')
frames = list()

for csv_file in csv_files:
    # Creating DataFrame
    df = pd.read_csv('data/' + csv_file)
    df.columns = cols

    # Drops useless columns
    to_drop_cols = ['Número do Alimento (qnt)', 'Número do Alimento (id)',
                    'Cinzas (g)', 'RE (mcg)', 'RAE (mcg)']

    df.drop(to_drop_cols, axis=1, inplace=True)

    # Refining data for ease of use.
    df.fillna(0, inplace=True)
    df.replace(['Tr', '*', ' '], 0, inplace=True)

    # Assigns new column with csv file name identifier
    # (might be useful in the future for categorizing)
    df = df.assign(Categoria=csv_file.replace('.csv', ''))
    frames.append(df)

table_name = 'food'

food_df = pd.concat(frames, ignore_index=True)
food_df.to_sql(table_name, con=engine, if_exists='append')