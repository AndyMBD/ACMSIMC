#coding:u8
from pylab import plt, mpl, np
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
# from pprint import pprint
from collections import OrderedDict as O
import pandas as pd

import streamlit as st
# left_column, mid_column, right_column  = st.columns(3)
left_sidebar  = st.sidebar
main_container = st.container()
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1
st.header(f"This page has run {st.session_state.counter} times.")
# plot style
style = np.random.choice(plt.style.available); print(style); 
# plt.style.use('grayscale') # ['grayscale', u'dark_background', u'bmh', u'grayscale', u'ggplot', u'fivethirtyeight']
# plot setting
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
mpl.rcParams['legend.fontsize'] = 12.5
# mpl.rcParams['legend.family'] = 'Times New Roman'
mpl.rcParams['font.family'] = ['Times New Roman']
mpl.rcParams['font.size'] = 14.0
# mpl.style.use('classic')
font = {'family' : 'Times New Roman', #'serif',
        'color' : 'darkblue',
        'weight' : 'normal',
        'size' : 14,}
textfont = {'family' : 'Times New Roman', #'serif',
            'color' : 'darkblue',
            'weight' : 'normal',
            'size' : 11.5,}

df_info = pd.read_csv(r"./build/info.dat")
data_file_name = df_info['DATA_FILE_NAME'].values[0].strip()
data_file_path = "./build/"+data_file_name

@st.cache_data
def fetch_and_clean_data():
    # Fetch data from URL here, and then clean it up.
    # 添加.dat文件解析逻辑
    if data_file_path.endswith('.dat'):
        # 假设.dat文件使用空格分隔，包含表头
        df_profiles = pd.read_csv(data_file_path, sep=',',header=0)
        # df_profiles = pd.read_csv(data_file_path)
    else:
        df_profiles = pd.read_csv(data_file_path)
    no_samples = df_profiles.shape[0]
    time = np.arange(no_samples) * df_info['DOWN_SAMPLE'].values[0] * df_info['TS'].values[0]
    df_profiles['Time'] = time  # 添加时间列

    return df_profiles

df_profiles = fetch_and_clean_data()
no_samples = df_profiles.shape[0]
no_traces  = df_profiles.shape[1]
time = np.arange(no_samples) * df_info['DOWN_SAMPLE'].values[0] * df_info['TS'].values[0]  # Fixed arange parameters

# Plotting
def get_axis(cNr):
    # fig, axes = plt.subplots(ncols=cNr[0], nrows=cNr[1], dpi=150, sharex=True);
    fig, axes = plt.subplots(ncols=cNr[0], nrows=cNr[1], sharex=True, figsize=(16*0.8, 9*0.8), dpi=80, facecolor='w', edgecolor='k');
    fig.subplots_adjust(right=0.95, bottom=0.1, top=0.95, hspace=0.2, wspace=0.02)    
    # fig.subplots_adjust(right=0.85, bottom=0.1, top=0.95, hspace=0.25)
    if sum(cNr)<=2:
        return axes
    else:
        return axes.ravel()

def plot_key(ax, key, df):
    ax.plot(time, df[key].values, '-', lw=1)
    ax.set_ylabel(key, fontdict=font)

def plot_it(ax, ylabel, d, time=None):
    count = 0
    for k, v in d.items():
        if count == 0:
            count += 1
            # ax.plot(time, v, '--', lw=2, label=k)
            ax.plot(time, v, '-', lw=1)
        else:
            # ax.plot(time, v, '-', lw=2, label=k)
            ax.plot(time, v, '-', lw=1)

    # ax.legend(loc='lower right', shadow=True)
    # ax.legend(bbox_to_anchor=(1.08,0.5), borderaxespad=0., loc='center', shadow=True)
    ax.set_ylabel(ylabel, fontdict=font)
    # ax.set_xlim(0,35) # shared x
    # ax.set_ylim(0.85,1.45)

# -- Create sidebar for plot controls
with left_sidebar:

    st.sidebar.markdown('## Time Range')
    time = st.sidebar.slider('Time range (s)', 
                                   min_value=df_profiles['Time'].min(), 
                                   max_value=df_profiles['Time'].max(), 
                                   value=(df_profiles['Time'].min(),df_profiles['Time'].max()))
    # container = st.container(border=True)
    # container.markdown('## Plot')
    # add_selectbox = st.sidebar.selectbox(
    #                             'How would you like to be contacted?',
    #                             df_profiles.columns.tolist())# Get list of column names
    selected_params = st.sidebar.multiselect(
        'Select parameters to display',
        options=df_profiles.columns[df_profiles.columns != 'Time'].tolist(),
        default=df_profiles.columns[0:4].tolist()  # Show first 3 parameters by default
    )
    st.write({data_file_name})
    st.write({data_file_path})
    st.write({no_samples})
    st.write({no_traces})
    st.write(len(df_profiles.columns))
    st.write({'Simulated time: %g s.'%(no_samples * df_info['TS'].values[0] * df_info['DOWN_SAMPLE'].values[0])})
    st.write({df_info['TS'].values[0]})
    st.write({df_info['DOWN_SAMPLE'].values[0]})
    st.write(df_profiles.head())
    st.write(df_profiles['Time'].max())
    st.write(df_profiles['Time'].min())

with main_container:
    for key in selected_params:
        if key != 'Time':
            # Apply time range filtering
            time_mask = (df_profiles['Time'] >= time[0]) & (df_profiles['Time'] <= time[1])
            fig, ax = plt.subplots(figsize=(12, 3))
            ax.plot(df_profiles['Time'][time_mask], 
                    df_profiles[key][time_mask],
                    '-', lw=1.2)
            ax.grid(True)
            ax.set_title(f"{key}", fontdict=font)
            ax.set_xlabel('Time [s]', fontdict=textfont)
            st.pyplot(fig)
            plt.close(fig)
