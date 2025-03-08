## Paso 3: Variables de entorno

import os
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales desde las variables de entorno
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

## Paso 4: Inicializar la biblioteca Spotipy

# Inicializar Spotipy con autenticación de cliente
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

## Paso 5: Realizar solicitudes a la API

# ID del artista (Bad Bunny)
artist_id = "4q3ewBCX7sLwd24euuV69X"

# Obtener el top 10 de canciones más populares del artista
top_tracks = sp.artist_top_tracks(artist_id)

#Ver el objeto JSON
print(top_tracks)

# Extraer nombre, popularidad y duración (convertida a minutos)
tracks_data = []
for track in top_tracks['tracks'][:10]:  # Top 10 canciones
    name = track['name']
    popularity = track['popularity']
    duration_min = track['duration_ms'] / (1000 * 60)  # Convertir de milisegundos a minutos
    tracks_data.append([name, popularity, round(duration_min, 2)])

#Ver la lista
print(tracks_data)

## Paso 6: Transformar a Pandas DataFrame

# Convertir a DataFrame
tracks_df = pd.DataFrame(tracks_data, columns=['name', 'popularity', 'duration_min'])

# Ordenar por popularidad descendente
df_sorted = tracks_df.sort_values(by='popularity', ascending=False)

# Mostrar el top 3 de canciones más populares
print(df_sorted.head(3))

## Paso 7: Analizar relación estadística

import matplotlib.pyplot as plt

# Crear el scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(tracks_df['duration_min'], tracks_df['popularity'], alpha=0.7)
plt.xlabel('Duración (minutos)')
plt.ylabel('Popularidad')
plt.title('Relación entre Duración y Popularidad de Canciones')
plt.grid(True)
plt.show()

interpretacion = [
    "No parece haber una relación directa entre la duración y la popularidad. Las canciones más populares tienen duraciones variadas, sin una tendencia clara de que las canciones más cortas o más largas sean más populares.",
    "Esto sugiere que la popularidad de una canción puede depender más de factores como la promoción, el artista, la viralidad en redes sociales o la calidad percibida, en lugar de su duración."
]

print(interpretacion)