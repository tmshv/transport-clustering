import pandas as pd
from pathlib import Path

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

df.to_csv('transport_dataset.csv', index=False)
