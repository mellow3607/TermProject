from pico2d import *



def handle_events():
    global running
    global dir
    global dir_y
    global right
    global left
    global up
    global bg_dir
    global jump
    global y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_RIGHT:
                right = True
                bg_dir -= 1
                dir += 1
            elif event.key == SDLK_LEFT:
                right = False
                bg_dir += 1
                dir -= 1
            elif event.key == SDLK_SPACE:
                up = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                    dir -= 1
                    bg_dir += 1
            elif event.key == SDLK_LEFT:
                    dir += 1
                    bg_dir -= 1



    pass

open_canvas()

black = load_image('black.jpg')
bg = load_image('forest.jpg')
ground = load_image('ground1.png')
character = load_image('character_sheet.png')
coin = load_image('coin.png')
ground2 = load_image('ground2.png')

running = True
x = 800 // 2
y = 0
bg_x,bg_y = 400,300
bg_dir = 0
frame = 1
frame_coin = 0
dir = 0
dir_y = 0
right = True
left = False
up = False
jump = 5

while running :
    clear_canvas()
    # black.draw(400,300)
    bg.draw(bg_x,bg_y)
    ground.clip_draw(50,0,2000,200,400,50)
    # character.clip_draw(0,100,100,100,x,160+y)
    # character.clip_draw(frame * 100,0,100,100,x,160+y)
    coin.clip_draw(frame_coin*100,0,100,50,540,450)
    coin.clip_draw(frame_coin*100,0,100,50,450,450)
    ground2.draw(200,200)
    ground2.draw(600,200)
    ground2.draw(300,300)
    ground2.draw(500,400)

    if right == True:
        character.clip_draw(frame * 100, 0, 100, 100, x, 160 + y)
        x += dir * 5
        bg_x += bg_dir
    if right == False:
        character.clip_draw(frame * 100, 0, 100, 100, x, 160 + y)
        bg_x += bg_dir
        x += dir * 5
    if up == True:
        y += 20 - jump
        jump += 2
        character.clip_draw(frame*100,200,100,100,x,160+y)
        if y < 95:
            y = 95
            up = False
            jump = 0


    update_canvas()
    # x += dir * 5

    handle_events()



    frame = (frame + 1)%8
    frame_coin = (frame_coin+1)%12

    delay(0.01)

close_canvas()
