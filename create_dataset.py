import pandas as pd
from pathlib import Path
import imquality.brisque as brisque
import PIL.Image
from tqdm import tqdm

# ignore warnings from skimage
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv('images_paths.csv')
df.columns = ['path']

# df = df.sample(100)

def fix_path(row):
    f = row['path'].replace('\\', '/')
    return f'raw_data/veriwild/{f}'
df['path'] = df.apply(fix_path, axis=1)

def get_car_id(row):
    f = Path(row['path'])
    return f.parent.name
df['car_id'] = df.apply(get_car_id, axis=1)

total = df.shape[0]
for row_id, row, in tqdm(df.iterrows(), total=total):
    path = row['path']
    img = PIL.Image.open(path)
    q = brisque.score(img)
    w, h = img.size
    df.loc[row_id, 'width'] = w
    df.loc[row_id, 'height'] = h
    df.loc[row_id, 'brisque'] = q

print(df)
df.to_csv('transport_dataset.csv', index=False)
