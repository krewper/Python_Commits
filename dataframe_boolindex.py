#importing pandas as pd

import pandas as pd

#dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
        'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
        'score':[400, 390, 690, 1290]}

df = pd.DataFrame(dict, index = [False, True, False, True])

print(df.loc[True])