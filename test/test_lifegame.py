from lifegame.lifegame import LifeGame, AnimationObserver
import numpy as np
from numpy import testing as np_test

def test_initialize():
    game = LifeGame(initial_state=np.zeros((10,10)))
    assert game.Nx == 10
    assert game.Ny == 10
    
    game = LifeGame(initial_state=np.zeros((20,10)))
    assert game.Nx == 20
    assert game.Ny == 10

def test_update_isolated_individual_will_die():
    zeros = np.zeros((3,3))
    isolated = zeros.copy()
    isolated[1,1] = 1
    game = LifeGame(initial_state=isolated)
    game.update()
    
    np_test.assert_array_equal(zeros, game.state)

def test_update_survive():
    zeros = np.zeros((3,3))
    # Keey alive
    # * * _
    # * * _
    # _ _ _
    two_surrounding = zeros.copy()
    two_surrounding[0,1] = 1
    two_surrounding[0,2] = 1
    two_surrounding[1,1] = 1
    two_surrounding[1,2] = 1
    game = LifeGame(initial_state=two_surrounding.copy())
    game.update()
    
    np_test.assert_array_equal(two_surrounding, game.state)

def test_update_born():
    zeros = np.zeros((4,4))
    # Born new one at (1,1)
    #
    # step i state
    # _ _ _ _
    # _ * * _
    # _ * _ _
    # _ _ _ _
    # 
    # step i + 1 state
    # _ _ _ _
    # _ * * _
    # _ * * _
    # _ _ _ _
    born_new_one = zeros.copy()
    born_new_one[1,1] = 1
    born_new_one[1,2] = 1
    born_new_one[2,1] = 1
    
    game = LifeGame(initial_state=born_new_one.copy())
    game.update()
    
    expected = born_new_one.copy()
    expected[2,2] = 1
    
    np_test.assert_array_equal(expected, game.state)

def test_update_die_by_overcrowding():
    zeros = np.zeros((3,3))
    will_die = zeros.copy()
    will_die[0,0] = 1
    will_die[0,1] = 1
    will_die[0,2] = 1
    will_die[1,0] = 1
    will_die[1,1] = 1
    
    game = LifeGame(initial_state=will_die.copy())
    game.update()
    
    expected = zeros.copy()
    
    np_test.assert_array_equal(expected, game.state)

def test_run():
    N = 100
    state = np.zeros((N,N))
    state[N // 2, N // 2] = 1
    state[N // 2 - 1, N // 2] = 1
    state[N // 2 + 1, N // 2] = 1
    state[N // 2, N // 2 - 1] = 1
    state[N // 2 - 1, N // 2 + 1] = 1
    
    game = LifeGame(initial_state=state, observer=AnimationObserver())
    game.run()
    game.output_result("hogehoge.gif")