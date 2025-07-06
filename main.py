from scripts.load_data import cargar_datos_csv
from scripts.alerts import verificar_alerta
from scripts.plot import graficar_precipitacion

# Ruta del archivo
path = "data/P03-Rumihurco_Machángara_Precipitación-Mensual.csv"

# 1. Cargar y limpiar
df = cargar_datos_csv(path)

# 2. Obtener últimos 12 meses
df_last12 = df.sort_values('fecha', ascending=False).head(12).sort_values('fecha')

# 3. Mostrar alertas
alertas = verificar_alerta(df_last12)
if not alertas.empty:
    print("🚨 ALERTAS DE PRECIPITACIÓN BAJA:")
    print(alertas[['fecha', 'valor']])

# 4. Graficar
graficar_precipitacion(df_last12)
