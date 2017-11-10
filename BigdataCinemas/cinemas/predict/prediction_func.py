from __future__ import unicode_literals
import os.path
#import pandas as pd
import pickle
import os
import sys
import pandas as pd
from django.conf import settings




def cinemas_predict(name_path):
    PATH = os.path.join(settings.BASE_DIR, 'data')

    if not os.path.isfile(name_path): return (1, None)

    model = pickle.load(open(os.path.join(PATH,'model.pcl'),"rb"))
    df = pickle.load(open(os.path.join(PATH,'df.pcl'),"rb"))

    ids = pd.read_csv(name_path, encoding="windows-1251")
    temp_df = df[df.index.isin(ids.iloc[:,0])]

    prediction1 = model.predict(df[df.index.isin(ids.iloc[:,0])])
    #prediction = {i:v for i,v in zip(temp_df.index.values, prediction1)}

    temp_df['prediction'] = prediction1

    return(0, temp_df.loc[:,'prediction'])
