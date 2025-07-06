import folium

def crear_mapa():
    # Vista general centrada entre ambas estaciones
    m = folium.Map(location=[-0.2810, -78.5190], zoom_start=15)

    # Estación actual (Rumihurco)
    folium.Marker(
        [-0.275, -78.525],
        popup="Estación Rumihurco",
        icon=folium.Icon(color='green', icon='cloud')
    ).add_to(m)

    # Estación propuesta El Troje (ajustada según mapa real)
    folium.Marker(
        [-0.28315, -78.51090],  # Coordenadas ajustadas cerca de Calle A y Av. Simón Bolívar
        popup="📍 Estación Propuesta El Troje",
        icon=folium.Icon(color='red', icon='tint')
    ).add_to(m)

    return m._repr_html_()
