class GameState:
    def __init__(self,state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw


running = None
stack = None

def run(title_state):
    global running, stack
    running = True

    stack = [title_state]
    title_state.enter()

    while(running):
        stack[-1].handle_events()
        #stack[-1].update()
        stack[-1].draw()

    while(len(stack)>0):
        stack[-1].exit()
        stack.pop()

# 현재상태 삭제 후 새로운 상태추가, enter로 들어감
def change_state(state):
    global stack
    if(len(stack)>0):
        stack[-1].exit()
        stack.pop()
    stack.append(state)
    state.enter()

def pop_state():
    global stack
    if (len(stack) > 0):
        stack[-1].exit()
        stack.pop()
    if(len(stack)>0):
        stack[-1].resume()


# 현재상태 저장(pause) 후 새로운 상태
def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()

def quit():
    global running
    running = False