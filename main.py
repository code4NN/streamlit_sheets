"""
Sadhana card Filling streamlit version
Requirements
1. Everyone can see everyone's scores
2. user with pin can edit..
3. a summary for this week for Sadhana Card IC
---
page-views for v1
1. for the user editing
2. summary of all
3. just seeing around
"""
import streamlit as st
import time
import datetime

st.set_page_config(page_title="Sadhana Card",
                    # page_icon='⌛',
                    layout='centered'
                    )

group = st.radio(label="Choose Group",
                options=['Nakul','Arjun','Bhim','Yud'],
                horizontal=True,key='group')
maplist = {'Nakul':['Bh. Ankur','Bh. Manish'],
            'Arjun':['Bh. Pragyesh','Bh. Dhruv','Bh. Nikhilesh'],
            'Bhim':['Bh. Satyam','Bh. Shridhar','Bh. Jateen','Bh. Akash','Bh. Karan'],
            'Yud':['Bh. Trideep','Bh. Raj','Bh. Shivendra','Bh. Parth','Bh. Vivek','Bh. Pradhuman']
            }
devotee = st.selectbox(label="Choose name",
                        options=sorted(maplist[group]),
                        key='user')
st.markdown("---")
# ---------Daily Filling Block

st.markdown("## Daily Filling")
fill = {}
fillingdate = '23 Dec, Thu'

with st.expander("Morning Program",expanded=True):
    # waking up
    fill['wakeup'] = st.time_input('wake up')
    st.markdown("")
    
    # SA
    fill['SA'] = st.radio(label="SA Attendance",
                        options=['not filled','PP','L0','L1','L2','L3','L4','L5','LL'],
                        index=0,
                        horizontal=True)
    st.markdown("")

    # MC
    fill['MC'] = st.radio(label="Morning Class",
                        options=['not filled','Full Present','Partially Present','Absent'],
                        index=0,
                        horizontal=True)
    st.markdown("")

    # MA
    fill['MA'] = st.radio(label="Mangal Aarti",
                        options=['not filled','Present','Absent'],
                        index=0,
                        horizontal=True)
    st.markdown("")

    # Chanting
    fill['chant'] = st.time_input("Chanting 📿")

# ---------------Reading and Hearing
with st.expander("Sadhana 🔥",expanded=True):
    fill['Reading'] = st.number_input(label="Reading",
                                        min_value=-1,
                                        value=-1,
                                        step=1
                                        )
    
    st.markdown("#### Hearings")
    fill['Hearing_SP'] = st.number_input(label="Srila Prabhupada",
                                        min_value=-1,
                                        value=-1,
                                        step=1
                                        )
            
    fill['Hearing_HHRNSM'] = st.number_input(label="HHRNSM",
                                        min_value=-1,
                                        value=-1,
                                        step=1
                                        )
            
    fill['Hearing_SP'] = st.number_input(label="HG RSP",
                                        min_value=-1,
                                        value=-1,
                                        step=1
                                        )
    
    verse = st.radio(label="Shloka",options=['notdone','done'],horizontal=True)
    if verse=='done':
        verse_number = st.text_input(label="Which one 😎")
        if verse_number =="":
            fill['verse'] = 'done'
        else:
            fill['verse'] = verse_number
    else :
        fill['verse'] = 'notdone'

# --------------- College and Studies
with st.expander('College and Studies',expanded=True):
    # st.markdown("### College")
    
    fill['college'] = st.radio(label='College Class',
                               options=['notfilled','All Present','Missed 1','Missed 2', 'Missed 2+','no classes'],
                               index=0,
                               horizontal=True)
    st.markdown("")

    fill['self_study'] = st.number_input(label="Self Study",
                                        min_value=-1,
                                        value=-1,
                                        step=1
                                        )


submit = st.button("done 👍")
if submit:
    fill