import pandas as pd
import numpy as np
from linearmodels import PanelOLS

### DEFINE
def main():
    df = import_data()
    fit1 = run_regression(df)
    formatted1 = format_model(fit1)

    fit2 = run_regression_1960(df)
    formatted2 = format_model(fit2)
    
    write_csv(formatted1, 'regression1.csv')
    write_csv(formatted2, 'regression2.csv')

    # with open('output/regression.csv', 'w') as f:
    #     f.write('<tab:regression>' + '\n')
    #     formatted1.to_csv(f, sep = '\t', index = False, header = False)
    #     formatted2.to_csv(f, sep = '\t', index = False, header = False)

    

def write_csv(formatted, name = ''):
    file_name = 'output/'+ name
    with open(file_name, 'w') as f:
        f.write('<tab:regression>' + '\n')
        formatted.to_csv(f, sep = '\t', index = False, header = False)

    
def import_data():
    df = pd.read_csv('input/data_cleaned.csv')
    df['post_tv'] = df['year'] > df['year_tv_introduced']
    
    return(df)

def run_regression(df):
    df = df.set_index(['county_id', 'year'])
    model = PanelOLS.from_formula('chips_sold ~ 1 + post_tv + EntityEffects + TimeEffects', data = df)
    fit = model.fit()
    
    return(fit)

def run_regression_1960(df):
    df = df.set_index(['county_id', 'year'])
    # add code to run only on the subset of Yr>= 1960
    df =  df.iloc[df.index.get_level_values('year') >= 1960]
    model = PanelOLS.from_formula('chips_sold ~ 1 + post_tv + EntityEffects + TimeEffects', data = df)
    fit = model.fit()
    
    return(fit)
    
def format_model(fit):
    formatted = pd.DataFrame({'coef'     : fit.params, 
                              'std_error': fit.std_errors, 
                              'p_value'  : fit.pvalues})
    formatted = formatted.loc[['post_tv[T.True]']]
    
    return(formatted)
    
### EXECUTE
main()