import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn as skl
from math import ceil
from scipy.stats import gaussian_kde, ttest_1samp
from statsmodels.stats.weightstats import ztest
from pandas.api.types import is_numeric_dtype

def scan_for_bad_data_cells(data: pd.DataFrame):
    print('Scanning dataframe for missing or bad data')
    # Compile a regex pattern for known bad strings
    # These can be ignored if values are accepted for that field
    regex_pattern = r'nan|unk|none|na|n/a|unknown|0|^$'
    # Create zero filled copy of passed df
    print(data.describe(include='all'))
    print(data.info(verbose=True, show_counts=True))
    counter_df = pd.DataFrame(0, index=np.arange(len(data)), columns=data.keys())
    for col in data.keys():
        if data[col].dtype == 'object':
            str_results = data[col].str.contains(regex_pattern, case=False, regex=True)
        else:
            str_results = data[col].isna() | data[col].isnull()
        results = data[col].isna() | data[col].isnull()
        full_results = str_results | results
        counter_df[col] = full_results.astype('Float32')
    print('Printout of scan results')
    counter_df.insert(0,'num_of_invalid_vals', counter_df.sum(axis=1, skipna=True, numeric_only=True))
    print(f'Invalid entries per index: {counter_df['num_of_invalid_vals']}')
    counter_df.set_index('num_of_invalid_vals', inplace=True)
    print(counter_df.tail(10).to_string())
    for col in counter_df:
        print(f'Number of invalid values in column {col}: {counter_df[col].sum()}')
      
def plot_all_data(data: pd.DataFrame, name: str='') -> None:
    print('Plotting all columns as hist and box plots')
    print(data.describe(include='all'))
    print(data.info(verbose=True, show_counts=True))
    col_len = len(data.keys())
    ax_rows = 2 * ceil(col_len / 3)
    print(f'Column Len = {col_len}')
    print(f'Axes Rows Amount = {ax_rows}')
    ax_cols = 3 if col_len >= 3 else col_len
    fig, axs = plt.subplots(ax_rows, ax_cols, figsize=[12, 8*ceil(ax_rows/2)])
    col_counter = 0
    row_counter = 0
    for col in data.keys():
        sns.histplot(data=data, x=col, ax=axs[row_counter,col_counter])
        
        sns.boxplot(data=data, x=col, ax=axs[row_counter+1,col_counter])
        col_counter += 1
        if col_counter > 2:
            col_counter = 0
            row_counter += 2
    fig.suptitle(name)

def simple_ttest_all_data_columns(data: pd.DataFrame, alpha:float=0.05, samples:int=30) -> dict:
    print('Starting T-tests...')
    r_dict = {}
    for col in data:
        if not is_numeric_dtype(data[col]):
            print(f'Skipping {col} as dtype is not numeric')
            continue
        col_mean = data[col].mean()
        print(f'mean for {col}: {col_mean}')
        t_statistic, p_val = ttest_1samp(data[col], samples)
        print(f'p_value for {col}: {p_val}')
        if p_val < alpha:
            print(f'Reject null hypothesis for {col}')
            r_dict[col] = (t_statistic, p_val)
        else:
            print(f'Fail to reject null hypothesis for {col}')
    print('')
    return r_dict

def ztest_all_data_columns(data: pd.DataFrame, alpha:float=0.05, samples:int=50) -> dict:
    print('Starting Z-tests')
    r_dict = {}
    for col in data:
        if not is_numeric_dtype(data[col]):
            print(f'Skipping {col} as dtype is not numeric')
            continue
        # Get two disticnt samples from the data
        sample1 = data.sample(samples, random_state=691)
        # Drop taken samples from the original data to ensure distinct samples
        remaining_data = data.drop(index=sample1.index.values)
        sample2 = remaining_data.sample(samples, random_state=691)
        col_mean = sample2[col].mean()
        print(f'mean for {col}: {col_mean}')
        
        ztest_score, p_val = ztest(sample1[col], value=col_mean, alternative='larger')
        print(f'p_value for {col}: {p_val}')
        if p_val < alpha:
            print(f'Reject null hypothesis for {col}')
            r_dict[col] = (ztest_score, p_val)
        else:
            print(f'Fail to reject null hypothesis for {col}')
    print('')
    return r_dict

def plot_features_vs_col(full_df, col_name):
    df = full_df.copy().drop(columns=[col_name])
    y = full_df[col_name]
    height = ceil(len(df.columns)/3)
    sub_fig, axs = plt.subplots(height,3, sharey=True, figsize=(20,6*height), constrained_layout=True)
    counter = 0
    lkws = {'color':'black', 'linestyle':'--', 'alpha':0.3}
    cbax = []
    for ax, col in zip(axs.flatten(), df.columns):
        df_x = df[col]
        xy = np.vstack([df_x, y])
        dens = gaussian_kde(xy)(xy)
        g = sns.regplot(x=df_x,y=y,ci=False, ax=ax, line_kws=lkws, label='Trend Line')
        g.set(ylim=(0,None))
        plot_scat = ax.scatter(df_x, y, c=dens, cmap='plasma')
        ax.set_xlabel(col)
        ax.set_ylabel('')
        if counter and counter % 3 != 0:
            ax.tick_params(axis='y', which='both', left=False, right=False)
        if counter and (counter+1) % 3 == 0:
            cbax.append(ax)
        counter += 1
        
    sub_fig.suptitle('Features × Total Spent', x=0.47, ha='center')
    sub_fig.supylabel('Total Spent')
    # axs[1].legend(loc='upper left')
    for ax in cbax:
        plt.colorbar(plot_scat, ax=ax, pad=0.01, label='KDE')
    plt.show()