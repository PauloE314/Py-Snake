import pygame
from pygame.mixer import Sound
from typing import List, Dict


class AudioManager:
    """
    Gerenciador de áudios da aplicação
    """
    songs: Dict[str, Sound]

    def __init__(self, songs: Dict[str, str]):
        self.songs = {}

        # Cria os sons
        for song_name, song_path in songs.items():
            print(song_name, song_path)
            self.songs[song_name] = Sound(song_path)


    def play(self, name: str):
        """
        Toca o som com o nome passado como parâmetro
        """
        song = self.songs.get(name)

        if song:
            song.play()
        

    def stop(self):
        pygame.mixer.music.stop()

