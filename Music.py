from pygame import mixer


def init():
    mixer.init()


def paddle_hit():
    if not mixer.music.get_busy():
        mixer.music.load('paddle_hit.wav')
        mixer.music.play()


def wall_hit():
    if not mixer.music.get_busy():
        mixer.music.load('wall_hit.wav')
        mixer.music.play()


def score():
    if not mixer.music.get_busy():
        mixer.music.load('score.wav')
        mixer.music.play()
