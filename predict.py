import numpy as np
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_log_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
# Define the 'prediction()' function.
@st.cache()
def prediction(car_df,carwidth,enginesize,horsepower,drivewheel_fwd,car_company_buick):
  x = car_df.iloc[:,:-1]
  y = car_df['price']
  x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 42,test_size = 0.33)
  lin_reg = LinearRegression()
  lin_reg.fit(x_train,y_train)
  score = lin_reg.score(x_train,y_train)
  price = lin_reg.predict([[carwidth,enginesize,horsepower,drivewheel_fwd,car_company_buick]])
  price = price[0]
  y_test_pred = lin_reg.predict(x_test)
  r2score = r2_score(y_test,y_test_pred)
  mae = mean_absolute_error(y_test,y_test_pred)
  msle = mean_squared_log_error(y_test,y_test_pred)
  rmse = np.sqrt(mean_squared_error(y_test,y_test_pred))
  return price,score,r2score,mae,msle,rmse

def app(car_df):
  st.markdown("<p style = 'color:blue;font-size:25px'>This app uses <b>Linear Regression</b> to predict the price of a car based on your inputs.",unsafe_allow_html = True)
  st.subheader('Select Values: ')
  car_width = st.slider('Car width',float(car_df['carwidth'].min()),float(car_df['carwidth'].max()))
  engine_size = st.slider('Engine size',int(car_df['enginesize'].min()),int(car_df['enginesize'].max()))
  hp = st.slider('Horse Power',int(car_df['horsepower'].min()),int(car_df['horsepower'].max()))
  drivewheel = st.radio('Is it a forward drive wheel car?',('Yes','No'))
  if drivewheel =='No':
    drivewheel = 0
  else:
    drivewheel = 1
  ccb = st.radio('Is the car manufactured by Buick',('Yes','No'))
  if ccb == 'No':
    ccb = 0
  else:
    ccb = 1
  if st.button('Predict'):
    st.subheader('Prediction Results: ')
    price,score,car_r2,car_mae,car_msle,car_rmse = prediction(car_df,car_width,engine_size,hp,drivewheel,ccb)
    st.success('The predicted price of the car: ${:,}'.format(int(price)))
    st.info('Accuracy score of this model is {:.2%}'.format(score))
    st.info(f'R squared score of this model is {car_r2:.3f}')
    st.info(f'Mean Absolute Error of this model is {car_mae:.3f}')
    st.info(f'Mean Squared Log Error of this model is {car_msle:.3f}')
    st.info(f'Root Mean Squared Error of this model is {car_rmse:.3f}')