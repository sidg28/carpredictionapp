import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header('Visualize Data')
  st.set_option('deprecation.showPyplotGlobalUse',False)
  st.subheader('Scatter Plot')
  features_list = st.multiselect('Select the X-axis values: ',('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))
  for i in features_list:
    st.subheader(f'Scatter PLot between {i} and price')
    plt.figure(figsize = (12,6))
    sns.scatterplot(x = i,y='price',data = car_df)
    st.pyplot()
  st.subheader('Visualisation selector')
  plot_types = st.multiselect('Select charts or plots',('Histogram','Box Plot','Correlation Heatmap'))
  if 'Histogram' in plot_types:
    st.subheader('Histogram')
    columns = st.selectbox('Select the column to create its histogram',('carwidth','enginesize','horsepower'))
    plt.figure(figsize = (12,6))
    plt.title(f'Histogram for {columns}')
    plt.hist(car_df[columns],bins = 'sturges',edgecolor = 'black')
    st.pyplot()
  if 'Box Plot' in plot_types:
    st.subheader('Box Plot')
    columns = st.selectbox('Select the column to create its Box Plot',('carwidth','enginesize','horsepower'))
    plt.figure(figsize = (10,5))
    plt.title(f'Box Plot for {columns}')
    sns.boxplot(car_df[columns])
    st.pyplot()
  if 'Correlation Heatmap' in plot_types:
    st.subheader('Correlation  Heatmap')
    plt.figure(figsize = (10,10))
    ax = sns.heatmap(car_df.corr(),annot = True)
    bottom,top = ax.get_ylim()
    ax.set_ylim(bottom+0.5,top-0.5)
    st.pyplot()