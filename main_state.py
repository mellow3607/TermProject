import random
import json
import os

from pico2d import *

import game_framework
import title_state

from mario import Mario

name = "MainState"

mario = None

def enter():
    global mario
    mario = Mario()

def exit():
    global mario
    del mario

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            mario.handle_event(event)

def update():
    mario.update()

def draw():
    clear_canvas()
    mario.draw()
    update_canvas()



