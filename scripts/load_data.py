import pandas as pd

def cargar_datos_csv(path):
    df = pd.read_csv(path)
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y/%m')
    df = df.dropna(subset=['valor'])
    return df
