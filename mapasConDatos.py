"""crear un mapa con datos de natalidad migracion y otro con datos de poblacion de  cada pais.  
y una funcion que me calcule la poblacion total de un pais. 
y una funcion que me calcule la poblacion total de un continente.   """  


import folium
import pandas as pd
#import geopandas as gpd
df = pd.read_csv("Poblacion_y_natalidad.csv")

mapa = folium.Map(location=[df["Latitud"].mean(), df["Longitud"].mean()], zoom_start=3)

for i in range(0, df.shape[0]):
    folium.Marker(
        location=[df.iloc[i]["Latitud"], df.iloc[i]["Longitud"]],
        popup=df.iloc[i]["Poblacion"]
    ).add_to(mapa)

mapa.save("mapa.html")