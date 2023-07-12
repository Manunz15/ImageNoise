from load_image import*

def create_noise(a):
    shape = list(h.shape)
    noise = np.zeros(shape)

    # set the seed
    np.random.seed(1642147)
    
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                # Box-Muller numbers
                u = -np.log(1 - np.random.uniform(0,1))
                theta = np.random.uniform(0,a)

                noise[i][j][k] = 0.5*np.sqrt(2*u)*(np.cos(theta)+np.sin(theta))

    # normalization of the noise
    noise /= np.amax(noise)

    return noise