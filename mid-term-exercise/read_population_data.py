import pandas as pd
import numpy as np
import pylab as plt
from IPython import embed

df = pd.read_csv('person_info.csv')

age_groups = np.unique(df['age'])
sexes = np.unique(df['sex'])
print('No. groups: ', len(age_groups))
        
D = df.groupby(['sex','year']).sum()
both = D.loc['0 Both sexes']
pop = df.columns[4]

for group in sexes:
    D.loc[group, ' (%)'] = D.loc[group,pop].values/both[pop].values

    

F = df.groupby(['age','year']).sum()
for group in age_groups:
    F.loc[group, ' (%)'] = F.loc[group,pop].values/both[pop].values

plt.plot(F.loc[age_groups[0], ' (%)'])
plt.title(age_groups[0] + ' as a percentage of the population')
plt.show()

