import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def my_bargraph(item_names=('apple','banana','orange'), item_values=[20,80,50], check=True):
    sam = pd.DataFrame( {'item_values':item_values, 'item_names':item_names})
    sam = sam.sort(['item_values'])
    (item_values, item_names ) = np.array(sam.item_values),np.array(sam.item_names)
    if check:
        print(sam)
    else:
        y_pos = np.arange(len(item_names)) + 0.1
        x = max( [5, len(item_names) / 2.5 ])
        fig = plt.figure(figsize=(x,x))
        plt.barh(y_pos, item_values, align='center', height=0.25 , alpha=0.4 )
        plt.yticks(y_pos, item_names)
        plt.ylabel('columns')
        plt.xlabel('feature importance')
        plt.title('How fast you want to go home?')
        plt.show()
    print(', '.join(item_names))
    
my_bargraph()
