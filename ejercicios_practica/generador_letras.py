# Generador de letras
# Pedimos a un usuario que elija una canción de una lista de canciones.
# Cuando el usuario lo hace, imprime la letra de la canción que seleccionó.

songs = {
    
    "Justin Bieber" : ["Baby", "All That Matters", "Cold Water"],
    "Gustavo Cerati" : ["Adiós", "Crimen", "Te para 3"],
    "Drake" : ["In My Feeling", "One Dance", "0 To 100"]
    
}

def show_lyrics(song, artist):
    
    lyrics ={ 
            
        "Baby by Justin Bieber" : "Baby baby baby",
        "All That Matters by Justin Bieber" : "papa",
        "Cold Water by Justin Bieber" : "iop",
        
        "Adiós by Gustavo Cerati" : "hola",
        "Crimen by Gustavo Cerati" : "lol",
        "Te Para 3 by Gustavo Cerati" : "wdd",
        
        "In My Feeling by Drake" : "dof",
        "One Dance by Drake" : "dfs",
        "0 To 100 by Drake" : "dmfd"

    }
    
    song_artist = f"{song} by {artist}"
    if song_artist in lyrics:
        print(f"------- {song_artist} ------------")
        print(lyrics[song_artist])
        
def list_song_by_artist(artist):
        if artist in songs:
            print(f"Canciones de {artist}:")
            for song in songs[artist]:
                print(song)
        else:
            print(f"No se encontraron canciones de {artist}.")

def main():
    print("Bienvenido, por favor, seleccione una canción de los siguientes artistas:")
    while True:
        for i, artist in enumerate(songs.keys(), start=1):
            print(f"{i}. {artist}")

        selection = input("Ingresa el número del artista o * para salir: ")

        if selection == "*":
            break
        elif selection.isdigit():
            selection = int(selection)
            if 1 <= selection <= len(songs):
                artist = list(songs.keys())
                artist_selection = artist[selection - 1]
                list_song_by_artist(artist_selection)
                song = input(f"Elige una canción de {artist_selection}: ")
                if song in songs[artist_selection]:
                    show_lyrics(song, artist_selection)
                else:
                    print("Canción no válida.")
            else:
                print("Opción no válida.")
        else:
            print("Entrada no válida. Ingresa un número o * para salir.")

if __name__ == "__main__":
    main()