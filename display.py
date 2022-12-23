import streamlit as st

import helper as gapi

st.header('api access testing')

sheetID = '1B5mc_TOPx04uGIYXDilb3oqd_CwZBb41eV6f-mCmQXA'
sample_range = 'random!B1:C2'
sample_range
range =st.text_input('enter range')
#--------------------

values = gapi.getData(sheetID,sample_range)
values
