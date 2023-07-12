from plot import*
from cleaner import*

# dirty image
show_image(h.astype(np.uint8), 'Dirty image')

# range of a
a_min = 0
a_max = 200
N = 21

for i in range(4):

    # N points of a
    a_array = np.linspace(a_min, a_max, N)
    # Shannon entropy
    ent_array = np.zeros(N)

    # save the entropy for every a-value
    for index, a in enumerate(a_array):
        clean_h, ent = cleaner(a)
        ent_array[index] = ent

    # find the minimum entropy and study his neighbourhood
    min = np.argmin(ent_array)
    a_min, a_max, N = new_a(min, a_array, N)

    # plot the entropy over a
    plot(a_array, ent_array, min, i)

# the clean image is the one with the a of minimum entropy
clean_h, ent = cleaner(a_array[min])
# clean image
show_image(clean_h.astype(np.uint8), f'Clean image --> a = {a_array[min]}')