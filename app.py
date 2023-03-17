import pickles
import scikit-learn
import numpy as np

filename = 'model.pickle'

model = pickle.load(open(filename, "rb"))

import streamlit as st

st.title('aaa')
a = st.number_input('Tham số a')
a_pred = model.predict(a)
if st.button('Giải'):
  st.success(a_pred)
