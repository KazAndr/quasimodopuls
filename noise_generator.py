import numpy as np

class Noiser(object):
    def __init__(self, median, amplitude, t_resolution, n_chanels, win_size):
        self.median = median
        self.amplitude = amplitude
        self.t_resolution = t_resolution
        self.n_chanels = n_chanels
        self.win_size = win_size
        
    def gener_noise(self):
        self.noise = []
        for _ in range(self.n_chanels): 
            self.noise.append(np.random.normal(self.median, self.amplitude, self.win_size))
    
    def get_noise(self):
        return self.noise