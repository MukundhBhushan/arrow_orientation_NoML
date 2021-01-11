import numpy as np
from scipy import ndimage
import pandas as pd
import matplotlib.pylab as plt

#left
leftarr = np.array([[[154., 182.]],

       [[148., 225.]],

       [[244., 184.]],

       [[154., 168.]],

       [[116., 217.]],

       [[244., 202.]],

       [[120., 174.]],

       [[128., 167.]],

       [[153., 207.]],

       [[100., 191.]],

       [[212., 183.]],

       [[104., 210.]],

       [[111., 188.]],

       [[224., 181.]],

       [[133., 225.]],

       [[213., 205.]],

       [[233., 204.]],

       [[181., 186.]],

       [[168., 186.]],

       [[191., 183.]]])


uparr = np.array([[[260.,  71.]],

       [[238.,  66.]],

       [[256., 160.]],

       [[239., 160.]],

       [[250., 146.]],

       [[256., 137.]],

       [[239.,  96.]],

       [[262.,  38.]],

       [[219.,  66.]],

       [[252.,  25.]],

       [[238., 150.]],

       [[280.,  51.]],

       [[235.,  25.]],

       [[279.,  70.]],

       [[257., 127.]],

       [[237., 123.]],

       [[258., 100.]],

       [[259.,  81.]],

       [[239.,  77.]],

       [[218.,  50.]],

       [[228.,  35.]]])


rightarr = np.array([[[164., 125.]],

       [[158., 150.]],

       [[207., 128.]],

       [[ 87., 150.]],

       [[162., 110.]],

       [[ 88., 131.]],

       [[196., 150.]],

       [[163., 166.]],

       [[206., 142.]],

       [[181., 167.]],

       [[194., 115.]],

       [[114., 151.]],

       [[131., 150.]],

       [[114., 128.]],

       [[184., 108.]]])




centroid = rightarr.mean(axis=0)
#print(centroid[0])
cent = []
s = []
for i in rightarr:
      #print(i[0])
      s.append(i[0])
      dist = np.linalg.norm(i-centroid)
      cent.append(dist)
      
mid = cent[len(cent)//2]

maxc = max(cent)

x = pd.DataFrame(s,columns=['a','b'])

for i,j in zip(x.index,cent):

      if(j<mid):
            plt.scatter(x['a'][i],x['b'][i],c='green')
      if(j==maxc):
            plt.scatter(x['a'][i],x['b'][i],c='black')
      else:
            plt.scatter(x['a'][i],x['b'][i],c='blue')
      



plt.scatter(centroid[0][0],centroid[0][1],c='red')

plt.show()

pos = rightarr[cent.index(maxc)]

if((pos[0][0]>centroid[0][0]) & (pos[0][0]-centroid[0][0] > pos[0][1]-centroid[0][1])):
      print("left")

elif((pos[0][1]>centroid[0][1]) & (pos[0][0]-centroid[0][0] < pos[0][1]-centroid[0][1])):
      print("up")





print(centroid)


#print(x['a'][0])