# show images

import matplotlib.pyplot as plt

def show_img(disp_img):
    dpi = plt.rcParams['figure.dpi']
    fig_size = (disp_img.shape[0]/dpi, disp_img.shape[1]/dpi)
    fig, ax = plt.subplots(1, figsize=fig_size)

    ax.axis('off')
    ax.imshow(disp_img)
    plt.show()

def show_imgs(disp_imgs, in_line = None, names = None):
    if not in_line:
        in_line = len(disp_imgs)
    
    while len(disp_imgs) % in_line != 0:
        disp_imgs += [None]
        
    nrows = int(len(disp_imgs) / in_line)
    
    fig = plt.figure(figsize=(6.4 * in_line, 4.8 * nrows))
    
    for i in range(len(disp_imgs)):
        ax = fig.add_subplot(nrows, in_line, i+1)
        ax.axis('off')
        if disp_imgs[i] is not None:
            if names:
                ax.set_title(names[i])
            ax.imshow(disp_imgs[i])
    plt.show()