import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle

dataf={'score':[5,7,3,2],
       'names':['as','sd','sr','wf'] }

data=pd.DataFrame(dataf)

fig=plt.figure(
    FigureClass=Waffle,
    rows=7,
    values=data.score,
    labels=list(data.names))

plt.show()
