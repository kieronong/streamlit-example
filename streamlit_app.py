import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Yogurt Park: Froyo Orders in 2018')

def load_data(nrows):
    data = pd.read_csv('yopo_2015.csv', nrows=nrows)
    # data = data.set_index(['Flavor'])
    return data

data = load_data(10000)

st.bar_chart(data)

# minion_satisfaction = data[["Approving"]]

# min_date = data.index.min().to_pydatetime()
# max_date = data.index.max().to_pydatetime()

# [select_min, select_max] = st.slider("Choose a date range.", 
#     max_value=max_date, 
#     min_value=min_date,
#     value=[min_date, max_date])

# minion_satisfaction_selected = minion_satisfaction.loc[select_min : select_max].reset_index()

# minion_satisfaction_chart = alt.Chart(minion_satisfaction_selected).mark_line().encode(
#      alt.X('Date',
#         type='temporal',
#         axis=alt.Axis(
#             grid=False, 
#             tickCount={"interval": "month", "step": 4},
#             labelOverlap=True,
#             labelExpr="[timeFormat(datum.value, '%b')[0], timeFormat(datum.value, '%m') == '01' ? timeFormat(datum.value, '%Y') : '']" )), 
#      alt.Y('Approving', 
#         title='Percentage of Minions Approving', 
#         axis=alt.Axis(grid=True),
#         scale=alt.Scale(domain=[0, 100])))

# st.altair_chart(minion_satisfaction_chart, use_container_width=True)