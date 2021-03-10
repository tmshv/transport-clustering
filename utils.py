from skimage import io
import matplotlib.pyplot as plt
import numpy as np

def show_cluster(df, max_images=10):
    plt.figure(figsize=(25, 25))

    if df.shape[0] > max_images:
        df = df.sample(max_images)

    i = 0
    for index, row in df.iterrows():
        plt.subplot(10, 10, i+1)
        file = row['path']
        # img = load_img(file)
        img = io.imread(file)
        # img = np.array(img)
        plt.imshow(img)
        plt.axis('off')
        i += 1


def get_sample(data, n_items):
    idx = np.random.choice(data.shape[0], n_items, replace=False)
    data[idx, :], idx

