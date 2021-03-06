from codecs import ignore_errors
import streamlit as st
import pandas as pd
import plotly.express as px


confrimed_covid = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

confrimed_df = pd.read_csv(confrimed_covid)

new_df = confrimed_df.melt(id_vars=['Country/Region','Province/State','Lat','Long'])


temp_val = 0
def dailyCaseClac(x):
    global temp_val
    currentVal = x - temp_val
    temp_val = x
    return int(currentVal)




page_value  = st.sidebar.radio('Select Page', ['Demo', 'Cases'])
print(page_value)

# This is the streamlit method explanation

if page_value == 'Demo':

    st.write('Hello World ***Accepts Markdown as well***')
    st.text('Hello World from Streamlit.text')

    st.title("this is the Title Card")
    st.header('This is the header text')
    st.subheader('This is the sub title')
    st.dataframe(confrimed_df)
    st.table(confrimed_df[['Country/Region', 'Province/State']])



if page_value == 'Cases':
    st.header('Covid Cases')

    country_list = list(new_df['Country/Region'].unique())
    selectedCountry  = st.sidebar.selectbox('Select Country', country_list)

    new_df['Daily_Case'] = new_df[new_df['Country/Region'] == selectedCountry]['value'].apply(lambda x: int(dailyCaseClac(x)))

    new_df['Daily_Case'] = new_df['Daily_Case'].fillna(0).astype(int)
    df_selectedCountry = new_df[new_df['Country/Region'] == selectedCountry]

    # st.dataframe(new_df[new_df['Country/Region'] == selectedCountry].tail())

    fig = px.line(df_selectedCountry,x = 'variable',y = 'Daily_Case',)

    st.plotly_chart(fig)

    st.table(df_selectedCountry)