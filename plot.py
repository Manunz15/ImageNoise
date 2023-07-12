import matplotlib.pyplot as plt

def show_image(h, title):
    plt.imshow(h)
    plt.title(title)
    plt.axis('off')
    plt.show()

def plot(a_array, ent_array, min, i):

    plt.scatter(a_array[min], ent_array[min], c = 'red', label = 'a = {:.2f}'.format(a_array[min]))
    plt.plot(a_array, ent_array, zorder = 0)    
    
    plt.title(f'Round {i+1}')
    plt.xlabel('a-value')
    plt.ylabel('Shannon entropy')
    plt.legend()
    plt.show()