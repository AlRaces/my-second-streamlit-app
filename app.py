import pickle
import sklearn
import numpy as np

filename = 'model.pickle'

model = pickle.load(open(filename, "rb"))

import streamlit as st

st.title('aaa')
temp = np.array(st.number_input('Temp:'))
temp_pred = model.predict(temp.reshape(-1, 1))
if st.button('Giải'):
  st.success(temp_pred)
