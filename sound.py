import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'Gun.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'Npc Hit.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'Npc Death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'Npc Gun.wav')
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + 'Got Hit.wav')
        self.theme = pg.mixer.music.load(self.path + 'theam.mp3')
        pg.mixer.music.set_volume(0.4)