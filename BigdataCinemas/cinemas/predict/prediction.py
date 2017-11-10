from __future__ import unicode_literals
import os.path
#import pandas as pd
import pickle
import os
import sys
import pandas as pd




if __name__ == '__main__':
    if len(sys.argv) != 2: exit()

    name_path = sys.argv[1]
    if not os.path.isfile(name_path): exit()

    model = pickle.load(open('data/model.pcl',"rb"))
    df = pickle.load(open('data/df.pcl',"rb"))

    ids = pd.read_csv(name_path)
    temp_df = df[df.index.isin(ids.iloc[:,0])]

    prediction1 = model.predict(df[df.index.isin(ids.iloc[:,0])])
    #prediction = {i:v for i,v in zip(temp_df.index.values, prediction1)}

    temp_df['prediction'] = prediction1

    print(temp_df.loc[:,'prediction'].reset_index)
