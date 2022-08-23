import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

### DEFINE
def main():
    df = pd.read_csv('output/data_merged.csv')
    # plot_data(df)
    df = clean_data(df)
    plot_data(df)
    df.to_csv('output/data_cleaned.csv', index = False)

def plot_data(df):
    # plt.hist(df['chips_sold'])
    sns.displot(df['chips_sold'], stat='percent', bins = 20)
    plt.savefig('output/chips_sold.pdf')

def clean_data(df):
    df['chips_sold'][df['chips_sold'] == -999999] = np.NaN
    return(df)
    
### EXECUTE
main()
