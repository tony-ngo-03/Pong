from pygame import mixer

def init():
    mixer.init()

def paddle_hit():
    mixer.music.load('paddle_hit.wav')
    mixer.music.play()

def wall_hit():
    mixer.music.load('wall_hit.wav')
    mixer.music.play()

def score():
    mixer.music.load('score.wav')
    mixer.music.play()

