def verificar_alerta(df, umbral=10.0):
    alertas = df[df['valor'] < umbral]
    return alertas
