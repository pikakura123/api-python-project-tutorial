import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()

from dotenv import load_dotenv
load_dotenv()

import os

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

print("Client ID:", client_id)
print("Client Secret:", client_secret)

if not client_id or not client_secret:
    raise ValueError("CLIENT_ID y CLIENT_SECRET deben estar establecidos en el archivo .env")

# Paso 3: Configurar la autenticación de Spotipy
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
print("Conexión con la API de Spotify establecida correctamente.")

try:
    # Paso 4: Realizar solicitudes a la API para obtener las canciones top de Mozart
    artist_id = '4NJhFmfw43RLBLjQvxDuRS'

    # Obtener el top 10 de canciones del artista
    top_tracks = sp.artist_top_tracks(artist_id, country='US')['tracks'][:10]

    # Extraer el nombre, popularidad y duración de las canciones
    track_info = []
    for track in top_tracks:
        track_info.append({
            'name': track['name'],
            'popularity': track['popularity'],
            'duration': track['duration_ms'] / 60000  # Convertir ms a minutos
        })

    # Imprimir la información de las canciones
    for info in track_info:
        print(f"Track: {info['name']}, Popularity: {info['popularity']}, Duration: {info['duration']:.2f} minutes")

    # Paso 5: Transformar a Pandas DataFrame
   
    df = pd.DataFrame(track_info)
    df_sorted = df.sort_values(by='popularity')

    # Mostrar el top 3 resultante
    print(df_sorted.head(3))

    # Paso 6: Analizar relación estadística
   
    sns.scatterplot(x='duration', y='popularity', data=df_sorted)
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Popularity')
    plt.title('Relationship between Duration and Popularity')
    plt.show()

finally:

    del sp
    del auth_manager