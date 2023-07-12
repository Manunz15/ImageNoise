from scipy_entropy import*
from noise import*

def cleaner(a):
    # create noise
    noise = create_noise(a)
    H_noise = np.fft.fft2(noise)
    
    # use fourier to clean the image
    clean_h = abs(np.fft.ifft2(H/H_noise))
    
    # Shannon entropy of the image
    ent = np.mean(entropy(clean_h.astype(np.uint8), base = 256))

    return clean_h, ent

def new_a(min, a_array, N):

    # number of points
    new_N = 21

    # new extremes
    if min == 0:
        a_min = a_array[min]
        new_N = 11
    else:
        a_min = a_array[min-1]
        
    if min == N - 1:
        a_max = a_array[min]
        new_N = 11
    else:
        a_max = a_array[min+1]

    return a_min, a_max, new_N