import numpy as np
from lifegame.lifegame import LifeGame, AnimationObserver

def create_locomotive(state, start_x, start_y):
    # Tテトロミノによる機関車
    state[start_x+5, start_y] = 1
    state[start_x+6, start_y] = 1
    state[start_x+7, start_y] = 1
    state[start_x+8, start_y] = 1
    state[start_x+4, start_y+1] = 1
    state[start_x+8, start_y+1] = 1
    state[start_x+8, start_y+2] = 1
    state[start_x+0, start_y+3] = 1
    state[start_x+1, start_y+3] = 1
    state[start_x+4, start_y+3] = 1
    state[start_x+7, start_y+3] = 1
    state[start_x+0, start_y+4] = 1
    state[start_x+1, start_y+4] = 1
    state[start_x+2, start_y+4] = 1
    state[start_x+0, start_y+5] = 1
    state[start_x+1, start_y+5] = 1
    state[start_x+4, start_y+5] = 1
    state[start_x+7, start_y+5] = 1
    state[start_x+8, start_y+6] = 1
    state[start_x+4, start_y+7] = 1
    state[start_x+8, start_y+7] = 1
    state[start_x+5, start_y+8] = 1
    state[start_x+6, start_y+8] = 1
    state[start_x+7, start_y+8] = 1
    state[start_x+8, start_y+8] = 1
    return state

def main():
    N = 100
    center = N//2
    state = np.zeros((N,N))
    # Separated
    state = create_locomotive(state=state, start_x=center, start_y=center)
    state = create_locomotive(state=state, start_x=center-30, start_y=center)
    # Disappered
    state = create_locomotive(state=state, start_x=center, start_y=center + 20)
    state = create_locomotive(state=state, start_x=center-20, start_y=center + 20)
    # Leave cloud
    state = create_locomotive(state=state, start_x=center, start_y=center - 20)
    state = create_locomotive(state=state, start_x=center-15, start_y=center - 20)

    game = LifeGame(initial_state=state, observer=AnimationObserver())
    game.run(steps=100)
    game.output_result("hogehoge.gif")

if __name__ == '__main__':
    main()
    