import numpy as np

h = np.load('img_modificata.npy')
H = np.fft.fft2(h)