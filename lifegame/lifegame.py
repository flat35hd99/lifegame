from code import interact
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime

class LifeGame():
    def __init__(self, initial_state, observer=None):        
        self.state = initial_state
        self.Nx, self.Ny = initial_state.shape
        self.observer = observer
    
    def update(self):
        present_state = self.state.copy()
        for ix in range(-1, self.Nx - 1):
            for iy in range(-1, self.Ny - 1):
                _count = (
                    present_state[ix-1, iy-1]
                    + present_state[ix, iy-1]
                    + present_state[ix+1, iy-1]
                    
                    + present_state[ix-1, iy]
                    + present_state[ix+1, iy]
                    
                    + present_state[ix-1, iy+1]
                    + present_state[ix, iy+1]
                    + present_state[ix+1, iy+1]
                )
                
                if _count in [0,1] or _count >= 4:
                    self.state[ix, iy] = 0
                elif _count == 3:
                    self.state[ix, iy] = 1
                # else _count == 2, then leave present value
    
    def run(self, steps=1000):
        for _ in range(steps):
            self.update()
            self.observe()
    
    def observe(self):
        self.observer.observe(state=self.state)
    
    def output_result(self, filename):
        self.observer.output(filename=filename)
            
            
# class AbstractObserver():
#     """Abstract observer
#     Initialize once
#     Recieve numpy ndarray and Do something for (each) step(s)
#     Output result(s) by output()
#     """
#     def __init__(self) -> None:
#         pass

#     def observe(self, state: np.ndarray) -> None:
#         pass
    
#     def output(self, filename) -> None:
#         pass

class AnimationObserver():
    def __init__(self):
        # super().__init__()
        self.fig = plt.figure()
        self.images = []
    
    def observe(self, state: np.ndarray):
        image = plt.imshow(state, cmap='gray', vmin=0, vmax=1)
        self.images.append([image])
    
    def output(self, filename):
        _anime = anime.ArtistAnimation(self.fig, self.images, interval=100)
        _anime.save(filename)