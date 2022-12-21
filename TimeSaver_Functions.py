import streamlit as st
import pandas as pd
import numpy as np
import numpy.ma as ma
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sc
from scipy.stats import norm
import pylab 
import warnings
warnings.filterwarnings(action="ignore")
from collections import Counter
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from statsmodels.tsa.seasonal import DecomposeResult, seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import acf,pacf
styles = [dict(selector="tr:hover",
                           props=[("background", "")]),
                      dict(selector="th", props=[("color", "black"),##eee
                                                 #("border", "0.1px solid black"),
                                                 ("padding", "4px 10px"),
                                                 ("border-collapse", "collapse"),
                                                 ("background", "#84A4A4"),
                                                 ("text-transform", "uppercase"),
                                                 ("text-align","center"),
                                                 ("border-right", "0.1px solid black"),
                                                 #("border-left", "1px red"),
                                                 ("font-size", "15px")]),
                      dict(selector="td", props=[#("color", "black"),
                                                 #("border", "0.1px solid black"),
                                                 ("text-align","center"),
                                                 ("padding", "1px 35px"),
                                                 ("border-right", "#B9B9B9"),
                                                 #("border-left", "0.5px solid "),
                                                 ("border-top", "0.5px solid"),
                                                 ("border-bottom", "0.5px red"),
                                                 ("border-collapse", "collapse"),
                                                 ("font-size", "15px")]),
                      dict(selector="table", props=[("font-family" , 'Arial'),
                                                    ("margin" , "10px auto"),
                                                    ("text-align","center"),
                                                    ("border-collapse" , "collapse"),
                                                    ("border" , "0px solid black"),
                                                    ("border-right", "1px solid black "),
                                                    ("border-left", "1px solid black "),
                                                    ("border-bottom" , "2px solid #00cccc"),
                                                   ]),
                      dict(selector="caption", props=[("caption-side", "bottom")])]



#To hide hamburger (top right corner) and “Made with Streamlit” footer, do this :
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
#st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

custom_streamlit_named_footer = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
            content:'Made By Ravinder with Streamlit';
            visibility: visible;
            display: block;
            position: relative;
            #background-color: red;
            padding: 0px;
            top: 0px;
            }
            </style>
            """

# hide_streamlit_style1 = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             footer:after {
#             content: 'Copyright © 2010-2013. All Rights Reserved. Disclaimer.';
#             visibility: visible;
#             text-decoration: none;
#             font-size: 20px;
#             background-color: transparent;
#             #color: #000000;
#             clear: left;
#             float: left;
#             position: relative;
#             left: 35%;
#             margin-top: 0px;
#             margin-bottom: 0px;
#             }
#             div.credits{display:none;}
#             </style>
#             """

#st.markdown(custom_streamlit_named_footer, unsafe_allow_html=True)

custom_streamlit_linkedin_footer = """
            <style>
                .footer {
                    position: absolute;
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    background-color: white;
                    color: black;
                    text-align: left;
                    }
            </style>
            <div class="footer"> Made By
                <a href="https://www.linkedin.com/in/ravinder-j-37849b244/" target="_blank">Ravinder</a>
            </div>
            
            """

#st.markdown(custom_streamlit_linkedin_footer, unsafe_allow_html=True)


CSS_Adjustments = """
            <style>
            .css-18e3th9 {/*decrease gap from header*/
                flex: 1 1 0%;
                width: 100%;
                padding: 0rem 5rem 0rem;
                min-width: auto;
                max-width: initial;
                }
            .css-qrbaxs { /*select box text size white theme*/
                font-size: 18px;
                color: black;
                margin-bottom: 7px;
                height: auto;
                min-height: 1.5rem;
                vertical-align: middle;
                display: flex;
                flex-direction: row;
                -webkit-box-align: center;
                align-items: center;
                }
                .css-16huue1 {
                font-size: 18px;
                }
            .css-qri22k { /* footer text size*/
                display: block;
                color: rgba(49, 51, 63, 0.4);
                flex: 0 1 0%;
                font-size: 18px;
                min-width: auto;
                max-width: initial;
                padding: 0.5rem 1rem;
                width: 100%;
                }
                thead, tbody, tfoot, tr, td, th { /* table border*/
                border-color: #B9B9B9;
                border-top-color: #B9B9B9;
                border-right-color: #B9B9B9;
                border-bottom-color: #B9B9B9;
                border-left-color: #B9B9B9;
                border-style: solid;
                border-width: 1px;
                text-align: center;
                }
                
                .st-c4 {/*selection box boder in black theme*/
                    border-left-color: #FC988C;
                }
                .st-c5 {
                    border-right-color: #FC988C;
                }
                .st-c6 {
                    border-top-color: #FC988C;
                }
                .st-c7 {
                    border-bottom-color: #FC988C;
                 }   
                .st-c3 {
                    border-top-color: #FC988C;
                }
                .st-dh {/*selection box boder in light theme*/
                    border-left-color: #FC988C;
                }
                .st-di {
                    border-right-color: #FC988C;
                }
                .st-dj {
                    border-top-color: #FC988C;
                }
                .st-dk {
                    border-bottom-color: #FC988C;
                }
                h1 { /*Time saver top padding*/
                    font-family: "Source Sans Pro", sans-serif;
                    font-weight: 700;
                    
                    padding: 0rem 0px 0rem;
                    margin: 0px;
                    line-height: 0.1;
                }
                .css-12x0zl8 { /*gap btwn Time saver and description*/
                    gap: 0rem;
                }
                
                .css-12ttj6m { /*form border red colour*/
                    border: 1px solid rgb(238 44 8 / 90%);
                    border-radius: 0.8rem;
                    padding: calc(1em - 1px);
                }

                .css-1cpxqw2 { /*submit button border red colour*/
                    background-color: rgb(255, 255, 255);
                    border: 1px solid rgb(240 4 4 / 85%);
                }  

            <style>
            """
#st.markdown(CSS_Adjustments, unsafe_allow_html=True)

def st_button2(icon, url, label, iconsize):
    if icon == 'linkedin':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
                {label}
            </a>
        </p>''' 
    elif icon == 'Email':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16">
                    <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z"/>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == '':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                {label}
            </a>
        </p>'''
    return st.markdown(button_code, unsafe_allow_html=True)



def About_Dataset (df):
    abtdf = f'<p style="font-family:sans-serif; font-size: 18px;">About Dataset</p>'
    st.write(f"**<h1 style='text-align: center;'>{abtdf}</h1>**", unsafe_allow_html=True)
    st.write(f"- **Number of Observations : {df.shape[0]}**")
    st.write(f"- **Number of Variables : {df.shape[1]}**")
    st.write(f"- **Number of Duplicated Rows : {len(np.where(df.duplicated())[0])}**")
    st.write('')
    var_types = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Variable types :</p>'
    st.markdown(f"**{var_types}**", unsafe_allow_html=True)
    colnum=[]
    numvar=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colnum.append(df[i].name)
    if len(colnum)>0:
        st.write(f"**►‎ ‎ ‎ ‎Numeric Variables : {len(colnum)}**") 
        st.write(f" **‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎{' ‎ ‎,‎ ‎ '.join(colnum)}**")
    colcat=[]
    for i in df:
        if df[i].dtypes == "object" :
            colcat.append(df[i].name)
        if df[i].dtypes != "object" :
            if df[i].nunique() <=5 :
                colcat.append(df[i].name)
    if len(colcat)>0:
        st.write(f"**►‎ ‎ ‎ ‎Categorical Variables : {len(colcat)}**")
        st.write(f" **‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎{' ‎ ‎,‎ ‎ '.join(colcat)}**")
    st.write("")
    u=pd.DataFrame({'datatype':df.dtypes.value_counts()})
    r=u.reset_index()
    r.rename(columns={'index':'datatype','datatype':'count'},inplace=True)
    r=r.astype(str)
    j=pd.DataFrame({'datatype':df.dtypes})
    g=j.reset_index()
    g.rename(columns={'index':'variable'},inplace=True)
    g=g.astype(str)
    var_dttypes = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Variable Datatypes :</p>'
    st.markdown(f"**{var_dttypes}**", unsafe_allow_html=True)
    row0_dt1,row0_dt2  = st.columns((2,5))
    with row0_dt1:            
        st.table(r.style.set_table_styles(styles))
        st.table(g.style.set_table_styles(styles))
    head = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Head of the Dataset</p>'
    st.markdown(f"**{head}**", unsafe_allow_html=True)
    st.table(df.head().style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
    st.write("")
    tail = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Tail of the Dataset</p>'
    st.markdown(f"**{tail}**", unsafe_allow_html=True)
    st.table(df.tail().style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
    
        
def Missing_values(df):
    missval = f'<p style="font-family:sans-serif; font-size: 18px;">Missing Values</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{missval}</h1>**", unsafe_allow_html=True)
    count = df.isnull().sum()
    percent_missing = df.isnull().sum() * 100 / len(df)
    missing_value_df = pd.DataFrame({'count': count,'percent_missing': round(percent_missing,2)})
    missing_value_df = pd.concat([pd.DataFrame(df.dtypes).rename(columns={0:'Data type'}),missing_value_df],axis=1)
    missing_value_df.reset_index(level=0, inplace=True)
    missing_value_df.rename(columns = {'index':'Variables'}, inplace = True)
    missing_value_df = missing_value_df.astype(str)
    hide_table_row_miss = """
        <style>
        tbody th {display:none}
        .blank {display:none}
        </style>
        """
    # Inject CSS with Markdown
    st.markdown(hide_table_row_miss, unsafe_allow_html=True)

    row0_NA01,row0_NAsp,row0_NA02 = st.columns((2,.1,2))
    with row0_NA01:            
        st.table(missing_value_df.style.set_precision(2).set_table_styles(styles))
    st.write("") 
    mul=[]
    with row0_NA02:
        st.write(f"**BARCHART OF MISSING VALUES**") 
        if df.shape[1] >15:
            for i in range(1,11):
                if i*15<df.shape[1]:
                    mul.append(i*15)
            fig, ax = plt.subplots()
            for i in mul:
                plt.subplot(len(mul),1,1)
                fig = plt.figure(figsize=(1,1))
                ax1=msno.bar(df.iloc[:,i-15:i],color="dodgerblue",fontsize=20)
                st.pyplot(fig)
            plt.subplot(1,1,1)
            ax2=msno.bar(df.iloc[:,mul[-1]:],color="dodgerblue",fontsize=20)
            st.pyplot(fig)
        else:
            fig, ax = plt.subplots()
            ax1=msno.bar(df,color="dodgerblue",fontsize=20)
            st.pyplot(fig)
            
            
def Outliers (df):
    outli = f'<p style="font-family:sans-serif; font-size: 18px;">Outlier Checking</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{outli}</h1>**", unsafe_allow_html=True)
    colout=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colout.append(df[i].name)
    if len(colout)>0:
        row0_out01,row0_out02,row0_outsp1,row0_out03 = st.columns((2,2,.2,2))
        with row0_out01:
            colout.insert(0,'None')
            st.write("##")
            col = st.selectbox("SELECT VARIABLE",colout)
            if col!='None':
                q1 = np.round(df[col].quantile(0.25),2)
                q3 = np.round(df[col].quantile(0.75),2)
                iqr = q3 - q1
                low  = np.round(q1 - (1.5*iqr),2)
                high = np.round(q3 + (1.5*iqr),2)
                out1 = df[col][df[col]<low].values
                out2 = df[col][df[col]>high].values
                st.write("##")
                new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 18px;"> Five Number Summary</p>'
                st.markdown(f"<h1 color: black;'>{new_title1}</h1>", unsafe_allow_html=True)
                st.write(f"- **Minimum ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎   {df[col].min():.2f}**")
                st.write(f"- **First Quartile( Q1) ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ :‎ ‎ ‎ ‎ {q1:.2f}**")
                st.write(f"- **Median ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎ {df[col].median():.2f}**")
                st.write(f"- **Third Quartile( Q3) ‎‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎{q3:.2f}**")
                st.write(f"- **Maximum‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎   {df[col].max():.2f}**")

                st.write("")
                new_title2 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 18px;">Observations:</p>'
                st.markdown(f"<h1 color: black;'>{new_title2}</h1>", unsafe_allow_html=True)

                if len(out1)>0:
                    st.write(f"- **values less than {low:.0f} are outliers**")

                if len(out2)>0:
                    st.write(f"- **values greater than {high:.0f} are outliers**")

                if (len(out1)==0) & (len(out2)==0) :
                    st.write(f"- **No Outliers Found**")

                with row0_out02:
                    new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 16px;">{df[col].name} </p>'
                    st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)

                    warnings.filterwarnings(action="ignore")
                    fig, ax = plt.subplots()
                    fig = go.Figure()
                    fig.add_trace(go.Box(
                        y=df[col],
                        name=df[col].name,
                        marker_color='#FF4136',
                        boxmean=True # represent mean
                    ))
                    fig.update_layout(title_text=f"Boxplot‎ ‎ of‎ ‎ {df[col].name}",title={
                                'y':0.9,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'},title_font_color="#FF4136")
                    st.plotly_chart(fig)    
                    
            else:
                with row0_out02:
                    st.write("##")
                    st.write("##")
                    st.warning("**SELECT VARIABLE**")
                
        st.write("##")
        st.write("##")
        if st.checkbox("Select Multiple Variables"):
            #del colout[0:1]

            form1 = st.form(key = 'Options')
            
            if len(colout[1:])<=10:
                all = st.checkbox("Select all")
                if all:
                    selected_options = form1.multiselect("Select one or more Variables:",colout[1:],colout[1:])
                else:
                    selected_options =  form1.multiselect("Select one or more Variables:",colout[1:])
            elif len(colout[1:])>10:
                selected_options = form1.multiselect("Select one or more Variables (max 10):",colout[1:])[0:10]
                
            if "load_statef" not in st.session_state:
                st.session_state.load_statef = False

            if form1.form_submit_button("Submit") or st.session_state.load_statef:
                st.session_state.load_statef = True
                for col in selected_options:
                    #col_button = st.radio("",options = [f'{df[col].name}'])
                    row0_out01,row0_out02,row0_outsp1,row0_out03 = st.columns((2,2,.2,2))
                    with row0_out01:
                        st.write("##")
                        q1 = np.round(df[col].quantile(0.25),2)
                        q3 = np.round(df[col].quantile(0.75),2)
                        iqr = q3 - q1
                        low  = np.round(q1 - (1.5*iqr),2)
                        high = np.round(q3 + (1.5*iqr),2)
                        out1 = df[col][df[col]<low].values
                        out2 = df[col][df[col]>high].values
                        st.write("##")
                        new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 18px;"> Five Number Summary</p>'
                        st.markdown(f"<h1 color: black;'>{new_title1}</h1>", unsafe_allow_html=True)
                        st.write(f"- **Minimum ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎   {df[col].min():.2f}**")
                        st.write(f"- **First Quartile( Q1) ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ :‎ ‎ ‎ ‎ {q1:.2f}**")
                        st.write(f"- **Median ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎ {df[col].median():.2f}**")
                        st.write(f"- **Third Quartile( Q3) ‎‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎{q3:.2f}**")
                        st.write(f"- **Maximum‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎   {df[col].max():.2f}**")

                        st.write("##")

                        new_title2 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 18px;">Observations:</p>'
                        st.markdown(f"<h1 color: black;'>{new_title2}</h1>", unsafe_allow_html=True)

                        if len(out1)>0:
                            st.write(f"- **values less than {low:.0f} are outliers**")

                        if len(out2)>0:
                            st.write(f"- **values greater than {high:.0f} are outliers**")

                        if (len(out1)==0) & (len(out2)==0) :
                            st.write(f"- **No Outliers Found**")

                    with row0_out02:
                        new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 16px;">{df[col].name} </p>'
                        st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)

                        warnings.filterwarnings(action="ignore")
                        fig, ax = plt.subplots()
                        fig = go.Figure()
                        fig.add_trace(go.Box(
                            y=df[col],
                            name=df[col].name,
                            marker_color='#FF4136',
                            boxmean=True # represent mean
                        ))
                        fig.update_layout(title_text=f"Boxplot‎ ‎ of‎ ‎ {df[col].name}",title={
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},title_font_color="#FF4136")

                        st.plotly_chart(fig)
                    st.write("*-"*280)    

    else:
        st.warning('**NO NUMERIC VARIABLE IS AVAILABLE**') 
        

        
        
def Outliers_full (df):
    outli = f'<p style="font-family:sans-serif; font-size: 18px;">Outlier Checking</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{outli}</h1>**", unsafe_allow_html=True)
    colout=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colout.append(df[i].name)
    if len(colout)>0:
        for col in colout:
            #col_button = st.radio("",options = [f'{df[col].name}'])
            row0_out01,row0_out02,row0_outsp1,row0_out03 = st.columns((2,2,.2,2))
            with row0_out01:
                st.write("##")
                q1 = np.round(df[col].quantile(0.25),2)
                q3 = np.round(df[col].quantile(0.75),2)
                iqr = q3 - q1
                low  = np.round(q1 - (1.5*iqr),2)
                high = np.round(q3 + (1.5*iqr),2)
                out1 = df[col][df[col]<low].values
                out2 = df[col][df[col]>high].values
                st.write("##")
                new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 18px;"> Five Number Summary</p>'
                st.markdown(f"<h1 color: black;'>{new_title1}</h1>", unsafe_allow_html=True)
                st.write("##")
                st.write(f"- **Minimum ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎   {df[col].min():.2f}**")
                st.write(f"- **First Quartile( Q1) ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ :‎ ‎ ‎ ‎ {q1:.2f}**")
                st.write(f"- **Median ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎ {df[col].median():.2f}**")
                st.write(f"- **Third Quartile( Q3) ‎‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎{q3:.2f}**")
                st.write(f"- **Maximum‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎   :‎ ‎ ‎ ‎   {df[col].max():.2f}**")

                st.write("##")

                new_title2 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 18px;">Observations:</p>'
                st.markdown(f"<h1 color: black;'>{new_title2}</h1>", unsafe_allow_html=True)

                if len(out1)>0:
                    st.write(f"- **values less than {low:.0f} are outliers**")

                if len(out2)>0:
                    st.write(f"- **values greater than {high:.0f} are outliers**")

                if (len(out1)==0) & (len(out2)==0) :
                    st.write(f"- **No Outliers Found**")

            with row0_out02:
                new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 16px;">{df[col].name} </p>'
                st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)

                warnings.filterwarnings(action="ignore")
                fig, ax = plt.subplots()
                fig = go.Figure()
                fig.add_trace(go.Box(
                    y=df[col],
                    name=df[col].name,
                    marker_color='#FF4136',
                    boxmean=True # represent mean
                ))
                fig.update_layout(title_text=f"Boxplot‎ ‎ of‎ ‎ {df[col].name}",title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},title_font_color="#FF4136")

                st.plotly_chart(fig)
            st.write("*-"*280)
    else:
        st.warning('**NO NUMERIC VARIABLE IS AVAILABLE**')     
        
def Univariate_Continuous(df):
    uvcont = f'<p style="font-family:sans-serif; font-size: 18px;">Univariate Continuous</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{uvcont}</h1>**", unsafe_allow_html=True)
    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colnum.append(df[i].name)

    if len(colnum)>0:
        row16_1, row16_sp1,row16_sp2,row16_4  = st.columns((4,.2,.2, 10.5))
        with row16_1:
            colnum.insert(0,'None')
            col = st.selectbox("SELECT VARIABLE",colnum)  
            if col!='None':
                new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Descriptive Statistics</p>'
                st.markdown(f"**{new_title1}**", unsafe_allow_html=True)
                q1 = np.round(df[col].quantile(0.25),2)
                q3 = np.round(df[col].quantile(0.75),2)
                percnt_mis=str(round(df[col].isnull().sum()/df[col].shape[0]*100,2))
                percnt_zero=str(round(df[df[col]==0].shape[0]/df[col].shape[0]*100,2))
                d = {'Count':df[col].count(),'Distinct':df[col].nunique(),
                     'Missing ( '+percnt_mis+' %)':df[col].isnull().sum(),
                     'Zeros ( '+percnt_zero+' %)':df[df[col]==0].shape[0],
                     'Sum':df[col].sum(),'Mean':round(df[col].mean()), 
                 'Median': round(df[col].median()),'Mode':round(df[col].mode()[0]),
                'Minimum':round(df[col].min(),1),'Maximum':round(df[col].max(),1),'Range':round(df[col].max()-df[col].min()),
                 'Q1':q1,'Q3':q3,'IQR':q3-q1,
                'Variance':round(df[col].var()),'Standard Deviation':round(df[col].std(),1),
                'Skewness':round(df[col].skew(),1),'Kurtosis':round(df[col].kurtosis(),1)}
                stat = pd.DataFrame(data=d,index=['Values'])
                stat=stat.T
                stat.reset_index(level=0, inplace=True)
                stat.rename(columns = {'index':'Measures'}, inplace = True)
                hide_table_row_stat = """
                                        <style>
                                        tbody th {display:none}
                                        .blank {display:none}
                                        </style>
                                        """
                # Inject CSS with Markdown
                st.markdown(hide_table_row_stat, unsafe_allow_html=True)
                st.table(stat.style.set_precision(2).set_table_styles(styles))

                with row16_4:
                    uvcontvar = f'<p style="font-family:sans-serif; color:green; font-size: 16px;">{df[col].name}</p>'
                    st.markdown(f"**<h1 style='text-align: center; '>{uvcontvar}</h1>**", unsafe_allow_html=True)
                    st.write("##")
                    st.write("##")
                    new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 16px;">Observations :</p>'
                    st.markdown(f"**{new_title1}**", unsafe_allow_html=True)
                    if df[col].skew() >= -0.5 and df[col].skew() <= 0.5:
                        st.write("- **Distribution seems to be approximately symmetric**")
                    elif df[col].skew() >= -1 and df[col].skew() < -0.5:
                        st.write("- **Distribution is slightly negatively skewed**")
                    elif df[col].skew() <= 1 and df[col].skew() > 0.5:
                        st.write("- **Distribution is slightly positively skewed**")
                    elif df[col].skew() < -1:
                        st.write("- **Distribution is negatively skewed**")
                    elif df[col].skew() > 1 :
                        st.write("- **Distribution is positvely skewed**")

                    st.write(f"- **Most of the {df[col].name} ranges between {round(df[col].quantile(0.25))} and {round(df[col].quantile(0.75))}**")
                    st.write("")
                    warnings.filterwarnings(action="ignore")
                    fig, ax = plt.subplots()
                    fig = plt.figure(figsize=(15,5)) # try different values
                    ax = plt.axes()
                    plt.gcf().autofmt_xdate()
                    plt.subplot(1, 3, 1)
                    box=sns.boxplot(df[col]);
                    title = "Boxplot of {}"
                    plt.title(title.format(df[i].name))
                    title= "Boxplot for {}"
                    plt.title(title.format(df[col].name))
                    plt.subplot(1, 3, 2) 
                    dist=sns.distplot(df[col],fit=norm,fit_kws={"color":"red"})
                    title = "Distribution Plot of {}"
                    plt.title(title.format(df[col].name))
                    plt.subplot(133)
                    prob=sc.probplot(df[col],plot=plt);
                    plt. tight_layout()
                    st.pyplot(fig)
                    ############
                    ###PLOTLY###
                    ############
#                     fig = make_subplots(rows=1, cols=3,subplot_titles=[f"Boxplot of {col}", f"Distribution Plot of {col}", f"Probability Plot of {col}"])#,
#                                        #column_widths=[0.55, 0.45,0.55])
#                     fig.add_trace(go.Box(x=df[col].dropna(),name='',boxmean=True,showlegend=False),row=1,col=1,)

#                     distplfig1 = ff.create_distplot([df[col].dropna().values.tolist()], group_labels=['Distribution'],
#                                                     show_rug=True)
                    
#                     distplfig = ff.create_distplot([df[col].dropna().values.tolist()], group_labels = ['Norm'],curve_type='normal',
#                                                    colors=['#FF4136'],show_rug=True)
                    
#                     fig.add_trace(distplfig.data[1],row=1, col=2)
                    
#                     for k in range(len(distplfig1.data)):
#                         fig.add_trace(distplfig1.data[k],
#                         row=1, col=2)
                        
#                     from statsmodels.graphics.gofplots import qqplot
#                     qqplot_data = qqplot(df[col].dropna(), line='s').gca().lines

#                     fig.add_trace(go.Scatter(
#                         x = qqplot_data[0].get_xdata(),
#                         y = qqplot_data[0].get_ydata(),
#                         mode='markers',
#                         line=dict(color='#6CB3FF',width=1),
#                         showlegend=False,name='Actual'
#                     ),row=1, col=3)
            
#                     fig.add_trace(go.Scatter(
#                         x = qqplot_data[1].get_xdata(),
#                         y = qqplot_data[1].get_ydata(),
#                         mode='lines',
#                         showlegend=True,name='Expected'
#                     ),row=1, col=3)
        
#                     fig.update_layout(barmode='overlay')
#                     fig.update_layout(autosize=False,width=1000,height=400)
#                     fig.update_xaxes(title_text=col, row=1, col=1)
#                     fig.update_xaxes(title_text=col, row=1, col=2)
#                     #fig.update_yaxes(title_text="Density", row=1, col=2)

#                     fig.update_xaxes(title_text="Theoritical Quantities", row=1, col=3)
#                     fig.update_yaxes(title_text="Sample Quantities", row=1, col=3)
#                     fig.update_traces(showlegend=False)
#                     st.plotly_chart(fig)
    
    
#                     with st.expander("See explanation"):
#                         mul_button = st.radio("",options = ['Head of Dataset','Tail of Dataset'])
#                         st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
            
            else:
                with row16_4:
                    st.write("##")
                    st.warning("**SELECT CONTINUOUS VARIABLE**")
                
        st.write("##")
        st.write("##")
        if st.checkbox("Select Multiple Continuous Variables"):

            form1 = st.form(key = 'Options')
            
            if len(colnum[1:])<=10:
                all = st.checkbox("Select all Continuous Variables")
                if all:
                    selected_options = form1.multiselect("Select one or more Variables:",colnum[1:],colnum[1:])
                else:
                    selected_options = form1.multiselect("Select one or more Variables:",colnum[1:])   
                
            elif len(colnum[1:])>10:
                selected_options = form1.multiselect("Select one or more Variables (max 10):",colnum[1:])[0:10]        
                
            if "load_statef" not in st.session_state:
                st.session_state.load_statef = False

            if form1.form_submit_button("Submit") or st.session_state.load_statef:
                st.session_state.load_statef = True
                for i in selected_options:
                    #col_button = st.radio("",options = [f'{df[i].name}'])
                    uvcont_1, uvcont_sp1,uvcont_sp2,uvcont_4  = st.columns((4,.2,.2, 10.5))
                    with uvcont_1:
                        st.write("##")
                        st.write('')
                        new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 18px;">Descriptive Statistics</p>'
                        st.markdown(f"**{new_title1}**", unsafe_allow_html=True)
                        q1 = np.round(df[i].quantile(0.25),2)
                        q3 = np.round(df[i].quantile(0.75),2)
                        percnt_mis=str(round(df[i].isnull().sum()/df[i].shape[0]*100,2))
                        percnt_zero=str(round(df[df[i]==0].shape[0]/df[i].shape[0]*100,2))
                        d = {'Count':df[i].count(),
                             'Distinct':df[i].nunique(),
                             'Missing ( '+percnt_mis+' %)':df[i].isnull().sum(),
                             'Zeros ( '+percnt_zero+' %)':df[df[i]==0].shape[0],
                             'Sum':df[i].sum(),
                             'Mean':round(df[i].mean()),
                             'Median': round(df[i].median()),
                             'Mode':round(df[i].mode()[0]),
                             'Minimum':round(df[i].min(),1),
                             'Maximum':round(df[i].max(),1),
                             'Range':round(df[i].max()-df[i].min()),
                             'Q1':q1,
                             'Q3':q3,
                             'IQR':q3-q1,
                             'Variance':round(df[i].var()),
                             'Standard Deviation':round(df[i].std(),1),
                             'Skewness':round(df[i].skew(),1),
                             'Kurtosis':round(df[i].kurtosis(),1)}
                        stat = pd.DataFrame(data=d,index=['Values'])
                        stat=stat.T
                        stat.reset_index(level=0, inplace=True)
                        stat.rename(columns = {'index':'Measures'}, inplace = True)
                        st.table(stat.style.set_precision(2).set_table_styles(styles)) 
                    with uvcont_4:
                        uvcontvar = f'<p style="font-family:sans-serif; color:green; font-size: 16px;">{df[i].name}</p>'
                        st.markdown(f"**<h1 style='text-align: center; '>{uvcontvar}</h1>**", unsafe_allow_html=True)
                        new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 16px;">Observations :</p>'
                        st.markdown(f"**{new_title1}**", unsafe_allow_html=True)
                        if df[i].skew() >= -0.5 and df[i].skew() <= 0.5:
                            st.write("- **Distribution seems to be approximately symmetric**")
                        elif df[i].skew() >= -1 and df[i].skew() < -0.5:
                            st.write("- **Distribution is slightly negatively skewed**")
                        elif df[i].skew() <= 1 and df[i].skew() > 0.5:
                            st.write("- **Distribution is slightly positively skewed**")
                        elif df[i].skew() < -1:
                            st.write("- **Distribution is negatively skewed**")
                        elif df[i].skew() > 1 :
                            st.write("- **Distribution is positvely skewed**")

                        st.write(f"- **Most of the {df[i].name} ranges between {round(df[i].quantile(0.25))} and {round(df[i].quantile(0.75))}**")
                        st.markdown("")
                        warnings.filterwarnings(action="ignore")
                        fig, ax = plt.subplots()
                        fig = plt.figure(figsize=(15,5)) # try different values
                        ax = plt.axes()
                        plt.gcf().autofmt_xdate()
                        plt.subplot(1, 3, 1)
                        box=sns.boxplot(df[i]);
                        title = "Boxplot of {}"
                        plt.title(title.format(df[i].name))
                        title= "Boxplot for {}"
                        plt.title(title.format(df[i].name))
                        plt.subplot(1, 3, 2) 
                        dist=sns.distplot(df[i],fit=norm,fit_kws={"color":"red"})
                        title = "Distribution Plot of {}"
                        plt.title(title.format(df[i].name))
                        plt.subplot(133)
                        prob=sc.probplot(df[i],plot=plt);
                        plt. tight_layout()
                        st.pyplot(fig)
                        ############
                        ###PLOTLY###
                        ############
#                         col=i
#                         fig = make_subplots(rows=1, cols=3,subplot_titles=[f"Boxplot of {col}", f"Distribution Plot of {col}", f"Probability Plot of {col}"])#,
#                                        #column_widths=[0.55, 0.45,0.55])
#                         fig.add_trace(go.Box(x=df[col].dropna(),name='',boxmean=True,showlegend=False),row=1,col=1,)

#                         distplfig1 = ff.create_distplot([df[col].dropna().values.tolist()], group_labels=['Distribution'],
#                                                         show_rug=True)

#                         distplfig = ff.create_distplot([df[col].dropna().values.tolist()], group_labels = ['Norm'],curve_type='normal',
#                                                        colors=['#FF4136'],show_rug=True)

#                         fig.add_trace(distplfig.data[1],row=1, col=2)

#                         for k in range(len(distplfig1.data)):
#                             fig.add_trace(distplfig1.data[k],
#                             row=1, col=2)

#                         from statsmodels.graphics.gofplots import qqplot
#                         qqplot_data = qqplot(df[col].dropna(), line='s').gca().lines

#                         fig.add_trace(go.Scatter(
#                             x = qqplot_data[0].get_xdata(),
#                             y = qqplot_data[0].get_ydata(),
#                             mode='markers',
#                             line=dict(color='#6CB3FF',width=1),
#                             showlegend=False,name='Actual'
#                         ),row=1, col=3)

#                         fig.add_trace(go.Scatter(
#                             x = qqplot_data[1].get_xdata(),
#                             y = qqplot_data[1].get_ydata(),
#                             mode='lines',
#                             showlegend=True,name='Expected'
#                         ),row=1, col=3)

#                         fig.update_layout(barmode='overlay')
#                         fig.update_layout(autosize=False,width=1000,height=400)
#                         fig.update_xaxes(title_text=col, row=1, col=1)
#                         fig.update_xaxes(title_text=col, row=1, col=2)
#                         #fig.update_yaxes(title_text="Density", row=1, col=2)

#                         fig.update_xaxes(title_text="Theoritical Quantities", row=1, col=3)
#                         fig.update_yaxes(title_text="Sample Quantities", row=1, col=3)
#                         fig.update_traces(showlegend=False)
#                         st.plotly_chart(fig)                       
                        
                        
                    st.write("*-"*280)    

    else:
        st.warning('**NO NUMERIC VARIABLE IS AVAILABLE**')
        

        
def Univariate_Continuous_full(df):
    uvcont = f'<p style="font-family:sans-serif; font-size: 18px;">Univariate Continuous</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{uvcont}</h1>**", unsafe_allow_html=True)
    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colnum.append(df[i].name)

    if len(colnum)>0:
        for i in colnum:
            #col_button = st.radio("",options = [f'{df[i].name}'])
            uvcontvar = f'<p style="font-family:sans-serif; color:green; font-size: 16px;">{df[i].name}</p>'
            st.markdown(f"**<h1 style='text-align: center; '>{uvcontvar}</h1>**", unsafe_allow_html=True)
            uvcont_1, uvcont_sp1,uvcont_sp2,uvcont_4  = st.columns((4,.2,.2, 10.5))
            with uvcont_1:
                #st.write("##")
                new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 18px;">Descriptive Statistics</p>'
                st.markdown(f"**{new_title1}**", unsafe_allow_html=True)
                q1 = np.round(df[i].quantile(0.25),2)
                q3 = np.round(df[i].quantile(0.75),2)
                percnt_mis=str(round(df[i].isnull().sum()/df[i].shape[0]*100,2))
                percnt_zero=str(round(df[df[i]==0].shape[0]/df[i].shape[0]*100,2))
                d = {'Count':df[i].count(),
                     'Distinct':df[i].nunique(),
                     'Missing ( '+percnt_mis+' %)':df[i].isnull().sum(),
                     'Zeros ( '+percnt_zero+' %)':df[df[i]==0].shape[0],
                     'Sum':df[i].sum(),
                     'Mean':round(df[i].mean()),
                     'Median': round(df[i].median()),
                     'Mode':round(df[i].mode()[0]),
                     'Minimum':round(df[i].min(),1),
                     'Maximum':round(df[i].max(),1),
                     'Range':round(df[i].max()-df[i].min()),
                     'Q1':q1,
                     'Q3':q3,
                     'IQR':q3-q1,
                     'Variance':round(df[i].var()),
                     'Standard Deviation':round(df[i].std(),1),
                     'Skewness':round(df[i].skew(),1),
                     'Kurtosis':round(df[i].kurtosis(),1)}
                stat = pd.DataFrame(data=d,index=['Values'])
                stat=stat.T
                stat.reset_index(level=0, inplace=True)
                stat.rename(columns = {'index':'Measures'}, inplace = True)
                st.table(stat.style.set_precision(2).set_table_styles(styles)) 
            with uvcont_4:
#                 uvcontvar = f'<p style="font-family:sans-serif; color:green; font-size: 16px;">{df[i].name}</p>'
#                 st.markdown(f"**<h1 style='text-align: center; '>{uvcontvar}</h1>**", unsafe_allow_html=True)
                st.write("##")
                st.write("#")
                new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 16px;">Observations :</p>'
                st.markdown(f"**{new_title1}**", unsafe_allow_html=True)
                if df[i].skew() >= -0.5 and df[i].skew() <= 0.5:
                    st.write("- **Distribution seems to be approximately symmetric**")
                elif df[i].skew() >= -1 and df[i].skew() < -0.5:
                    st.write("- **Distribution is slightly negatively skewed**")
                elif df[i].skew() <= 1 and df[i].skew() > 0.5:
                    st.write("- **Distribution is slightly positively skewed**")
                elif df[i].skew() < -1:
                    st.write("- **Distribution is negatively skewed**")
                elif df[i].skew() > 1 :
                    st.write("- **Distribution is positvely skewed**")

                st.write(f"- **Most of the {df[i].name} ranges between {round(df[i].quantile(0.25))} and {round(df[i].quantile(0.75))}**")
                st.markdown("")
                warnings.filterwarnings(action="ignore")
                fig, ax = plt.subplots()
                fig = plt.figure(figsize=(15,5)) # try different values
                ax = plt.axes()
                plt.gcf().autofmt_xdate()
                plt.subplot(1, 3, 1)
                box=sns.boxplot(df[i]);
                title = "Boxplot of {}"
                plt.title(title.format(df[i].name))
                title= "Boxplot for {}"
                plt.title(title.format(df[i].name))
                plt.subplot(1, 3, 2) 
                dist=sns.distplot(df[i],fit=norm,fit_kws={"color":"red"})
                title = "Distribution Plot of {}"
                plt.title(title.format(df[i].name))
                plt.subplot(133)
                prob=sc.probplot(df[i],plot=plt);
                plt. tight_layout()
                st.pyplot(fig)
                
            st.write("*-"*280) 
        
    else:
        st.warning('**NO NUMERIC VARIABLE IS AVAILABLE**')    
        
        
def Univariate_Categorical(df):
    catg = f'<p style="font-family:sans-serif; font-size: 18px;">Univariate Categorical</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{catg}</h1>**", unsafe_allow_html=True)
    colcat=[]
    for i in df:
        if df[i].dtypes == "object" :
            if df[i].nunique()>0:
                colcat.append(df[i].name)

        if df[i].dtypes != "object" :
            if df[i].nunique() > 0 and df[i].nunique() <=5 :
                colcat.append(df[i].name)
    if len(colcat)>0:
        rowcat1,rowcatsp, rowcat2,rowcatsp1  = st.columns((1.5,.5,2,.2))
        with rowcat1:
            colcat.insert(0,'None')
            col = st.selectbox("SELECT VARIABLE",colcat)
            if col != 'None':
                df[col] = df[col].fillna('NaN').astype(str)
                clas=df[col].value_counts().index.tolist()
                category=st.selectbox("SELECT CATEGORY",clas)
                st.write("")
                if 1 < df[col].nunique()<=20:
                   #plt.rcdefaults()
                    fig, ax = plt.subplots()
    #                         fig = plt.figure(figsize=(15,df[col].nunique()*1.8))
    #                         ax1=sns.barplot(df[col].value_counts().values,(df[col].value_counts().index).astype(str));
    #                         for p in ax1.patches:
    #                             ax1.annotate(int(p.get_width()),
    #                     ((p.get_y() + p.get_width()), p.get_y()), 
    #                     xytext=(2, -30),fontsize=22,
    #                     rotation=0,
    #                     textcoords='offset points', 
    #                     horizontalalignment='left')
    #                         total = len(df[col].dropna())
    #                         for p in ax1.patches:
    #                             percentage = '{:.1f}%'.format(100 * p.get_width()/total)
    #                             x = p.get_x() + p.get_width() + 0.02
    #                             y = p.get_y() + p.get_height()/1.2
    #                             ax1.annotate(percentage, (x, y),fontsize=22)
    #                         plt.margins(x=0.15)
    #                         #else:
    #                         plt.xlabel('count',fontsize=30)
    #                         title = "Count Plot of {}"
    #                         plt.title(title.format(df[col].name),fontsize=30)
    #                         plt.xticks(fontsize=25)
    #                         plt.yticks(fontsize=25)
    #                         st.pyplot(fig)

                    #fig = px.histogram(y=df[col].astype(str)).update_yaxes(categoryorder='total ascending')

                    dfcat = pd.DataFrame(df[[col]].dropna().astype(str).groupby(col).agg('size')).reset_index().rename(columns={0:'count'}).sort_values('count',ascending=False).reset_index(drop=True)

                    fig = px.bar(dfcat, y = col, x = 'count', text_auto=True,color='count',title=f"count plot of {df[col].name}").update_yaxes(categoryorder='min ascending')
                    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False) #'.2s'

    #                 fig.update_layout(
    #                         autosize=False,
    #                         width=500,
    #                         height=500
    #                     )

                    if df[col].nunique()<=2:

                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df[col].nunique()*150,#df2[x].nunique()
                        )


                    elif df[col].nunique()>=3 and df[col].nunique()<=5:

                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df[col].nunique()*100,#df2[x].nunique()
                        )

                    elif df[col].nunique()>5 and df[col].nunique()<=10:

                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df[col].nunique()*70,#df2[x].nunique()
                        )

                    else:
                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df[col].nunique()*50,#df2[x].nunique()
                        )

                    fig.update_layout(title_text=f"count plot of {df[col].name}",title={
                                        'y':0.9,
                                        'x':0.5,
                                        'xanchor': 'center',
                                        'yanchor': 'top'},title_font_color="red")
                    st.plotly_chart(fig)

    #             elif df[col].nunique() ==1 :
    #                 fig, ax = plt.subplots()
    #                 dfcat=df[[col]].copy()
    #                 classes=dfcat[col].value_counts()[10:].index.astype(str).tolist()
    #                 dfcat[col]=dfcat[col].replace((classes),('Others'))
    #                 dfcat = pd.DataFrame(dfcat.groupby(col).agg('size')).reset_index().rename(columns={0:'count'}).sort_values('count',ascending=False).reset_index(drop=True)

    #                 fig = px.bar(dfcat, y = col, x = 'count', text_auto=True,color='count').update_yaxes(categoryorder='min ascending')
    #                 fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    #                 fig.update_layout(
    #                         autosize=False,
    #                         width=500,
    #                         height=100
    #                     )
    #                 #fig.update_layout(
    #                         #yaxis_title_text=dfcat[col].name)
    #                 fig.update_layout(title_text=f"count plot of {df[col].name}",title={
    #                                     'y':0.9,
    #                                     'x':0.5,
    #                                     'xanchor': 'center',
    #                                     'yanchor': 'top'},title_font_color="red")

    #                 st.plotly_chart(fig)


                else :# df[col].nunique() > 20 :
                    if df[col].nunique() > 20:
                        st.write(f'**<FONT color="#FC7726">Top 10 Categories</FONT>**',unsafe_allow_html=True)
                    fig, ax = plt.subplots()
                    dfcat=df[[col]].copy()
                    classes=dfcat[col].value_counts()[10:].index.astype(str).tolist()
                    dfcat[col]=dfcat[col].replace((classes),('Others'))
                    dfcat = pd.DataFrame(dfcat.groupby(col).agg('size')).reset_index().rename(columns={0:'count'}).sort_values('count',ascending=False).reset_index(drop=True)

                    fig = px.bar(dfcat, y = col, x = 'count', text_auto=True,color='count').update_yaxes(categoryorder='min ascending')
                    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

    #                 dfcat=df.copy()
    #                 classes=dfcat[col].value_counts()[10:].index.astype(str).tolist()
    #                 dfcat[col]=dfcat[col].replace((classes),('Others'))
    #                 fig = px.histogram(y=dfcat[col].astype(str)).update_yaxes(categoryorder='min ascending')


    # #                         fig = plt.figure(figsize=(15,15))
    #                         valu=df[col].value_counts()[0:10].values.tolist()
    #                         valu.append(df[col].value_counts()[10:-1].values.sum())
    #                         classes=df[col].value_counts()[0:10].index.astype(str).tolist()
    #                         classes.append('Others')
    #                         ax1=sns.barplot(valu,classes);
    #                         for p in ax1.patches:
    #                             ax1.annotate(int(p.get_width()),
    #                     ((p.get_y() + p.get_width()), p.get_y()), 
    #                     xytext=(2, -30),fontsize=15,
    #                     rotation=0,
    #                     textcoords='offset points', 
    #                     horizontalalignment='left')
    #                         total = len(df[col].dropna())
    #                         for p in ax1.patches:
    #                             percentage = '{:.1f}%'.format(100 * p.get_width()/total)
    #                             x = p.get_x() + p.get_width() + 0.02
    #                             y = p.get_y() + p.get_height()/1.2
    #                             ax1.annotate(percentage, (x, y),fontsize=15)
    #                         plt.margins(x=0.15)
    #                         plt.xlabel('count',fontsize=30)
    #                         title = "Count Plot of {}"
    #                         plt.title(title.format(df[col].name),fontsize=30)
    #                         plt.xticks(fontsize=15)
    #                         plt.yticks(fontsize=15)
    ##                         st.pyplot(fig)

    #######                         fig = px.histogram(x=valu,y=classes).update_yaxes(categoryorder='total ascending')
                    fig.update_layout(
                            autosize=False,
                            width=500,
                            height=500
                        )
                    #fig.update_layout(
                            #yaxis_title_text=dfcat[col].name)
                    fig.update_layout(title_text=f"count plot of {df[col].name}",title={
                                        'y':0.9,
                                        'x':0.5,
                                        'xanchor': 'center',
                                        'yanchor': 'top'},title_font_color="red")

                    st.plotly_chart(fig)

                if 1 < df[col].nunique() <=20:
                    st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Number of Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{df[col].nunique()}</FONT>**',unsafe_allow_html=True)
                    lis2=' ‎ ‎,‎ ‎ '.join(df[col].unique().astype(str))
                    st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{lis2}</FONT>**',unsafe_allow_html=True)

                    a = df[col].value_counts()
                    catob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observation :</p>'
                    st.markdown(f"**{catob}**", unsafe_allow_html=True)      

                    if len(a.index) == 2:
                        if a.index[0]=='NaN':
                            st.write(f"- **count of {df[col].name} {a.index[-1]} is  :{a.values[-1]}**")
                        elif a.index[-1]=='NaN':
                            st.write(f"- **count of {df[col].name} {a.index[0]} is  :{a.values[0]}**")
                        elif (a.index[0]!='NaN') and (a.index[1]!='NaN'):
                            st.write(f"- **count of {df[col].name} {a.index[0]} is more in the data around :{a.values[0]}**")
                            st.write(f"- **count of {df[col].name} {a.index[1]} is less in the data around :{a.values[1]}**")

                    elif len(a.index)>2:
                        if a.index[0] == 'NaN':
                            st.write(f"- **count of {df[col].name} {a.index[1]} is more in the data around :{a.values[1]}**")
                        else:
                            st.write(f"- **count of {df[col].name} {a.index[0]} is more in the data around :{a.values[0]}**")

                        if a.index[-1] == 'NaN':
                            if a.index[0]!= a.index[-2]:
                                st.write(f"- **count of {df[col].name} {a.index[-2]} is less in the data around :{a.values[-2]}**")
                        else:
                            st.write(f"- **count of {df[col].name} {a.index[-1]} is less in the data around :{a.values[-1]}**")


                elif df[col].nunique()==1:
                    st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Number of Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{df[col].nunique()}</FONT>**',unsafe_allow_html=True)
                    lis2=' ‎ ‎,‎ ‎ '.join(df[col].unique().astype(str))
                    st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{lis2}</FONT>**',unsafe_allow_html=True)

                    a = df[col].value_counts()
                    catob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observation :</p>'
                    st.markdown(f"**{catob}**", unsafe_allow_html=True)
                    st.write(f"- **count of {df[col].name} {a.index[0]} is  :{a.values[0]}**")

                else:
                    st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Number of Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{df[col].nunique()}</FONT>**',unsafe_allow_html=True)
                    lis2=' ‎ ‎,‎ ‎ '.join(df[col].value_counts()[0:20].index.astype(str))
                    st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Top 20 Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{lis2}</FONT>**',unsafe_allow_html=True)

                    a = df[col].value_counts()
                    catob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observation :</p>'
                    st.markdown(f"**{catob}**", unsafe_allow_html=True)

                    if a.index[0] == 'NaN':
                        st.write(f"- **count of {df[col].name} {a.index[1]} is more in the data around :{a.values[1]}**")
                    else:
                        st.write(f"- **count of {df[col].name} {a.index[0]} is more in the data around :{a.values[0]}**")

                    if a.index[-1] == 'NaN':
                        st.write(f"- **count of {df[col].name} {a.index[-2]} is less in the data around :{a.values[-2]}**")
                    else:
                        st.write(f"- **count of {df[col].name} {a.index[-1]} is less in the data around :{a.values[-1]}**")

                with rowcat2:
                    new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 16px;">{df[col].name} </p>'
                    st.markdown(f"**<h1 style='text-align: left; '>{new_title}</h1>**", unsafe_allow_html=True)

                    hide_table_row_uvcat = """
                        <style>
                        tbody th {display:none}
                        .blank {display:none}
                        </style>
                        """
                    # Inject CSS with Markdown
                    st.markdown(hide_table_row_uvcat, unsafe_allow_html=True)
                    categories1 = df[col].value_counts().index.tolist()
                    count1 = df[col].value_counts().values.tolist()

                    frequency1 = (df[col].value_counts(normalize=True)*100).values.tolist()
                    df3=pd.DataFrame({'CATEGORIES':categories1,'COUNT':count1,'FREQUENCY %':np.round(frequency1,2)})
                    df2=df3[df3['CATEGORIES']==category]
                    if df[col].nunique() > 20:
                        mul_button = st.radio("",options = ['Top 10 Categories','Bottom 10 Categories'])
                        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
                    st.write(f'**<FONT color="#FC7726">Considering‎ ‎ {category}‎ ‎ Category</FONT>**',unsafe_allow_html=True)
                    st.table(df2.style.set_precision(2).set_table_styles(styles))
                    if df[col].nunique()<=20: 
                        categories = df[col].value_counts().index.tolist()
                        count = df[col].value_counts().values.tolist()

                        frequency = (df[col].value_counts(normalize=True)*100).values.tolist()
                        df1=pd.DataFrame({'CATEGORIES':categories,'COUNT':count,'FREQUENCY %':np.round(frequency,2)})
                        df1.loc[len(df1.index)] = ['Total (sum)',df1['COUNT'].sum(),100.00]
                        #st.table(df1)

                        st.table(df1.style.set_precision(2).set_table_styles(styles))

                        values=df[col].value_counts()
                        labels=df[col].value_counts().index.tolist()
                        fig1, ax1 = plt.subplots()
                        fig1=go.Figure(data=[go.Pie(values=values,labels=labels)])
                        fig1.update_layout(title_text=f"Pie Chart of {df[col].name}",title={
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},title_font_color="#1F30CB")
                        st.plotly_chart(fig1)

                    else:
                        if mul_button == 'Top 10 Categories' :
                            categories = df[col].value_counts()[0:10].index.tolist()
                            categories.append('Others')
                            count = df[col].value_counts()[0:10].values.tolist()
                            count.append(df[col].value_counts()[10:].sum())
                            frequency=(df[col].value_counts(normalize=True)*100)[0:10].values.tolist()
                            frequency.append((df[col].value_counts(normalize=True)*100)[10:-1].values.sum())
                            df1=pd.DataFrame({'CATEGORIES':categories,'COUNT':count,'FREQUENCY %':np.round(frequency,2)})
                            df1.loc[len(df1.index)] = ['Total (sum)',df1['COUNT'].sum(),100.00]
                            st.write(f'**<FONT color="#FC7726">Top 10 Categories</FONT>**',unsafe_allow_html=True)
                            st.table(df1.style.set_precision(2).set_table_styles(styles))

                        elif mul_button == 'Bottom 10 Categories' :
                            categories = df[col].value_counts()[-10:].index.tolist()
                            categories.append('Others')
                            count = df[col].value_counts()[-10:].values.tolist()
                            count.append(df[col].value_counts()[0:-10].sum())
                            frequency=(df[col].value_counts(normalize=True)*100)[-10:].values.tolist()
                            frequency.append((df[col].value_counts(normalize=True)*100)[0:-10].values.sum())
                            df1=pd.DataFrame({'CATEGORIES':categories,'COUNT':count,'FREQUENCY %':np.round(frequency,2)})
                            df1.loc[len(df1.index)] = ['Total (sum)',df1['COUNT'].sum(),100.00]
                            st.write(f'**<FONT color="#FC7726">Bottom 10 Categories</FONT>**',unsafe_allow_html=True)
                            st.table(df1.style.set_precision(2).set_table_styles(styles))

                        values=df[col].value_counts()[0:10].values.tolist()
                        values.append(df[col].value_counts()[10:].values.sum())
                        labels=df[col].value_counts()[0:10].index.tolist()
                        labels.append('Others')
                        fig1, ax1 = plt.subplots()
                        fig1=go.Figure(data=[go.Pie(values=values,labels=labels)])
                        fig1.update_layout(title_text=f"Pie Chart of {df[col].name}",title={
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},title_font_color="#1F30CB")
                        st.plotly_chart(fig1)
            else:
                with rowcat2:
                    st.write("##")
                    st.warning("**SELECT CATEGORICAL VARIABLE**")

        colcat1=[]
        for i in df:            
            if df[i].dtypes == "object" :
                colcat1.append(df[i].name)

            if df[i].dtypes != "object" :
                if df[i].nunique() <=5 :
                    colcat1.append(df[i].name)    
        st.write("##")
        
        if st.checkbox("Select Multiple Categorical Variables"):
            form1 = st.form(key = 'Options')
            
            if len(colcat1)<=10:            
                all = st.checkbox("Select all Categorical Variables ")
                if all:
                    selected_options = form1.multiselect("Select one or more Variables:",colcat1,colcat1)
                else:
                    selected_options =  form1.multiselect("Select one or more Variables:",colcat1)                  
            else:
                selected_options =  form1.multiselect("Select one or more Variables (max 10):",colcat1)[0:10]
                
            if "load_statef" not in st.session_state:
                st.session_state.load_statef = False  

            if form1.form_submit_button("Submit") or st.session_state.load_statef:
                st.session_state.load_statef = True
                for col in selected_options:
                    df[col] = df[col].fillna('NaN').astype(str)
                    #col_button = st.radio("",options = [f'{df[col].name}'])
                    if df[col].nunique()<=20:
                        rowcat1,rowcatsp, rowcat2,rowcatsp1  = st.columns((1.5,.5,2,.2))
                        with rowcat1:
                            st.write("##")
                            st.write("")
                            categories = df[col].value_counts().index.tolist()
                            count = df[col].value_counts().values.tolist()
                            frequency = (df[col].value_counts(normalize=True)*100).values.tolist()
                            df1=pd.DataFrame({'CATEGORIES':categories,'COUNT':count,'FREQUENCY %':np.round(frequency,2)})
                            df1.loc[len(df1.index)] = ['Total (sum)',df1['COUNT'].sum(),100.00]
                            warnings.filterwarnings(action="ignore")
                            #plt.rcdefaults()
                            fig, ax = plt.subplots()
#                                     fig = plt.figure(figsize=(15,df[col].nunique()*1.8))
#                                     ax1=sns.barplot(df[col].value_counts().values,(df[col].value_counts().index).astype(str));
#                                     for p in ax1.patches:
#                                         ax1.annotate(int(p.get_width()),
#                                 ((p.get_y() + p.get_width()), p.get_y()), 
#                                 xytext=(2, -30),fontsize=22,
#                                 rotation=0,
#                                 textcoords='offset points', 
#                                 horizontalalignment='left')
#                                     total = len(df[col].dropna())
#                                     for p in ax1.patches:
#                                         percentage = '{:.1f}%'.format(100 * p.get_width()/total)
#                                         x = p.get_x() + p.get_width() + 0.02
#                                         y = p.get_y() + p.get_height()/1.2
#                                         ax1.annotate(percentage, (x, y),fontsize=22)
#                                     plt.margins(x=0.15)
#                                     plt.xlabel('count',fontsize=30)
#                                     title = "Count Plot of {}"
#                                     plt.title(title.format(df[col].name),fontsize=30)
#                                     plt.xticks(fontsize=25)
#                                     plt.yticks(fontsize=25)
#                                     st.pyplot(fig)

                            #fig = px.histogram(y=df[col].astype(str)).update_yaxes(categoryorder='total ascending')
                            dfcat = pd.DataFrame(df[[col]].dropna().astype(str).groupby(col).agg('size')).reset_index().rename(columns={0:'count'}).sort_values('count',ascending=False).reset_index(drop=True)
                
                            fig = px.bar(dfcat, y = col, x = 'count', text_auto=True,color='count',title=f"count plot of {df[col].name}").update_yaxes(categoryorder='min ascending')
                            fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

                            if df[col].nunique()<=2:

                                fig.update_layout(
                                    autosize=False,
                                    width=500,
                                    height=df[col].nunique()*150,#df2[x].nunique()
                                )

                            elif df[col].nunique()>=3 and df[col].nunique()<=5:
                                fig.update_layout(
                                    autosize=False,
                                    width=500,
                                    height=df[col].nunique()*100,#df2[x].nunique()
                                )
                                
                            elif df[col].nunique()>5 and df[col].nunique()<=10:
                                fig.update_layout(
                                    autosize=False,
                                    width=500,
                                    height=df[col].nunique()*70,#df2[x].nunique()
                                )

                            else:
                                fig.update_layout(
                                    autosize=False,
                                    width=500,
                                    height=df[col].nunique()*45,#df2[x].nunique()
                                )
                            fig.update_layout(title_text=f"count plot of {df[col].name}",title={
                                                'y':0.9,
                                                'x':0.5,
                                                'xanchor': 'center',
                                                'yanchor': 'top'},title_font_color="red")
                            fig.update_layout(
                        yaxis_title_text=df[col].name)
                            st.plotly_chart(fig)

                            st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Number of Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{df[col].nunique()}</FONT>**',unsafe_allow_html=True)
                            lis2=' ‎ ‎,‎ ‎ '.join(df[col].unique().astype(str))
                            st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{lis2}</FONT>**',unsafe_allow_html=True)

                            a = df[col].value_counts()
                            catob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observation :</p>'
                            st.markdown(f"**{catob}**", unsafe_allow_html=True)
                            
                            if len(a.index) == 2:
                                if a.index[0]=='NaN':
                                    st.write(f"- **count of {df[col].name} {a.index[-1]} is  :{a.values[-1]}**")
                                elif a.index[-1]=='NaN':
                                    st.write(f"- **count of {df[col].name} {a.index[0]} is  :{a.values[0]}**")
                                elif (a.index[0]!='NaN') and (a.index[1]!='NaN'):
                                    st.write(f"- **count of {df[col].name} {a.index[0]} is more in the data around :{a.values[0]}**")
                                    st.write(f"- **count of {df[col].name} {a.index[1]} is less in the data around :{a.values[1]}**")
                                    
                            elif len(a.index) == 1:
                                st.write(f"- **count of {df[col].name} {a.index[0]} is  :{a.values[0]}**")

                            elif len(a.index)>2:
                                if a.index[0] == 'NaN':
                                    st.write(f"- **count of {df[col].name} {a.index[1]} is more in the data around :{a.values[1]}**")
                                else:
                                    st.write(f"- **count of {df[col].name} {a.index[0]} is more in the data around :{a.values[0]}**")

                                if a.index[-1] == 'NaN':
                                    #if a.index[0]!= a.index[-2]:
                                    st.write(f"- **count of {df[col].name} {a.index[-2]} is less in the data around :{a.values[-2]}**")
                                else:
                                    st.write(f"- **count of {df[col].name} {a.index[-1]} is less in the data around :{a.values[-1]}**")

                        with rowcat2:
                            new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 16px;">{df[col].name} </p>'
                            st.markdown(f"**<h1 style='text-align: left; '>{new_title}</h1>**", unsafe_allow_html=True)

                            hide_table_row_uvcat = """
                                <style>
                                tbody th {display:none}
                                .blank {display:none}
                                </style>
                                """
                            # Inject CSS with Markdown
                            st.markdown(hide_table_row_uvcat, unsafe_allow_html=True)
                            st.table(df1.style.set_precision(2).set_table_styles(styles))
                            values=df[col].value_counts()
                            labels=df[col].value_counts().index.tolist()

                            fig1, ax1 = plt.subplots()
                            fig1=go.Figure(data=[go.Pie(values=values,labels=labels)])
                            fig1.update_layout(title_text=f"Pie Chart of {df[col].name}",title={
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},title_font_color="#1F30CB")
                            st.plotly_chart(fig1)
                        st.write("*-"*280)

                    else:
                        rowcat1,rowcatsp, rowcat2,rowcatsp1  = st.columns((1.5,.5,2,.2))
                        with rowcat1:
                            st.write("##")
                            st.write("##")
                            st.write("")
                            fig, ax = plt.subplots()
                            #fig = plt.figure(figsize=(15,20*1))
                            
                            dfcat=df[[col]].copy()
                            classes=dfcat[col].value_counts()[10:].index.astype(str).tolist()
                            dfcat[col]=dfcat[col].replace((classes),('Others'))
                            dfcat = pd.DataFrame(dfcat.groupby(col).agg('size')).reset_index().rename(columns={0:'count'}).sort_values('count',ascending=False).reset_index(drop=True)

                            fig = px.bar(dfcat, y = col, x = 'count', text_auto=True,color='count').update_yaxes(categoryorder='min ascending')
                            fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
                                                     
                            
#                             dfcat=df.copy()
#                             classes=dfcat[col].value_counts()[10:].index.astype(str).tolist()
#                             dfcat[col]=dfcat[col].replace((classes),('Others'))
#                             fig = px.histogram(y=dfcat[col].astype(str)).update_yaxes(categoryorder='min ascending')

#                                     ax1=sns.barplot(valu,classes);
#                                     for p in ax1.patches:
#                                         ax1.annotate(int(p.get_width()),
#                                 ((p.get_y() + p.get_width()), p.get_y()), 
#                                 xytext=(2, -30),fontsize=22,
#                                 rotation=0,
#                                 textcoords='offset points', 
#                                 horizontalalignment='left')
#                                     total = len(df[col].dropna())
#                                     for p in ax1.patches:
#                                         percentage = '{:.1f}%'.format(100 * p.get_width()/total)
#                                         x = p.get_x() + p.get_width() + 0.02
#                                         y = p.get_y() + p.get_height()/1.2
#                                         ax1.annotate(percentage, (x, y),fontsize=22)
#                                     plt.margins(x=0.15)
#                                     #else:
#                                     plt.xlabel('count',fontsize=30)
#                                     title = "Count Plot of {}"
#                                     plt.title(title.format(df[col].name),fontsize=30)
#                                     plt.xticks(fontsize=25)
#                                     plt.yticks(fontsize=25)
#                                     st.pyplot(fig)
                            #fig = px.histogram(x=valu,y=classes).update_yaxes(categoryorder='total ascending')
                            fig.update_layout(
                                    autosize=False,
                                    width=500,
                                    height=500
                                )
                            fig.update_layout(title_text=f"count plot of {df[col].name}",title={
                                                'y':0.9,
                                                'x':0.5,
                                                'xanchor': 'center',
                                                'yanchor': 'top'},title_font_color="red")
#                             fig.update_layout(
#                         yaxis_title_text=dfcat[col].name)

                            st.write(f'**<FONT color="#FC7726">Top 10 Categories</FONT>**',unsafe_allow_html=True)
                            st.plotly_chart(fig)
                            st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Number of Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{df[col].nunique()}</FONT>**',unsafe_allow_html=True)
                            lis2=' ‎ ‎,‎ ‎ '.join(df[col].value_counts()[0:20].index.astype(str))
                            st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Top 20 Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{lis2}</FONT>**',unsafe_allow_html=True)
                            a = df[col].value_counts()
                            catob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observation :</p>'
                            st.markdown(f"**{catob}**", unsafe_allow_html=True)
                            
                            if a.index[0] == 'NaN':
                                st.write(f"- **count of {df[col].name} {a.index[1]} is more in the data around :{a.values[1]}**")
                            else:
                                st.write(f"- **count of {df[col].name} {a.index[0]} is more in the data around :{a.values[0]}**")

                            if a.index[-1] == 'NaN':
                                if a.index[0]!= a.index[-2]:
                                    st.write(f"- **count of {df[col].name} {a.index[-2]} is less in the data around :{a.values[-2]}**")
                            else:
                                st.write(f"- **count of {df[col].name} {a.index[-1]} is less in the data around :{a.values[-1]}**")

                        with rowcat2:
                            new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 16px;">{df[col].name} </p>'
                            st.markdown(f"**<h1 style='text-align: left; '>{new_title}</h1>**", unsafe_allow_html=True)

                            hide_table_row_uvcat = """
                                <style>
                                tbody th {display:none}
                                .blank {display:none}
                                </style>
                                """
                            # Inject CSS with Markdown
                            st.markdown(hide_table_row_uvcat, unsafe_allow_html=True)
                            categories = df[col].value_counts()[0:10].index.tolist()
                            categories.append('Others')
                            count = df[col].value_counts()[0:10].values.tolist()
                            count.append(df[col].value_counts()[10:].sum())
                            frequency=(df[col].value_counts(normalize=True)*100)[0:10].values.tolist()
                            frequency.append((df[col].value_counts(normalize=True)*100)[10:-1].values.sum())
                            df1=pd.DataFrame({'CATEGORIES':categories,'COUNT':count,'FREQUENCY %':np.round(frequency,2)})
                            df1.loc[len(df1.index)] = ['Total (sum)',df1['COUNT'].sum(),100.00]
                            st.write("##")
                            st.write(f'**<FONT color="#FC7726">Top 10 Categories</FONT>**',unsafe_allow_html=True)
                            st.table(df1.style.set_precision(2).set_table_styles(styles))

                            values=df[col].value_counts()[0:10].values.tolist()
                            values.append(df[col].value_counts()[10:].values.sum())
                            labels=df[col].value_counts()[0:10].index.tolist()
                            labels.append('Others')
                            fig1, ax1 = plt.subplots()
                            fig1=go.Figure(data=[go.Pie(values=values,labels=labels)])
                            fig1.update_layout(title_text=f"Pie Chart of {df[col].name}",title={
                                'y':0.9,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'},title_font_color="#1F30CB")
                            st.plotly_chart(fig1)
                        st.write("*-"*280)

    else:
        st.warning("**NO CATEGORICAL VARIABLE AVAILABLE**")
        
        
def Univariate_Categorical_full(df):
    catg = f'<p style="font-family:sans-serif; font-size: 18px;">Univariate Categorical</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{catg}</h1>**", unsafe_allow_html=True)
    colcat=[]
    for i in df:
        if df[i].dtypes == "object" :
            if df[i].nunique()>0:
                colcat.append(df[i].name)

        if df[i].dtypes != "object" :
            if df[i].nunique() > 0 and df[i].nunique() <=5 :
                colcat.append(df[i].name)
    if len(colcat)>0:
        for col in colcat:
            df[col] = df[col].fillna('NaN').astype(str)
            #col_button = st.radio("",options = [f'{df[col].name}'])
            if df[col].nunique()<=20:
                rowcat1,rowcatsp, rowcat2,rowcatsp1  = st.columns((1.5,.5,2,.2))
                with rowcat1:
                    st.write("##")
                    st.write("")
                    categories = df[col].value_counts().index.tolist()
                    count = df[col].value_counts().values.tolist()
                    frequency = (df[col].value_counts(normalize=True)*100).values.tolist()
                    df1=pd.DataFrame({'CATEGORIES':categories,'COUNT':count,'FREQUENCY %':np.round(frequency,2)})
                    df1.loc[len(df1.index)] = ['Total (sum)',df1['COUNT'].sum(),100.00]
                    warnings.filterwarnings(action="ignore")
                    #plt.rcdefaults()
                    fig, ax = plt.subplots()
#                                     fig = plt.figure(figsize=(15,df[col].nunique()*1.8))
#                                     ax1=sns.barplot(df[col].value_counts().values,(df[col].value_counts().index).astype(str));
#                                     for p in ax1.patches:
#                                         ax1.annotate(int(p.get_width()),
#                                 ((p.get_y() + p.get_width()), p.get_y()), 
#                                 xytext=(2, -30),fontsize=22,
#                                 rotation=0,
#                                 textcoords='offset points', 
#                                 horizontalalignment='left')
#                                     total = len(df[col].dropna())
#                                     for p in ax1.patches:
#                                         percentage = '{:.1f}%'.format(100 * p.get_width()/total)
#                                         x = p.get_x() + p.get_width() + 0.02
#                                         y = p.get_y() + p.get_height()/1.2
#                                         ax1.annotate(percentage, (x, y),fontsize=22)
#                                     plt.margins(x=0.15)
#                                     plt.xlabel('count',fontsize=30)
#                                     title = "Count Plot of {}"
#                                     plt.title(title.format(df[col].name),fontsize=30)
#                                     plt.xticks(fontsize=25)
#                                     plt.yticks(fontsize=25)
#                                     st.pyplot(fig)

                    #fig = px.histogram(y=df[col].astype(str)).update_yaxes(categoryorder='total ascending')
                    dfcat = pd.DataFrame(df[[col]].dropna().astype(str).groupby(col).agg('size')).reset_index().rename(columns={0:'count'}).sort_values('count',ascending=False).reset_index(drop=True)

                    fig = px.bar(dfcat, y = col, x = 'count', text_auto=True,color='count',title=f"count plot of {df[col].name}").update_yaxes(categoryorder='min ascending')
                    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

                    if df[col].nunique()<=2:

                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df[col].nunique()*150,#df2[x].nunique()
                        )

                    elif df[col].nunique()>=3 and df[col].nunique()<=5:
                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df[col].nunique()*100,#df2[x].nunique()
                        )

                    elif df[col].nunique()>5 and df[col].nunique()<=10:
                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df[col].nunique()*70,#df2[x].nunique()
                        )

                    else:
                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df[col].nunique()*45,#df2[x].nunique()
                        )
                    fig.update_layout(title_text=f"count plot of {df[col].name}",title={
                                        'y':0.9,
                                        'x':0.5,
                                        'xanchor': 'center',
                                        'yanchor': 'top'},title_font_color="red")
                    fig.update_layout(
                yaxis_title_text=df[col].name)
                    st.plotly_chart(fig)

                    st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Number of Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{df[col].nunique()}</FONT>**',unsafe_allow_html=True)
                    lis2=' ‎ ‎,‎ ‎ '.join(df[col].unique().astype(str))
                    st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{lis2}</FONT>**',unsafe_allow_html=True)

                    a = df[col].value_counts()
                    catob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observation :</p>'
                    st.markdown(f"**{catob}**", unsafe_allow_html=True)

                    if len(a.index) == 2:
                        if a.index[0]=='NaN':
                            st.write(f"- **count of {df[col].name} {a.index[-1]} is  :{a.values[-1]}**")
                        elif a.index[-1]=='NaN':
                            st.write(f"- **count of {df[col].name} {a.index[0]} is  :{a.values[0]}**")
                        elif (a.index[0]!='NaN') and (a.index[1]!='NaN'):
                            st.write(f"- **count of {df[col].name} {a.index[0]} is more in the data around :{a.values[0]}**")
                            st.write(f"- **count of {df[col].name} {a.index[1]} is less in the data around :{a.values[1]}**")

                    elif len(a.index) == 1:
                        st.write(f"- **count of {df[col].name} {a.index[0]} is  :{a.values[0]}**")

                    elif len(a.index)>2:
                        if a.index[0] == 'NaN':
                            st.write(f"- **count of {df[col].name} {a.index[1]} is more in the data around :{a.values[1]}**")
                        else:
                            st.write(f"- **count of {df[col].name} {a.index[0]} is more in the data around :{a.values[0]}**")

                        if a.index[-1] == 'NaN':
                            #if a.index[0]!= a.index[-2]:
                            st.write(f"- **count of {df[col].name} {a.index[-2]} is less in the data around :{a.values[-2]}**")
                        else:
                            st.write(f"- **count of {df[col].name} {a.index[-1]} is less in the data around :{a.values[-1]}**")

                with rowcat2:
                    new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 16px;">{df[col].name} </p>'
                    st.markdown(f"**<h1 style='text-align: left; '>{new_title}</h1>**", unsafe_allow_html=True)

                    hide_table_row_uvcat = """
                        <style>
                        tbody th {display:none}
                        .blank {display:none}
                        </style>
                        """
                    # Inject CSS with Markdown
                    st.markdown(hide_table_row_uvcat, unsafe_allow_html=True)
                    st.table(df1.style.set_precision(2).set_table_styles(styles))
                    values=df[col].value_counts()
                    labels=df[col].value_counts().index.tolist()

                    fig1, ax1 = plt.subplots()
                    fig1=go.Figure(data=[go.Pie(values=values,labels=labels)])
                    fig1.update_layout(title_text=f"Pie Chart of {df[col].name}",title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},title_font_color="#1F30CB")
                    st.plotly_chart(fig1)
                st.write("*-"*280)

            else:
                rowcat1,rowcatsp, rowcat2,rowcatsp1  = st.columns((1.5,.5,2,.2))
                with rowcat1:
                    st.write("##")
                    st.write("##")
                    st.write("")
                    fig, ax = plt.subplots()
                    #fig = plt.figure(figsize=(15,20*1))

                    dfcat=df[[col]].copy()
                    classes=dfcat[col].value_counts()[10:].index.astype(str).tolist()
                    dfcat[col]=dfcat[col].replace((classes),('Others'))
                    dfcat = pd.DataFrame(dfcat.groupby(col).agg('size')).reset_index().rename(columns={0:'count'}).sort_values('count',ascending=False).reset_index(drop=True)

                    fig = px.bar(dfcat, y = col, x = 'count', text_auto=True,color='count').update_yaxes(categoryorder='min ascending')
                    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)


#                             dfcat=df.copy()
#                             classes=dfcat[col].value_counts()[10:].index.astype(str).tolist()
#                             dfcat[col]=dfcat[col].replace((classes),('Others'))
#                             fig = px.histogram(y=dfcat[col].astype(str)).update_yaxes(categoryorder='min ascending')

#                                     ax1=sns.barplot(valu,classes);
#                                     for p in ax1.patches:
#                                         ax1.annotate(int(p.get_width()),
#                                 ((p.get_y() + p.get_width()), p.get_y()), 
#                                 xytext=(2, -30),fontsize=22,
#                                 rotation=0,
#                                 textcoords='offset points', 
#                                 horizontalalignment='left')
#                                     total = len(df[col].dropna())
#                                     for p in ax1.patches:
#                                         percentage = '{:.1f}%'.format(100 * p.get_width()/total)
#                                         x = p.get_x() + p.get_width() + 0.02
#                                         y = p.get_y() + p.get_height()/1.2
#                                         ax1.annotate(percentage, (x, y),fontsize=22)
#                                     plt.margins(x=0.15)
#                                     #else:
#                                     plt.xlabel('count',fontsize=30)
#                                     title = "Count Plot of {}"
#                                     plt.title(title.format(df[col].name),fontsize=30)
#                                     plt.xticks(fontsize=25)
#                                     plt.yticks(fontsize=25)
#                                     st.pyplot(fig)
                    #fig = px.histogram(x=valu,y=classes).update_yaxes(categoryorder='total ascending')
                    fig.update_layout(
                            autosize=False,
                            width=500,
                            height=500
                        )
                    fig.update_layout(title_text=f"count plot of {df[col].name}",title={
                                        'y':0.9,
                                        'x':0.5,
                                        'xanchor': 'center',
                                        'yanchor': 'top'},title_font_color="red")
#                             fig.update_layout(
#                         yaxis_title_text=dfcat[col].name)

                    st.write(f'**<FONT color="#FC7726">Top 10 Categories</FONT>**',unsafe_allow_html=True)
                    st.plotly_chart(fig)
                    st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Number of Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{df[col].nunique()}</FONT>**',unsafe_allow_html=True)
                    lis2=' ‎ ‎,‎ ‎ '.join(df[col].value_counts()[0:20].index.astype(str))
                    st.write(f'**<FONT color="#FC7726">►‎ ‎ ‎ ‎ Top 20 Unique values of {df[col].name} :‎ ‎</FONT>**',f'**<FONT color="steelblue">{lis2}</FONT>**',unsafe_allow_html=True)
                    a = df[col].value_counts()
                    catob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observation :</p>'
                    st.markdown(f"**{catob}**", unsafe_allow_html=True)

                    if a.index[0] == 'NaN':
                        st.write(f"- **count of {df[col].name} {a.index[1]} is more in the data around :{a.values[1]}**")
                    else:
                        st.write(f"- **count of {df[col].name} {a.index[0]} is more in the data around :{a.values[0]}**")

                    if a.index[-1] == 'NaN':
                        if a.index[0]!= a.index[-2]:
                            st.write(f"- **count of {df[col].name} {a.index[-2]} is less in the data around :{a.values[-2]}**")
                    else:
                        st.write(f"- **count of {df[col].name} {a.index[-1]} is less in the data around :{a.values[-1]}**")

                with rowcat2:
                    new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 16px;">{df[col].name} </p>'
                    st.markdown(f"**<h1 style='text-align: left; '>{new_title}</h1>**", unsafe_allow_html=True)

                    hide_table_row_uvcat = """
                        <style>
                        tbody th {display:none}
                        .blank {display:none}
                        </style>
                        """
                    # Inject CSS with Markdown
                    st.markdown(hide_table_row_uvcat, unsafe_allow_html=True)
                    categories = df[col].value_counts()[0:10].index.tolist()
                    categories.append('Others')
                    count = df[col].value_counts()[0:10].values.tolist()
                    count.append(df[col].value_counts()[10:].sum())
                    frequency=(df[col].value_counts(normalize=True)*100)[0:10].values.tolist()
                    frequency.append((df[col].value_counts(normalize=True)*100)[10:-1].values.sum())
                    df1=pd.DataFrame({'CATEGORIES':categories,'COUNT':count,'FREQUENCY %':np.round(frequency,2)})
                    df1.loc[len(df1.index)] = ['Total (sum)',df1['COUNT'].sum(),100.00]
                    st.write("##")
                    st.write(f'**<FONT color="#FC7726">Top 10 Categories</FONT>**',unsafe_allow_html=True)
                    st.table(df1.style.set_precision(2).set_table_styles(styles))

                    values=df[col].value_counts()[0:10].values.tolist()
                    values.append(df[col].value_counts()[10:].values.sum())
                    labels=df[col].value_counts()[0:10].index.tolist()
                    labels.append('Others')
                    fig1, ax1 = plt.subplots()
                    fig1=go.Figure(data=[go.Pie(values=values,labels=labels)])
                    fig1.update_layout(title_text=f"Pie Chart of {df[col].name}",title={
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},title_font_color="#1F30CB")
                    st.plotly_chart(fig1)
                st.write("*-"*280)

    else:
        st.warning("**NO CATEGORICAL VARIABLE AVAILABLE**")
                
        
def Line_Plot(df):
    #df.dropna(inplace=True)
    new_title = f'<p style="font-family:sans-serif; font-size: 18px;">Line Plot</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)
    st.write('##')
    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if (df[i].nunique()) >5 :
                colnum.append(df[i].name)
    rowscat1,rowscatsp, rowscat2  = st.columns((1,0.1,4))
    if len(colnum)>0:
        with rowscat1:
            line = st.form(key = 'Options')
            x = line.multiselect("Select One or More Continuous Variables",colnum)
            time = df.columns.tolist()
            y = line.selectbox("Time Stamped Variable",time)
            submit_button_l = line.form_submit_button(label='Submit')
        with rowscat2:
            mul_button = st.radio("",options = ['Head of Dataset','Tail of Dataset'])
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
            if mul_button=='Head of Dataset':
                st.table(df.head(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            elif mul_button=='Tail of Dataset':
                st.table(df.tail(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            
            if "load_stateline" not in st.session_state:
                st.session_state.load_stateline = False  
            
            if submit_button_l or st.session_state.load_stateline:
                st.session_state.load_stateline = True
                if x:
                    df.Timestamp = pd.to_datetime(df[y].astype(str),infer_datetime_format=True) 
                    df.index = df.Timestamp
                    df.sort_index(axis = 0,inplace=True)
                    with rowscat1:
                        l = pd.DataFrame(df.index.to_list())
                        l[0] = l[0].astype(str)
                        time_list = l[0].unique().tolist()
                        time_list.insert(0,'None')
                        time_list1 = l[0].unique().tolist()
                        time_list1.reverse()
                        time_list1.insert(0,'None')
                        line2 = st.form(key = 'Options2')
                        up = line2.selectbox("start",time_list)
                        lo = line2.selectbox("end",time_list1)
                        submit_button_l2 = line2.form_submit_button(label='Select Date Time Range')

                    if len(x) == 1:
                        if submit_button_l2 or st.session_state.load_stateline:
                            st.session_state.load_stateline = True
                            if (up!='None') and (lo!='None'):
                                df = df.loc[up:lo]
                            else:
                                df=df
                        else:
                            df= df
                        fig = px.line(df, x=df.index, y=x)
                        fig.update_layout(xaxis_title=f"{y}",yaxis_title=f"{x[0]}")
                        fig.update_layout(title_text=f"{x[0]} by {y}",title={
                                            'y':0.92,
                                            'x':0.5,
                                            'xanchor': 'center',
                                            'yanchor': 'top'},title_font_color="red")
                        fig.update_xaxes(rangeslider_visible=True)
                        fig.update_layout(
                                        autosize=False,
                                        width=1100,
                                        height=500)
                        with rowscat2:
                            st.plotly_chart(fig)
                            max_index = np.argmax(df[x])
                            min_index = np.argmin(df[x])
                            mx=pd.DataFrame(df[x].iloc[max_index:max_index+1])
                            mn=pd.DataFrame(df[x].iloc[min_index:min_index+1])
                            lin_ob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observation :</p>'
                            st.markdown(f"**{lin_ob}**", unsafe_allow_html=True)
                            st.write(f'**►‎ ‎ ‎ ‎For {x[0]}**')
                            st.write(f"- **For**",f'**<FONT color="#FC7726">{pd.to_datetime(df.iloc[np.argmax(df[x])][y])}‎ ‎,</FONT>**',f'**<FONT color="steelblue">{x[0]}</FONT>**',f'**is high around**',f'**<FONT color="#FC7726">{str(mx[x].values[0][0])}</FONT>**',unsafe_allow_html=True)
                            st.write(f"- **For**",f'**<FONT color="#FC7726">{pd.to_datetime(df.iloc[np.argmin(df[x])][y])}‎ ‎,</FONT>**',f'**<FONT color="steelblue">{x[0]}</FONT>**',f'**is low around**',f'**<FONT color="#FC7726">{str(mn[x].values[0][0])}</FONT>**',unsafe_allow_html=True)

                    else:
                        if submit_button_l2 or st.session_state.load_stateline:
                            st.session_state.load_stateline = True
                            if (up!='None') and (lo!='None'):
                                df = df.loc[up:lo]
                            else:
                                df=df
                        else:
                            df=df
                        fig = px.line(df, x=df.index, y=x)
                        fig.update_layout(xaxis_title=f"{y}")
                        fig.update_xaxes(rangeslider_visible=True)
                        fig.update_layout(
                                        autosize=False,
                                        width=1100,
                                        height=500)
                        with rowscat2:
                            st.plotly_chart(fig)
                            lin_ob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observations :</p>'
                            st.markdown(f"**{lin_ob}**", unsafe_allow_html=True)
                            for clolumn in x:
                                max_index = np.argmax(df[clolumn])
                                min_index = np.argmin(df[clolumn])
                                mx=pd.DataFrame(df[clolumn].iloc[max_index:max_index+1])
                                mn=pd.DataFrame(df[clolumn].iloc[min_index:min_index+1])
                                st.write(f'**►‎ ‎ ‎ ‎For {clolumn}**')
                                st.write(f"- **For**",f'**<FONT color="#FC7726">{pd.to_datetime(df.iloc[np.argmax(df[clolumn])][y])}‎ ‎,</FONT>**',f'**<FONT color="steelblue">{clolumn}</FONT>**',f'**is high around**',f'**<FONT color="#FC7726">{str(mx[clolumn].values[0])}</FONT>**',unsafe_allow_html=True)
                                st.write(f"- **For**",f'**<FONT color="#FC7726">{pd.to_datetime(df.iloc[np.argmin(df[clolumn])][y])}‎ ‎,</FONT>**',f'**<FONT color="steelblue">{clolumn}</FONT>**',f'**is low around**',f'**<FONT color="#FC7726">{str(mn[clolumn].values[0])}</FONT>**',unsafe_allow_html=True)
                                
                else:
                    with rowscat2:
                        st.write("##")
                        st.warning("**SELECT CONTINUOUS VARIABLE**")
    else:
        st.warning("**NO CONTINUOUS VARIABLE AVAILABLE**")
        
def Time_Resampling(df):
    #df.dropna(inplace=True)
    new_title = f'<p style="font-family:sans-serif; font-size: 18px;">Time_Resampling</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)
    st.write('##')
    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colnum.append(df[i].name)
    rowscat1,rowscatsp, rowscat2  = st.columns((1.2,0.1,4))
    if len(colnum)>0:
        with rowscat1:
            k={"nanoseconds":"N","microseconds":"us","milliseconds":"ms","secondly frequency":"S","minutely frequency":"min",
               "hourly frequency":"H","business hour frequency":"BH","calendar day frequency":'D',
               "business day frequency":'B',"weekly frequency":"W","semi-month start frequency (1st and 15th)":"SMS",
               "semi-month end frequency (15th and end of month)":"SM","month start frequency":"MS",
               "business month start frequency":"BMS","month end frequency":"M","business month end frequency":"BM",
               "quarter start frequency":"QS","business quarter start frequency":"BQS",
               "quarter end frequency":"Q","business quarter endfrequency":"BQ",
               "year start frequency":"AS","business year start frequency":"BAS",
               "year end frequency":"A","business year end frequency":"BA"}
            time_alias = []
            for i in k.keys():
                time_alias.append(i)
                            
            ts = st.form(key = 'Options')
            x = ts.multiselect("Select One or More Continuous Variables ",colnum)
            time = df.columns.tolist()
            y = ts.selectbox("Time Stamped Variable",time)
            time_alias.reverse()
            samp = ts.selectbox("Select Resample Method",time_alias)
            agg = ts.selectbox("Aggregation Function",['mean','min','max','sum'])
            
            submit_button_rs = ts.form_submit_button(label='Submit')
        with rowscat2:
            mul_button = st.radio("",options = ['Head of Dataset','Tail of Dataset'])
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
            if mul_button=='Head of Dataset':
                st.table(df.head(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            elif mul_button=='Tail of Dataset':
                st.table(df.tail(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            
            if "load_state_tsamp" not in st.session_state:
                st.session_state.load_state_tsamp = False  
            
            if submit_button_rs or st.session_state.load_state_tsamp:
                st.session_state.load_state_tsamp = True
                if x:
                    df.Timestamp = pd.to_datetime(df[y].astype(str),infer_datetime_format=True) 
                    df.index = df.Timestamp
                    df.sort_index(axis = 0,inplace=True)
                    if len(x) == 1: 
                        if agg=='mean':
                            df = df[x].resample(k[samp]).mean()
                        elif agg=='min':
                            df = df[x].resample(k[samp]).min()
                        elif agg=='max':
                            df = df[x].resample(k[samp]).max()
                        elif agg=='sum':
                            df = df[x].resample(k[samp]).sum()

                        fig = px.bar(df, y = x,text_auto=True)
                        fig.update_layout(title_text=f"{agg}  of {df[x[0]].name} by {samp}",title={
                                            'y':0.92,
                                            'x':0.5,
                                            'xanchor': 'center',
                                            'yanchor': 'top'},title_font_color="red")
                        fig.update_layout(
                                        autosize=False,
                                        width=1100,
                                        height=500)
                        with rowscat2:
                            st.plotly_chart(fig)
                            tab_title = f'<p style="font-family:sans-serif; font-size: 15px;">{agg}  of {df[x[0]].name} by {samp}</p>'
                            st.markdown(f"**<h1 style='text-align: center; '>{tab_title}</h1>**", unsafe_allow_html=True)
                            color = df.columns.tolist()
                            st.table(df.style.set_precision(2).highlight_max(color,'#EDFB7C').highlight_min(color,'#B1F994').set_table_styles(styles))
                    else:
                        with rowscat2:
                            fig = px.bar(df, y = x,text_auto=True)
                            if agg=='mean':
                                df = df[x].resample(k[samp]).mean()
                            elif agg=='min':
                                df = df[x].resample(k[samp]).min()
                            elif agg=='max':
                                df = df[x].resample(k[samp]).max()
                            elif agg=='sum':
                                df = df[x].resample(k[samp]).sum()

                            for i in df:
                                fig = px.bar(df, y = df[i].name,text_auto=True,title=f"{agg} of  {df[i].name} by {samp}")
                                fig.update_layout(title_text=f"{agg}  of {i} by {samp}",title={
                                            'y':0.92,
                                            'x':0.5,
                                            'xanchor': 'center',
                                            'yanchor': 'top'},title_font_color="red")

                                fig.update_layout(
                                        autosize=False,
                                        width=1100,
                                        height=500)
                                st.plotly_chart(fig)
                            tab_title = f'<p style="font-family:sans-serif; font-size: 15px;">{agg} by {samp}</p>'
                            st.markdown(f"**<h1 style='text-align: center; '>{tab_title}</h1>**", unsafe_allow_html=True)
                            color = df.columns.tolist()
                            st.table(df.style.set_precision(2).highlight_max(color,'#EDFB7C').highlight_min(color,'#B1F994').set_table_styles(styles))
                            #.highlight_max(['min','max','mean','frequency','% share'],'#EDFB7C').highlight_min(['min','max','mean','frequency','% share'],'#B1F994').
                else:
                    with rowscat2:
                        st.write("##")
                        st.warning("**SELECT CONTINUOUS VARIABLE**")
                    
    else:
        st.warning("**NO CONTINUOUS VARIABLE AVAILABLE**")                          

        
        
def ETS_Decomposition(df):
    #df.dropna(inplace=True)
    new_title = f'<p style="font-family:sans-serif; font-size: 18px;">Error Trend Seasonality Decomposition</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)
    st.write('##')
    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colnum.append(df[i].name)
    rowscat1,rowscatsp, rowscat2  = st.columns((1,0.1,4))
    if len(colnum)>0:
        colnum.insert(0,'None')
        with rowscat1:
            ets = st.form(key = 'Options')
            x = ets.selectbox("Select Continuous Variable",colnum)
            time = df.columns.tolist()
            y = ets.selectbox("Time Stamped Variable",time)
            model = ets.selectbox("Select Model",['Additive','Multiplicative'])
            time_freq = {'Hours':24,'Day':30,'Week':4,'Month':12,'Quarter':3,'Year':1}
            time = ['Hours','Day','Week','Month','Quarter','Year']
            freq = ets.selectbox("Time Frequency",time)
            
            submit_button_ets = ets.form_submit_button(label='Submit')
        with rowscat2:
            mul_button = st.radio("",options = ['Head of Dataset','Tail of Dataset'])
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
            if mul_button=='Head of Dataset':
                st.table(df.head(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            elif mul_button=='Tail of Dataset':
                st.table(df.tail(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            
            if "load_state_ets" not in st.session_state:
                st.session_state.load_state_ets = False  
            
            if submit_button_ets or st.session_state.load_state_ets:
                st.session_state.load_state_ets = True
                if x!='None':
                    df=df[[y,x]].dropna()
                    df.Timestamp = pd.to_datetime(df[y].astype(str),infer_datetime_format=True) 
                    df.index = df.Timestamp
                    df.sort_index(axis = 0,inplace=True)

                    def plot_seasonal_decompose(result:DecomposeResult, dates:pd.Series=None, title:str="Seasonal Decomposition"):
                        x_values = dates if dates is not None else np.arange(len(result.observed))
                        return (
                            make_subplots(
                                rows=4,
                                cols=1,
                                subplot_titles=["Observed", "Trend", "Seasonal", "Residuals"],
                            )
                            .add_trace(
                                go.Scatter(x=x_values, y=result.observed, mode="lines", name='Observed'),
                                row=1,
                                col=1,
                            )
                            .add_trace(
                                go.Scatter(x=x_values, y=result.trend, mode="lines", name='Trend'),
                                row=2,
                                col=1,
                            )
                            .add_trace(
                                go.Scatter(x=x_values, y=result.seasonal, mode="lines", name='Seasonal'),
                                row=3,
                                col=1,
                            )
                            .add_trace(
                                go.Scatter(x=x_values, y=result.resid, mode="lines", name='Residual'),
                                row=4,
                                col=1,
                            )
                            .update_layout(
                                height=900, title=f'<b>{title}</b>', margin={'t':100}, title_x=0.5, showlegend=False
                            )
                        )

                    decomposition = seasonal_decompose(x=df[x], model=model, period=time_freq[freq])
                    fig = plot_seasonal_decompose(decomposition, dates=df.index)
                    fig.update_layout(
                                        autosize=False,
                                        width=1100,
                                        height=900)
                    st.plotly_chart(fig)  
                else:
                    with rowscat2:
                        st.write("##")
                        st.warning("**SELECT CONTINUOUS VARIABLE**")
                    
    else:
        st.warning("**NO CONTINUOUS VARIABLE AVAILABLE**")                    
        
        
        
def Stationarity_Check(df):
    #df.dropna(inplace=True) it is achevied in adf_test(series)
    new_title = f'<p style="font-family:sans-serif; font-size: 18px;">Augmented Dickey-Fuller Test</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)
    st.write('##')
    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colnum.append(df[i].name)
    rowscat1,rowscatsp, rowscat2  = st.columns((1,0.1,4))
    if len(colnum)>0:
        colnum.insert(0,'None')
        with rowscat1:
            sc = st.form(key = 'Options')
            x = sc.selectbox("Select Continuous Variable ",colnum)
            time = df.columns.tolist()
            y = sc.selectbox("Time Stamped Variable",time)
            
            submit_button_sc = sc.form_submit_button(label='Submit')
        with rowscat2:
            mul_button = st.radio("",options = ['Head of Dataset','Tail of Dataset'])
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
            if mul_button=='Head of Dataset':
                st.table(df.head(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            elif mul_button=='Tail of Dataset':
                st.table(df.tail(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            
            if "load_state_check" not in st.session_state:
                st.session_state.load_state_check = False  
            
            if submit_button_sc or st.session_state.load_state_check :
                st.session_state.load_state_check = True
                if x!='None':
                    tab_title = f'<p style="font-family:sans-serif; font-size: 15px;">Stationarity Check for {x}</p>'
                    st.markdown(f"**<h1 style='text-align: center; '>{tab_title}</h1>**", unsafe_allow_html=True)
                    df.Timestamp = pd.to_datetime(df[y].astype(str),infer_datetime_format=True) 
                    df.index = df.Timestamp
                    df.sort_index(axis = 0,inplace=True)
                    def adf_test(series):
                        result = adfuller(series.dropna(),autolag='AIC') # .dropna() handles differenced data
                        labels = ['ADF test statistic','p-value','# lags used','# observations']
                        out = pd.Series(result[0:4],index=labels)

                        for key,val in result[4].items():
                            out[f'critical value ({key})']=val

                        st.table(pd.DataFrame(out,columns=[""]).style.set_table_styles(styles))          # .to_string() removes the line "dtype: float64"
                        if result[1] <= 0.05:
                            st.write(f'**►‎ ‎ ‎ ‎Strong evidence against the‎ ‎**',f'**<FONT color="steelblue">Null Hypothesis</FONT>**',unsafe_allow_html=True)
                            st.write(f'**►‎ ‎ ‎ ‎Reject the‎ ‎**',f'**<FONT color="steelblue">Null Hypothesis</FONT>**',unsafe_allow_html=True)
                            st.write(f'**►‎ ‎ ‎ ‎Data has no unit root and is‎ ‎**',f'**<FONT color="steelblue">Stationary</FONT>**',unsafe_allow_html=True)

                        else:
                            st.write(f'**►‎ ‎ ‎ ‎Weak evidence against‎ ‎**',f'**<FONT color="steelblue">Null Hypothesis</FONT>**',unsafe_allow_html=True)
                            st.write(f'**►‎ ‎ ‎ ‎Fail to reject the‎ ‎**',f'**<FONT color="steelblue">Null Hypothesis</FONT>**',unsafe_allow_html=True)
                            st.write(f'**►‎ ‎ ‎ ‎Data has a unit root and is‎ ‎**',f'**<FONT color="steelblue">Non-Stationary</FONT>**',unsafe_allow_html=True)



                    adf_test(df[x])
                    
                else:
                    with rowscat2:
                        st.write("##")
                        st.warning("**SELECT CONTINUOUS VARIABLE**")
                
    else:
        st.warning("**NO CONTINUOUS VARIABLE AVAILABLE**")                    
                        
        
def ACF_PACF(df):
    #df.dropna(inplace=True)
    new_title = f'<p style="font-family:sans-serif; font-size: 18px;">Autocorrelation (ACF) And Partial Autocorrelation (PACF) Plots</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)
    st.write('##')
    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if (df[i].nunique()) >5 :
                colnum.append(df[i].name)
    rowscat1,rowscatsp, rowscat2  = st.columns((1,0.1,4))
    if len(colnum)>0:
        colnum.insert(0,'None')
        with rowscat1:
            apc = st.form(key = 'Options')
            x = apc.selectbox("Select Continuous Variable  ",colnum)
            time = df.columns.tolist()
            y = apc.selectbox("Time Stamped Variable",time)
            alag = np.arange(1,df.shape[0]).tolist()
            alag.insert(0,'Default 40 lags')
            acf_lag = apc.selectbox("ACF Lag",alag)
            plag = df.shape[0]/2
            plag_list = np.arange(1,df.shape[0]).tolist()[0:int(plag)-1]
            plag_list.insert(0,'Default 40 lags')
            pacf_lag = apc.selectbox("PACF Lag",plag_list)
            
            submit_button_acf = apc.form_submit_button(label='Submit')
        with rowscat2:
            mul_button = st.radio("",options = ['Head of Dataset','Tail of Dataset'])
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
            if mul_button=='Head of Dataset':
                st.table(df.head(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            elif mul_button=='Tail of Dataset':
                st.table(df.tail(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            
            if "load_state_acf" not in st.session_state:
                st.session_state.load_state_acf = False  
            
            if submit_button_acf or st.session_state.load_state_acf:
                st.session_state.load_state_acf = True
                if x!='None':
                    df.Timestamp = pd.to_datetime(df[y].astype(str),infer_datetime_format=True) 
                    df.index = df.Timestamp
                    df.sort_index(axis = 0,inplace=True)

                    def create_ACF_plot(series):
                        if acf_lag== 'Default 40 lags':
                            corr_array = acf(series.dropna(),nlags = 40, alpha=0.05)
                        else:
                            corr_array = acf(series.dropna(),nlags = acf_lag , alpha=0.05)

                        lower_y = corr_array[1][:,0] - corr_array[0]
                        upper_y = corr_array[1][:,1] - corr_array[0]

                        fig = go.Figure()
                        [fig.add_scatter(x=(x,x), y=(0,corr_array[0][x]), mode='lines',line_color='#3f3f3f') 
                         for x in range(len(corr_array[0]))]
                        fig.add_scatter(x=np.arange(len(corr_array[0])), y=corr_array[0], mode='markers', marker_color='#1f77b4',
                                       marker_size=12)
                        fig.add_scatter(x=np.arange(len(corr_array[0])), y=upper_y, mode='lines', line_color='rgba(255,255,255,0)')
                        fig.add_scatter(x=np.arange(len(corr_array[0])), y=lower_y, mode='lines',fillcolor='rgba(32, 146, 230,0.3)',
                                fill='tonexty', line_color='rgba(255,255,255,0)')
                        fig.update_traces(showlegend=False)
                        if acf_lag== 'Default 40 lags':
                            fig.update_xaxes(range=[-1,40+2])
                            title=f'Autocorrelation (ACF) for {x} with {acf_lag}'
                        else:
                            fig.update_xaxes(range=[-1,acf_lag+2])
                            title=f'Autocorrelation (ACF) for {x} with {acf_lag} lags'

                        fig.update_yaxes(zerolinecolor='#000000')
                        #title=f'Autocorrelation (ACF) for {x} with {acf_lag}'
                        fig.update_layout(title=title)
                        fig.update_xaxes(rangeslider_visible=True)
                        fig.update_layout(autosize=False,width=1100,height=500)
                        fig.update_layout(title={
                                        'y':0.92,
                                        'x':0.5,
                                        'xanchor': 'center',
                                        'yanchor': 'top'},title_font_color="red")
                        st.plotly_chart(fig)

                    def create_PACF_plot(series):
                        if pacf_lag== 'Default 40 lags':
                            corr_array = pacf(series.dropna(),nlags = 40, alpha=0.05)
                        else:
                            corr_array = pacf(series.dropna(),nlags = pacf_lag , alpha=0.05)

                        lower_y = corr_array[1][:,0] - corr_array[0]
                        upper_y = corr_array[1][:,1] - corr_array[0]

                        fig = go.Figure()
                        [fig.add_scatter(x=(x,x), y=(0,corr_array[0][x]), mode='lines',line_color='#3f3f3f') 
                         for x in range(len(corr_array[0]))]
                        fig.add_scatter(x=np.arange(len(corr_array[0])), y=corr_array[0], mode='markers', marker_color='#1f77b4',
                                       marker_size=12)
                        fig.add_scatter(x=np.arange(len(corr_array[0])), y=upper_y, mode='lines', line_color='rgba(255,255,255,0)')
                        fig.add_scatter(x=np.arange(len(corr_array[0])), y=lower_y, mode='lines',fillcolor='rgba(32, 146, 230,0.3)',
                                fill='tonexty', line_color='rgba(255,255,255,0)')
                        fig.update_traces(showlegend=False)
                        if pacf_lag== 'Default 40 lags':
                            fig.update_xaxes(range=[-1,40+2])
                            title=f'Partial Autocorrelation (PACF) for {x} with {pacf_lag}'
                        else:
                            fig.update_xaxes(range=[-1,pacf_lag+2])
                            title=f'Partial Autocorrelation (PACF) for {x} with {pacf_lag} lags'

                        fig.update_yaxes(zerolinecolor='#000000')
                        #title=f'Partial Autocorrelation (PACF) for {x} with {pacf_lag}'
                        fig.update_layout(title=title)
                        fig.update_xaxes(rangeslider_visible=True)
                        fig.update_layout(autosize=False,width=1100,height=500)
                        fig.update_layout(title={
                                        'y':0.92,
                                        'x':0.5,
                                        'xanchor': 'center',
                                        'yanchor': 'top'},title_font_color="red")
                        st.plotly_chart(fig) 

                    create_ACF_plot(df[x])
                    create_PACF_plot(df[x])
                
                else:
                    with rowscat2:
                        st.write("##")
                        st.warning("**SELECT CONTINUOUS VARIABLE**")

    else:
        st.warning("**NO CONTINUOUS VARIABLE AVAILABLE**")        
        

            
def Bivariate_Continuous_Vs_Continuous (df):
    new_title = f'<p style="font-family:sans-serif; font-size: 18px;">Bivariate Continuous Vs Continuous</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)
    st.write('##')
    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colnum.append(df[i].name)
    hu=[]
    hu.append("None")
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()<=5 :
                hu.append(df[i].name)
        if (df[i].dtypes=="object"):
            if df[i].nunique()<=50 :
                hu.append(df[i].name)

    rowscat1,rowscatsp, rowscat2,rowscat3  = st.columns((1.5,1,2,.1))
    if len(colnum)>0:
        with rowscat1:
            contcat1 = st.form(key = 'Options')
            x = contcat1.selectbox("Independent Continuous Variable",colnum)
            y = contcat1.selectbox("Dependent Continuous Variable",colnum)
            z = contcat1.selectbox("Optional Hue Variable",hu)
            submit_button1 = contcat1.form_submit_button(label='Submit')

            if submit_button1:
                fig1, ax1 = plt.subplots()
                ax = plt.axes()
                plt.gcf().autofmt_xdate()
                fig = plt.figure(figsize=(7,10))
                fig1=px.scatter(df, x=df[x].name, y=df[y].name,title= "scatter graph with an OLS trendline for Regression model",trendline="ols",trendline_color_override="red")

                fig1.update_layout(title_font_color="#B14E2B",title={
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})
                st.plotly_chart(fig1)

                with rowscat2:
                    fig, ax = plt.subplots()
                    fig = plt.figure(figsize=(10,8))
                    ax = plt.axes()
                    plt.gcf().autofmt_xdate()
                    if z=="None":
                        sc=sns.scatterplot(df[x],df[y])
                        sc.legend(loc='center left', bbox_to_anchor=(1.25, 0.5), ncol=1)
                    else:
                        sc=sns.scatterplot(df[x],df[y],hue=df[z])
                        sc.legend(loc='center left', bbox_to_anchor=(1, 0.86), ncol=1)
                    plt.title(df[x].name+"  V/S  "+df[y].name,fontsize=18)
                    plt.xlabel(df[x].name,fontsize=13)
                    plt.ylabel(df[y].name,fontsize=13)
                    st.pyplot(fig)
                    new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 16px;">Observations :</p>'
                    st.markdown(f"**{new_title1}**", unsafe_allow_html=True)
                    a= round(ma.corrcoef(ma.masked_invalid(df[x]),ma.masked_invalid(df[y]))[0][1],2)
                    if a >= 0.80 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable is Positively highly correlated with {df[y].name}**")
                        st.write(f"- **As {df[x].name} values increases {df[y].name} increases gradually**")
                    elif 0.79 >= a >= 0.50 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable is Positively moderately correlated with {df[y].name}**")
                        st.write(f"- **As {df[x].name} values increases {df[y].name} increases moderately**")
                    elif 0 <= a <= 0.49 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable has no good relation with {df[y].name}**")
                        st.write(f"- **{df[x].name} variable shows not that great effect on {df[y].name}**")
                    elif a <= -0.80 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable is Negatively highly correlated with {df[y].name}**")
                        st.write(f"- **As {df[x].name} values increases {df[y].name} decreases gradually**") 
                    elif -0.79 < a <= -0.50 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable is Negatively moderately correlated with {df[y].name}**")
                        st.write(f"- **As {df[x].name} values increases {df[y].name} decreases moderately**")
                    elif  0>= a >= -0.49 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable has no good relation with {df[y].name}**")
                        st.write(f"- **{df[x].name} variable shows not that great effect on {df[y].name}**")
            else:
                with rowscat2:
                    st.warning('**CLICK SUBMIT**')
                
    else:
        st.warning('**NO NUMERIC VARIABLE IS AVAILABLE**')

        

        
def Bivariate_Continuous_Vs_Continuous_full (df,cont,target):
    y=target
    new_title = f'<p style="font-family:sans-serif; font-size: 18px;">Bivariate Continuous Vs Continuous</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)
    st.write('##')
   # cont.remove(df[y].name)
    for x in cont:
        if x!=target:
            new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 16px;">{x} Vs {target}</p>'
            st.markdown(f"**<h1 style='text-align: center; '>{new_title}</h1>**", unsafe_allow_html=True)
            rowscat1,rowscatsp, rowscat2,rowscat3  = st.columns((1.5,1,2,.1))
            with rowscat1:
                fig1, ax1 = plt.subplots()
                ax = plt.axes()
                plt.gcf().autofmt_xdate()
                fig = plt.figure(figsize=(7,10))
                fig1=px.scatter(df, x=df[x].name, y=df[y].name,title= "scatter graph with an OLS trendline for Regression model",trendline="ols",trendline_color_override="red")

                fig1.update_layout(title_font_color="#B14E2B",title={
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'})
                st.plotly_chart(fig1)

                with rowscat2:
                    fig, ax = plt.subplots()
                    fig = plt.figure(figsize=(10,8))
                    ax = plt.axes()
                    plt.gcf().autofmt_xdate()
                    sc=sns.scatterplot(df[x],df[y])
                    sc.legend(loc='center left', bbox_to_anchor=(1.25, 0.5), ncol=1)
                    plt.title(df[x].name+"  V/S  "+df[y].name,fontsize=18)
                    plt.xlabel(df[x].name,fontsize=13)
                    plt.ylabel(df[y].name,fontsize=13)
                    st.pyplot(fig)
                    new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 16px;">Observations :</p>'
                    st.markdown(f"**{new_title1}**", unsafe_allow_html=True)
                    a= round(ma.corrcoef(ma.masked_invalid(df[x]),ma.masked_invalid(df[y]))[0][1],2)
                    if a >= 0.80 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable is Positively highly correlated with {df[y].name}**")
                        st.write(f"- **As {df[x].name} values increases {df[y].name} increases gradually**")
                    elif 0.79 >= a >= 0.50 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable is Positively moderately correlated with {df[y].name}**")
                        st.write(f"- **As {df[x].name} values increases {df[y].name} increases moderately**")
                    elif 0 <= a <= 0.49 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable has no good relation with {df[y].name}**")
                        st.write(f"- **{df[x].name} variable shows not that great effect on {df[y].name}**")
                    elif a <= -0.80 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable is Negatively highly correlated with {df[y].name}**")
                        st.write(f"- **As {df[x].name} values increases {df[y].name} decreases gradually**") 
                    elif -0.79 < a <= -0.50 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable is Negatively moderately correlated with {df[y].name}**")
                        st.write(f"- **As {df[x].name} values increases {df[y].name} decreases moderately**")
                    elif  0>= a >= -0.49 :
                        st.write(f"- **correlation coefficient value : {a.astype(str)}**")
                        st.write(f"- **{df[x].name} variable has no good relation with {df[y].name}**")
                        st.write(f"- **{df[x].name} variable shows not that great effect on {df[y].name}**")

            st.write("*-"*280)    
        
        
def Bivariate_Continuous_Vs_Categorical (df):
    bvcatcont = f'<p style="font-family:sans-serif; font-size: 18px;">Bivariate Continuous Vs Categorical</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{bvcatcont}</h1>**", unsafe_allow_html=True)
    colcatx=[]
    colconty=[]
    for i in df:
        if df[i].dtypes == "object" :
            #if df[i].nunique()<=50:
            if df[i].nunique()>0:
                colcatx.append(df[i].name)

        if df[i].dtypes != "object" :
            if df[i].nunique() <=5 :
                colcatx.append(df[i].name)

        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colconty.append(df[i].name)
    rowcatcat1,rowcatcatsp, rowcatcat2 = st.columns((2,.2,2.7))
    if len(colcatx)>0 and len(colconty)>0:
        with rowcatcat1:
            colconty.insert(0,'None')
            contcat = st.form(key = 'Options')
            y = contcat.selectbox("Continuous Variable",colconty)
            #colconty.insert(0,'None')
            x = contcat.selectbox("Categorical Variable",colcatx)
            submit_button_contcat = contcat.form_submit_button(label='Submit')
            
            if y!='None':
                if "load_state" not in st.session_state:
                    st.session_state.load_state = False
                    
                if submit_button_contcat or st.session_state.load_state:
                    st.session_state.load_state = True
                    clas_df=pd.DataFrame(df[y].groupby(df[x]).agg('mean'))
                    clas_df=clas_df.sort_values(by=df[y].name,ascending=False)
                    clas=clas_df.index.tolist()
                    z = st.selectbox("Select Categorical class",clas)
                    choice = st.radio("Select Type of Plot",('Boxplot','Barplot'))
                    warnings.filterwarnings(action="ignore")
                    fig, ax = plt.subplots()
                    if choice=='Boxplot':
                        data = []
                        classes= clas_df.index.tolist()[0:50]
                        classes.reverse()
                        for i in classes:
                            trace = go.Box(
                            x=df.loc[df[x] == i][df[y].name],
                            name = i,boxmean=True)
                            data.append(trace)
                        if df[x].nunique()<=50:
                            layout = go.Layout(title = f"Boxplot of {df[y].name} by {df[x].name}")
                        else:
                            layout = go.Layout(title = f"Boxplot of {df[y].name} by Top 50 {df[x].name}")

                        fig = go.Figure(data=data,layout=layout)
                        if df[x].nunique()<=2:

                            fig.update_layout(
                                autosize=False,
                                width=500,
                                height=df[x].nunique()*200,#df2[x].nunique()
                            )

                        elif df[x].nunique()>=3 and df[x].nunique()<=5:

                            fig.update_layout(
                                autosize=False,
                                width=500,
                                height=df[x].nunique()*100,#df2[x].nunique()
                            )

                        else:

                            fig.update_layout(
                                autosize=False,
                                width=500,
                                height=len(df[x].value_counts().index.tolist()[0:50])*35#df[x].nunique()*35,#df2[x].nunique()
                            )
        #                         fig.update_layout(
        #                             autosize=False,
        #                             width=500,
        #                             height=df[x].nunique()*100,
        #                         )
                        st.plotly_chart(fig)

                    if choice=='Barplot':
                        if df[x].nunique()<=50:
                            fig, ax = plt.subplots()
                            fig = plt.figure(figsize=(8,df[x].nunique()*0.8))
                            ax = plt.axes()
                            plt.gcf().autofmt_xdate()
                            bar=sns.barplot(df[y],df[x].astype(str));
                            plt.xticks(rotation = 45)
                            plt.title(df[x].name+" V/S "+df[y].name,fontsize=11)
                            st.pyplot(fig)
                        else:
                            title = f"Barplot of {df[y].name} by Top 50 {df[x].name}"
                            st.write(title)
                            fig, ax = plt.subplots()
                            fig = plt.figure(figsize=(8,50*0.6))
                            ax = plt.axes()
                            plt.gcf().autofmt_xdate()

                            bar_df1=pd.DataFrame(df[y].groupby(df[x]).agg('mean'))
                            bar_df1 = bar_df1.sort_values(by=df[y].name,ascending=False)
                            bar_df1.reset_index(level=0, inplace=True)
                            bar_df1 = bar_df1.iloc[0:50,:]

                            sns.barplot(bar_df1[df[y].name],bar_df1[df[x].name])
                            #bar=sns.barplot(df[y],df[x].astype(str));
                            plt.xticks(rotation = 45)
                            plt.title(df[x].name+" V/S "+df[y].name,fontsize=11)
                            st.pyplot(fig)

        #                     if df[x].nunique()>15:
        #                         fig = plt.figure(figsize=(7,df[x].nunique()*0.3)) # try different values
        #                     else:
        #                         fig = plt.figure(figsize=(7,6))

        #                     ax = plt.axes()
        #                     plt.gcf().autofmt_xdate()
        #                     kde=sns.kdeplot(df[y],hue=df[x])
        #                     plt.title(df[x].name+" V/S "+df[y].name,fontsize=11)
        #                     plt.xticks(fontsize=8)
        #                     plt. tight_layout()
        #                     st.pyplot(fig)
                    with rowcatcat2:
                        st.write("##")
                        st.info("If Continuous variable is related to Sales, Price, Charges, Bill, Cost, Payment, Expenses then Click the Check Box Yes")

                        agree = st.checkbox('Yes')
                        if agree:
                            catcontob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observation :</p>'
                            st.markdown(f"**{catcontob}**", unsafe_allow_html=True)
                            j = 0
                            null=pd.DataFrame({df[x].name:df[x].value_counts().index.values})


                            categories=[]
                            totsum=df[y].sum()
                            for col in null:
                                while j < null[col].nunique():

                                    a = pd.Series(df[y][df[x]==null[col].unique()[j]].values)
                                    if len(a)!=a.isnull().sum():

                                        e = pd.DataFrame({null.iloc[j,0:][0]:[a.min(),a.max(),round(a.mean()),a.mode()[0],len(a),len(a)/len(df[x])*100,(a.sum()/totsum)*100]},
                                                         index=['min','max','mean','mode','count','frequency','% share'])
                                    else:
                                        e = pd.DataFrame({null.iloc[j,0:][0]:[np.NaN,np.NaN,np.NaN,np.NaN,len(a),len(a)/len(df[x])*100,(a.sum()/totsum)*100]},
                                                         index=['min','max','mean','mode','count','frequency','% share'])

                                    categories.append(e)
                                    j = j+1
                            new=pd.concat(categories, axis = 1)
                            f=new[z]
                            val=f.values.tolist()

                            indx=f.index.tolist()

                            cla_df=pd.DataFrame([val], columns=indx)
                            complete=pd.concat([pd.DataFrame({f'{x}':[z]}),cla_df],axis=1)

                            st.write(f'**<FONT color="#FC7726">{df[y].name} for {z} {df[x].name}</FONT>**',unsafe_allow_html=True)

                            st.table(complete.style.set_precision(3).set_table_styles(styles))

                            cate1=df[x].value_counts().index.values.tolist()
                            a = pd.Series(df[y][df[x]==z])
                            if len(a)!=a.isnull().sum():
                                st.write(f"►‎ ‎ ‎ ‎ **For {df[x].name} {z} :** Most of the {df[y].name} ranges between **{str(round(a.quantile(0.25)))}** and **{str(round(a.quantile(0.75)))}**")

                            st.write(f'**<FONT color="#FC7726">{df[y].name} Stats for Different {df[x].name} Categories</FONT>**',unsafe_allow_html=True)

                            st.write('►‎ ‎ ‎ ‎',f'**<FONT color="#FC7726">%  share :‎ ‎</FONT>**',f'**{df[x].name} {new.columns[np.argmax(new.iloc[6,0:].values)]} has highest  %  share : {np.round(new.iloc[6,0:].values.max(),2)}‎ ‎ and {new.columns[np.argmin(new.iloc[6,0:].values)]} has lowest  %  share : {np.round(new.iloc[6,0:].values.min(),2)}**',unsafe_allow_html=True)

                            st.write('►‎ ‎ ‎ ‎',f'**<FONT color="#FC7726">Min {df[y].name} :‎ ‎</FONT>**',f'**{df[x].name} {new.columns[np.argmax(new.iloc[0,0:].values)]} has High Min {df[y].name} : {np.round(new.iloc[0,0:].values.max(),2)}‎ ‎ and {new.columns[np.argmin(new.iloc[0,0:].values)]} has Low Min {df[y].name} : {np.round(new.iloc[0,0:].values.min(),2)}**',unsafe_allow_html=True)

                            st.write('►‎ ‎ ‎ ‎',f'**<FONT color="#FC7726">Max {df[y].name} :‎ ‎</FONT>**',f'**{df[x].name} {new.columns[np.argmax(new.iloc[1,0:].values)]} has High Max {df[y].name} : {np.round(new.iloc[1,0:].values.max(),2)}‎ ‎ and {new.columns[np.argmin(new.iloc[1,0:].values)]} has Low Max {df[y].name} : {np.round(new.iloc[1,0:].values.min(),2)}**',unsafe_allow_html=True)

                            st.write('►‎ ‎ ‎ ‎',f'**<FONT color="#FC7726">Mean {df[y].name} :‎ ‎</FONT>**',f'**{df[x].name} {new.columns[np.argmax(new.iloc[2,0:].values)]} has High Mean {df[y].name} : {np.round(new.iloc[2,0:].values.max(),2)}‎ ‎ and {new.columns[np.argmin(new.iloc[2,0:].values)]} has Low Mean {df[y].name} : {np.round(new.iloc[2,0:].values.min(),2)}**',unsafe_allow_html=True)

                            st.write('►‎ ‎ ‎ ‎',f'**<FONT color="#FC7726">{df[x].name} Count  :‎ ‎</FONT>**',f'**{df[x].name} {new.columns[np.argmax(new.iloc[4,0:].values)]} count is High in the data : {np.round(new.iloc[4,0:].values.max(),2)}({np.round(new.iloc[5,0:].values.max(),2)} %) ‎ ‎ and {new.columns[np.argmin(new.iloc[4,0:].values)]} count is Less in the data : {np.round(new.iloc[4,0:].values.min(),2)} ({np.round(new.iloc[5,0:].values.min(),2)} %)**',unsafe_allow_html=True)

            #                         if df[x].nunique()>50:
            #                             st.write(f'**<FONT color="#FC7726">Considering Top 50 {df[x].name} Categories</FONT>**',unsafe_allow_html=True)
            #                             top_50avg=new.iloc[:,0:50]

            #                             st.write(f"►‎ ‎ ‎ ‎ **Average {df[y].name} {top_50avg.iloc[2,0:].values.max()}  for category {top_50avg.columns[np.argmax(top_50avg.iloc[2,0:].values)]} is high and Average {df[y].name} {top_50avg.iloc[2,0:].values.min()} for category {top_50avg.columns[np.argmin(top_50avg.iloc[2,0:].values)]} is low**")

            #                             st.write(f'**<FONT color="#FC7726">{df[y].name} for Top 50 {df[x].name} categories</FONT>**',unsafe_allow_html=True)

            #                         else:
            #                             st.write(f'**<FONT color="#FC7726">{df[y].name} for All {df[x].name} categories</FONT>**',unsafe_allow_html=True)

                            new1=new.T
                            #new1=new1.iloc[0:50,:]
                            new1.reset_index(level=0, inplace=True)
                            new1.rename(columns = {'index':'categories'}, inplace = True)

                            hide_table_row_bvcatcont = """
                                <style>
                                tbody th {display:none}
                                .blank {display:none}
                                </style>
                                """
                            # Inject CSS with Markdown
                            st.markdown(hide_table_row_bvcatcont, unsafe_allow_html=True)
                            sort_col = ['categories','min','max','mean','mode','count','frequency','% share']
                            sort_on = st.selectbox("Sort by",sort_col)

                            asc_dsc = st.radio(label = 'Sort ASC or DESC', options = ['ASC','DESC'])
                            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
                            if asc_dsc =='DESC' :
                                new1 = new1.sort_values(by = sort_on,ascending=False)
                            else :
                                new1 = new1.sort_values(by = sort_on,ascending=True)


                            if df[x].nunique()>50:
                                if (sort_on == 'categories') or (sort_on == 'count') or (sort_on == 'frequency'):
                                    st.write(f'**<FONT color="#FC7726">Showing Top 50 {sort_on.upper()} in {asc_dsc} order </FONT>**',unsafe_allow_html=True)

                                else :
                                    st.write(f'**<FONT color="#FC7726">Showing Top 50 {sort_on.upper()} {df[y].name} in {asc_dsc} order </FONT>**',unsafe_allow_html=True)

                                st.table(new1.iloc[0:50,:].style.set_precision(2).set_table_styles(styles))

                            else :
                                if (sort_on == 'categories') or (sort_on == 'count') or (sort_on == 'frequency'):
                                    st.write(f'**<FONT color="#FC7726">Showing {sort_on.upper()} in {asc_dsc} order </FONT>**',unsafe_allow_html=True)

                                else :
                                    st.write(f'**<FONT color="#FC7726">Showing  {sort_on.upper()} {df[y].name} in {asc_dsc} order </FONT>**',unsafe_allow_html=True)

                                st.table(new1.style.set_precision(2).highlight_max(['min','max','mean','frequency','% share'],'#EDFB7C').highlight_min(['min','max','mean','frequency','% share'],'#B1F994').set_table_styles(styles))

                            st.write("")

                        else:
                            j = 0
                            null=pd.DataFrame({df[x].name:df[x].value_counts().index.values})
                            catcontob = f'<p style="font-family:sans-serif; color:steelblue; font-size: 15px;">Observation :</p>'
                            st.markdown(f"**{catcontob}**", unsafe_allow_html=True)

                            categories=[]
                            totsum=df[y].sum()
                            for col in null:
                                while j < null[col].nunique():

                                    a = pd.Series(df[y][df[x]==null[col].unique()[j]].values)
                                    if len(a)!=a.isnull().sum():
                                        e = pd.DataFrame({null.iloc[j,0:][0]:[a.min(),a.max(),round(a.mean()),a.mode()[0],len(a),len(a)/len(df[x])*100]},
                                                         index=['min','max','mean','mode','count','frequency'])
                                    else:
                                        e = pd.DataFrame({null.iloc[j,0:][0]:[np.NaN,np.NaN,np.NaN,np.NaN,len(a),len(a)/len(df[x])*100]},
                                                         index=['min','max','mean','mode','count','frequency'])

                                    categories.append(e)
                                    j = j+1
                            new=pd.concat(categories, axis = 1)
                            f=new[z]
                            val=f.values.tolist()

                            indx=f.index.tolist()

                            cla_df=pd.DataFrame([val], columns=indx)
                            complete=pd.concat([pd.DataFrame({f'{x}':[z]}),cla_df],axis=1)
                            st.write(f'**<FONT color="#FC7726">{df[y].name} for {z} {df[x].name}</FONT>**',unsafe_allow_html=True)


                            st.table(complete.style.set_precision(3).set_table_styles(styles))

                            cate1=df[x].value_counts().index.values.tolist()
                            a = pd.Series(df[y][df[x]==z])
                            if len(a)!=a.isnull().sum():
                                st.write(f"►‎ ‎ ‎ ‎ **For {df[x].name} {z} :** Most of the {df[y].name} ranges between **{str(round(a.quantile(0.25)))}** and **{str(round(a.quantile(0.75)))}**")


                                st.write(f'**<FONT color="#FC7726">{df[y].name} Stats for Different {df[x].name} Categories</FONT>**',unsafe_allow_html=True)

                                st.write('►‎ ‎ ‎ ‎',f'**<FONT color="#FC7726">Min {df[y].name} :‎ ‎</FONT>**',f'**{df[x].name} {new.columns[np.argmax(new.iloc[0,0:].values)]} has High Min {df[y].name} : {np.round(new.iloc[0,0:].values.max(),2)}‎ ‎ and {new.columns[np.argmin(new.iloc[0,0:].values)]} has Low Min {df[y].name} : {np.round(new.iloc[0,0:].values.min(),2)}**',unsafe_allow_html=True)

                                st.write('►‎ ‎ ‎ ‎',f'**<FONT color="#FC7726">Max {df[y].name} :‎ ‎</FONT>**',f'**{df[x].name} {new.columns[np.argmax(new.iloc[1,0:].values)]} has High Max {df[y].name} : {np.round(new.iloc[1,0:].values.max(),2)}‎ ‎ and {new.columns[np.argmin(new.iloc[1,0:].values)]} has Low Max {df[y].name} : {np.round(new.iloc[1,0:].values.min(),2)}**',unsafe_allow_html=True)

                                st.write('►‎ ‎ ‎ ‎',f'**<FONT color="#FC7726">Mean {df[y].name} :‎ ‎</FONT>**',f'**{df[x].name} {new.columns[np.argmax(new.iloc[2,0:].values)]} has High Mean {df[y].name} : {np.round(new.iloc[2,0:].values.max(),2)}‎ ‎ and {new.columns[np.argmin(new.iloc[2,0:].values)]} has Low Mean {df[y].name} : {np.round(new.iloc[2,0:].values.min(),2)}**',unsafe_allow_html=True)

                                st.write('►‎ ‎ ‎ ‎',f'**<FONT color="#FC7726">{df[x].name} Count  :‎ ‎</FONT>**',f'**{df[x].name} {new.columns[np.argmax(new.iloc[4,0:].values)]} count is High in the data : {np.round(new.iloc[4,0:].values.max(),2)}({np.round(new.iloc[5,0:].values.max(),2)} %) ‎ ‎ and {new.columns[np.argmin(new.iloc[4,0:].values)]} count is Less in the data : {np.round(new.iloc[4,0:].values.min(),2)} ({np.round(new.iloc[5,0:].values.min(),2)} %)**',unsafe_allow_html=True)

                            new1=new.T
                            #new1=new1.iloc[0:50,:]
                            new1.reset_index(level=0, inplace=True)
                            new1.rename(columns = {'index':'categories'}, inplace = True)
                            hide_table_row_bvcatcont = """
                                <style>
                                tbody th {display:none}
                                .blank {display:none}
                                </style>
                                """
                            # Inject CSS with Markdown
                            st.markdown(hide_table_row_bvcatcont, unsafe_allow_html=True)

                            sort_col = ['categories','min','max','mean','mode','count','frequency','% share']
                            sort_on = st.selectbox("Sort by",sort_col)

                            asc_dsc = st.radio(label = 'Sort ASC or DESC', options = ['ASC','DESC'])
                            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
                            if asc_dsc =='DESC' :
                                new1 = new1.sort_values(by = sort_on,ascending=False)
                            else :
                                new1 = new1.sort_values(by = sort_on,ascending=True)


                            if df[x].nunique()>50:
                                if (sort_on == 'categories') or (sort_on == 'count') or (sort_on == 'frequency'):
                                    st.write(f'**<FONT color="#FC7726">Showing Top 50 {sort_on.upper()} in {asc_dsc} order </FONT>**',unsafe_allow_html=True)

                                else :
                                    st.write(f'**<FONT color="#FC7726">Showing Top 50 {sort_on.upper()} {df[y].name} in {asc_dsc} order </FONT>**',unsafe_allow_html=True)
                                #st.table(new1.iloc[0:50,:].style.set_precision(2).set_table_styles(styles))
                                st.table(new1.iloc[0:50,:].style.set_precision(2).set_table_styles(styles))

                            else :
                                if (sort_on == 'categories') or (sort_on == 'count') or (sort_on == 'frequency'):
                                    st.write(f'**<FONT color="#FC7726">Showing {sort_on.upper()} in {asc_dsc} order </FONT>**',unsafe_allow_html=True)

                                else :
                                    st.write(f'**<FONT color="#FC7726">Showing  {sort_on.upper()} {df[y].name} in {asc_dsc} order </FONT>**',unsafe_allow_html=True)                
                                st.table(new1.iloc[0:50,:].style.set_precision(2).highlight_max(
                                ['min','max','mean','frequency'],'#EDFB7C').highlight_min(
                                    ['min','max','mean','frequency'],'#B1F994').set_table_styles(styles))

            #                     cate=df[x].value_counts().index.values.tolist()
            #                     cate=cate[0:50]
            #                     for o in cate:
            #                         a = pd.Series(df[y][df[x]==o])
            #                         if len(a)!=a.isnull().sum():
            #                             st.write(f"- **For {df[x].name} {o} :** Most of the {df[y].name} ranges between **{str(round(a.quantile(0.25)))}** and **{str(round(a.quantile(0.75)))}**")
            #                     st.write("")
            else:
                with rowcatcat2:
                    st.write('##')
                    st.warning("**SELECT CONTINUOUS VARIABLE AND CLICK SUBMIT**")
                    
    else:
        st.warning("**NO CONTINUOUS OR CATEGORICAl VARIABLES AVAILABLE**")


def Bivariate_Categorical_Vs_Categorical(df):
    bvcatcat = f'<p style="font-family:sans-serif; font-size: 18px;">Bivariate Categorical Vs Categorical</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{bvcatcat}</h1>**", unsafe_allow_html=True)

#     df2=df
#     for i in df2:
#         if df2[i].isnull().sum()>0:
#             df2[i] = df2[i].fillna(np.NaN)#df2[i].mode()[0]
    colcatx=[]
    colcaty=[]
    for i in df:
        if df[i].dtypes == "object" :
            if df[i].nunique()<=50:
                colcatx.append(df[i].name)

        if df[i].dtypes != "object" :
            if df[i].nunique() <=5 :
                colcatx.append(df[i].name)

        if df[i].dtypes == "object" :
            if df[i].nunique()<=50:
                colcaty.append(df[i].name)

        if df[i].dtypes != "object" :
            if df[i].nunique()<=5:
                colcaty.append(df[i].name)
    hide_table_row_bvcatcat = """
                    <style>
                    tbody th {display:none}
                    .blank {display:none}
                    </style>
                    """
    if len(colcatx)>0 and len(colcaty)>0:
        yes = []
        rowcatcat1,rowcatcatsp, rowcatcat2,rowcatcatsp1  = st.columns((2,.5,3,.2))
        with rowcatcat1:
            colcatx.insert(0,'None')
            catcat = st.form(key = 'Options')
            x = catcat.selectbox("Independent Categorical Variable",colcatx)
            y = catcat.selectbox("Dependent Categorical Variable",colcaty)
            submit_button2 = catcat.form_submit_button(label='Submit')
            
        with rowcatcat2:
            st.warning("**Independent and Dependent variables choosen for Analysis have class count not more than 50**")
                
           
        if x!='None':
            if submit_button2:
                rowcatcatx1,rowcatcatxsp, rowcatcatx2,rowcatcatxsp1  = st.columns((2,.5,3,.2)) 
                df2 = df[[x]]
                df2[y] = df[[y]]
                #st.table(df2)
    #             for i in df2:
    #                 if df2[i].isnull().sum()>0:
    #                     df2[i] = df2[i].fillna(np.NaN)

                df2[y]=df2[y].astype(str)
                warnings.filterwarnings(action="ignore")
                with rowcatcatx1:
    #                     fig, ax = plt.subplots()
    #                     if df2[x].nunique()>df2[y].nunique():
    #                         fig = plt.figure(figsize=(11,df2[x].nunique()))
    #                     else:
    #                         fig = plt.figure(figsize=(11,df2[y].nunique()))

    #                     plt.title(df2[x].name+" V/S "+df2[y].name,fontsize=25)
    #                     ax=sns.countplot(y=df2[x], hue =df2[y]);
    # #                     for i in ax.patches:
    # #     # get_width pulls left or right; get_y pushes up or down
    # #                         if df2[x].nunique()>df2[y].nunique():
    # #                             ax.text(i.get_width()+1, i.get_y()+0.20, \
    # #                                     str(round((i.get_width()), 2)), fontsize=15)
    # #                         else :
    # #                             ax.text(i.get_width()+1, i.get_y()+0.20, \
    # #                                     str(round((i.get_width()), 2)), fontsize=15)
    # #                     plt.margins(x=0.1)
    #                     plt.xlabel("count",fontsize=20)
    #                     plt.ylabel(df2[x].name,fontsize=20)
    #                     plt.xticks(rotation=45,fontsize=20)
    #                     plt.yticks(fontsize=20)
    #                     plt.legend(fontsize="x-large",title = df2[y].name,loc = 'lower right')
    #                     st.pyplot(fig)
                    fig, ax = plt.subplots()
                    k=pd.crosstab(df2[x].astype(str),df2[y],dropna=False)
                    x_ind=k.index.tolist()
                    x_ind.reverse()
                    legend=k.columns.tolist()
                    legend.reverse()
                    fig = go.Figure()
                    for i in range(df2[y].nunique()):
                        val=k.iloc[:,i].values.tolist()
                        val.reverse()
                        fig.add_trace(go.Bar(
                            y=x_ind,
                            x=val,
                            name=legend[i],
                            orientation='h'
                        ))
                    if df2[x].nunique()<=2:

                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df2[x].nunique()*200,#df2[x].nunique()
                        )

                    elif df2[x].nunique()>=3 and df2[x].nunique()<=5:

                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df2[x].nunique()*100,#df2[x].nunique()
                        )

                    else:

                        fig.update_layout(
                            autosize=False,
                            width=500,
                            height=df2[x].nunique()*47,#df2[x].nunique()
                        )

                    fig.update_layout(barmode='stack')
                    fig.update_layout(yaxis_title_text=df2[x].name,xaxis_title_text="Count")

                    fig.update_layout(title_text=f"stacked bar chart of {df2[x].name} and {df2[y].name}",title={
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},title_font_color="#1F30CB")

                    st.plotly_chart(fig)

                    st.write("")

                with rowcatcatx2:
                    df1 = pd.DataFrame(pd.crosstab(df2[x].astype(str), df2[y].astype(str) ,margins=True))
                    st.table(df1.style.set_table_styles(styles))

                rowcatcat11,rowcatcatsp11, rowcatcat12,rowcatcatsp12  = st.columns((2,.5,3,.2))

                with rowcatcat12:
                    table = pd.crosstab(df2[x].astype(str), df2[y],dropna=False)
                    table = round(table.div(table.sum(axis=1), axis=0).mul(100), 2)
                    lab=df2[y].unique().tolist()
                    df2=[]
                    for lb in lab:
                        ind = (table.sort_values(by=[lb], ascending=False).loc[:, lb]).index.to_list()
                        val = (table.sort_values(by=[lb], ascending=False).loc[:, lb]).values.tolist()  
                        #l=pd.DataFrame({f'Category of {lb}':ind,f'% of {lb}':val})
                        #l=pd.DataFrame({f'for {df[y].name} {lb}':ind,f'% of {lb}':val})
                        l=pd.DataFrame({f'{df[x].name} for {df[y].name} {lb}':ind,f'% of  {lb} {df[y].name}':val})
                        df2.append(l)
                    new=pd.concat(df2,axis=1)
                    st.write(f"**Frequency of {df[y].name} for {df[x].name}**")

                    st.table(new.style.set_precision(2).set_table_styles(styles))

                with rowcatcat11:
                    new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 16px;">Observations :</p>'
                    st.markdown(f"**{new_title1}**", unsafe_allow_html=True)
                    j = 0
                    while j < df[x].nunique():
                        a = pd.crosstab(df[x],df[y])
                        b= pd.crosstab(df[x],df[y],margins = True)
                        st.write(f"**For {df[x].name} {str(a.iloc[[j]].index[0])}**")
                        st.write(f"- {df[y].name} {a.columns[np.argmin(a.iloc[j].values)]} count are less : {a.iloc[j].values.min()} which is equal to {np.round((a.iloc[j].values.min()/b.iloc[j,-1])*100,2)} %")
                        st.write(f"- {df[y].name} {a.columns[np.argmax(a.iloc[j].values)]} count are more : {a.iloc[j].values.max()} which is equal to {np.round((a.iloc[j].values.max()/b.iloc[j,-1])*100,2)} %")
                        j = j+1
            else:
                with rowcatcat1:
                    st.warning("**CLICK SUBMIT**")
                
    else:
        st.warning("**NO CATEGORICAL VARIABLES AVAILABLE**")

        
def Multi_Variate_Analysis(df):
    d=df.columns.to_list()
    for i in df:
        if df[i].dtypes == "object" :
            d.remove(df[i].name)
        if df[i].dtypes != "object" :
            if df[i].nunique() <5:
                d.remove(df[i].name)
    warnings.filterwarnings(action="ignore")
    mlt = f'<p style="font-family:sans-serif; font-size: 18px;">MultiVariate Analysis</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{mlt}</h1>**", unsafe_allow_html=True)

    f=round(df.loc[0:,d].corr(),2)
    targetvar=[]
    for i in df:
        if df[i].dtypes != "object" :
            if df[i].nunique()>5 :
                targetvar.append(df[i].name)
    if len(targetvar)>0:
        rowmul1,rowmulsp, rowmul2,rowmulsp1  = st.columns((2,.5,4,.2))
        with rowmul1:
            target = st.selectbox("Select Target Variable",targetvar)
            threshold =st.number_input('Select Correlation Threshold Value',min_value=0.30, max_value=1.00,step=0.05)
            #threshold=threshold+0.01
            #st.write('The current movie title is', val)
            #if st.checkbox("Observations"):
            new_title1 = f'<p style="font-family:sans-serif; color:steelblue; font-size: 16px;">Observations :</p>'
            st.markdown(f"**{new_title1}**", unsafe_allow_html=True)
            st.write(f'**<FONT color="Green">‎ ‎ ‎ ‎ Correlation check with Target variable‎ ‎ ‎ ‎</FONT>**',f'**<FONT color="#FC7726">{df[target].name}</FONT>**',unsafe_allow_html=True)
#             titl=f"Correlation check with Target variable {df[target].name}"
#             new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 17px;">{titl}</p>'
#             st.markdown(f"<h1 style='text-align: center; color: black;'>{new_title}</h1>", unsafe_allow_html=True)

            h=f[df[target].name][(f[df[target].name].values>=threshold) & (f[df[target].name].values<1)]
            if h.any():
                a = f[df[target].name][(f[df[target].name].values>=threshold) & (f[df[target].name].values<1)]
                t=pd.DataFrame(a)
                ind = t.index.tolist()
                lis1=' ‎ ‎,‎ ‎ '.join(ind)
                st.write(f'**<FONT color="#FC7726">►‎ ‎ {df[target].name}</FONT>**','‎ ‎is highly correlated with‎ ‎',f'**<FONT color="steelblue">{lis1}</FONT>**',unsafe_allow_html=True)
                #st.write(f"- **{df[target].name} :**  highly correlated with **{', '.join(ind)}**")
            else:
                st.write(f'**<FONT color="#FC7726">►‎ ‎ {df[target].name}</FONT>**','‎ ‎is not correlated with any variable</FONT>',unsafe_allow_html=True)

            f=round(df.loc[0:,d].corr(),2)
            st.write("")
            titl="Correlation check between All variables"
            new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 17px;">{titl}</p>'
            st.markdown(f"<h1 style='text-align: center; color: black;'>{new_title}</h1>", unsafe_allow_html=True)

            e = (f.values>=threshold) &(f.values<0.999)
            if e.any() :
                for i in f:
                    h=f[i][(f[i].values>=threshold) & (f[i].values<1)]
                    if h.any():
                        a = f[i][(f[i].values>=threshold) & (f[i].values<1)]
                        t=pd.DataFrame(a)
                        ind = t.index.tolist()

                        lis2=' ‎ ‎,‎ ‎ '.join(ind)
                        st.write(f'**<FONT color="#FC7726">►‎ ‎ {f[i].name}</FONT>**','‎ ‎is highly correlated with‎ ‎',f'**<FONT color="steelblue">{lis2}</FONT>**',unsafe_allow_html=True)

            else:
                st.write(f'**<FONT color="#FC7726">►‎ ‎ No correlation Exists between Variables</FONT>**',unsafe_allow_html=True)

        with rowmul2:
            st.write("##")
            st.warning("**Select Threshold value of your choice, e.g 0.8, 0.7 or 0.6 etc. if the correlation coefficient value between two variables is greater than or equal to threshold value, then they are highly correlated.**")
            st.warning("**Pairplot takes more time. ‎ ‎Better go with Heatmap. ‎ ‎ If Heatmap is not clear, ‎  go with correlation Matrix table.**")
            st.write("##")
            if st.checkbox("Pairplot"):
                colnum=[]
                for i in df:
                    if (df[i].dtypes!="object"):   
                        colnum.append(df[i].name)
                if len(colnum)>0:
                    fig, ax = plt.subplots()
                    fig=sns.pairplot(df.loc[0:,d])
                    st.pyplot(fig)
                else:
                    st.write('**NO NUMERIC VARIABLE IS AVAILABLE**')
            st.write("")

            if st.checkbox("Heatmap"):
                colnum=[]
                for i in df:
                    if (df[i].dtypes!="object"):   
                        colnum.append(df[i].name)
                if len(colnum)>0:
                    fig, ax = plt.subplots()
                    fig = plt.figure(figsize=(df.loc[0:,d].shape[1],df.loc[0:,d].shape[1]*0.7))
                    heat=sns.heatmap(df.loc[0:,d].corr(),annot=True,fmt='0.2f')
                    plt.title("correlation heat map \n",fontsize=10)
                    plt.xticks(rotation= 90,fontsize=15)
                    plt.yticks(rotation= 360,fontsize=15)
                    #plt. tight_layout()
                    st.pyplot(fig)
                else:
                    st.write('**NO NUMERIC VARIABLE IS AVAILABLE**')

            st.write("")        
            if st.checkbox("Correlation Matrix Table"):
                colnum=[]
                for i in df:
                    if (df[i].dtypes!="object"):   
                        colnum.append(df[i].name)
                if len(colnum)>0:
                    st.table(df.loc[0:,d].corr().style.background_gradient(cmap='coolwarm').set_precision(2).set_table_styles(styles))

                else:
                    st.write('**NO NUMERIC VARIABLE IS AVAILABLE**')
    else:
        st.warning('**NO NUMERIC VARIABLE IS AVAILABLE**')
        
        
        
def Group_By(df):
    abtdf = f'<p style="font-family:sans-serif; font-size: 18px;">Group By</p>'
    st.write(f"**<h1 style='text-align: center;'>{abtdf}</h1>**", unsafe_allow_html=True)
    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            colnum.append(df[i].name)
    rowmul1,rowmulsp, rowmul2,rowmulsp1  = st.columns((2,.5,4,.2))
    with rowmul1:
        columns = df.columns.tolist()
        colnum1=colnum       
        Agg_fun = ["count","sum","mean","median","min","max","std","var"]

        All = st.form(key = 'Options')
        Group_By = All.multiselect("Select one or more Variables for Group By:",columns)
        Agg_column = All.multiselect("Select one or more Aggregate Columns:",colnum1)
        Agg_functions = All.multiselect("Select Aggregate Functions:",Agg_fun)
        submit_button = All.form_submit_button(label='Submit')
        
        if len(Group_By) == 0 and len(Agg_column) == 0 and  len(Agg_functions) == 0:
            with rowmul2:
                st.warning("**Please select Group By column**")
            
        else:       
            if "load_state" not in st.session_state:
                    st.session_state.load_state = False

            if submit_button or st.session_state.load_state:
                st.session_state.load_state = True

                with rowmul2:
                    hide_table_groupby = """
                                    <style>
                                    tbody th {display:none}
                                    .blank {display:none}
                                    </style>
                                    """
                    # Inject CSS with Markdown
                    st.markdown(hide_table_groupby, unsafe_allow_html=True)

                    if len(Group_By) and len(Agg_column) and len(Agg_functions) > 0:

                        gkk = df.groupby(by=Group_By,as_index=False)[Agg_column].agg(Agg_functions).reset_index()
                        gkk.columns = ['_'.join(col) for col in gkk.columns.values]
                        st.table(gkk.style.set_precision(2).set_table_styles(styles))

                    elif len(Group_By) == 1 and len(Agg_column) == 0 and len(Agg_functions) == 0 :
                        targetvar = df[Group_By[0]].value_counts().index.tolist()
                        target = st.selectbox(f"Select {Group_By[0]} Group",targetvar)
                        gkk = df.groupby(by=Group_By,as_index=False)
                        st.table(gkk.get_group(target).style.set_table_styles(styles))

                    elif len(Group_By) > 1 and len(Agg_column) == 0 and len(Agg_functions) == 0 :
                        groups = []
                        targetvar = df[Group_By[0]].value_counts().index.tolist()
                        target = st.selectbox(f"Select {Group_By[0]} Group",targetvar)
                        groups.append(target)

                        j= 0
                        while j < len(Group_By) :

                            targetvar1 = df[Group_By[j+1]][df[Group_By[j]]==groups[-1]].value_counts().index.tolist()

                            target1 = st.selectbox(f"Select {Group_By[j+1]} Group",targetvar1)
                            groups.append(target1)
                            if j == len(Group_By)-2:
                                break
                            j= j+1

                        gkk = df.groupby(by=Group_By,as_index=False)
                        st.table(gkk.get_group(tuple(groups)).style.set_table_styles(styles))

                    elif len(Group_By) == 0 and len(Agg_column) >0 and  len(Agg_functions) > 0 :
                        st.warning("**Please select Group By column**")

                    elif len(Group_By) == 0 and len(Agg_column) == 0 and  len(Agg_functions) == 0:
                        st.warning("**Please select Group By column**")

                    elif len(Group_By) ==0 and len(Agg_column) >=1 and  len(Agg_functions) >= 0 :
                        st.warning("**Please select Group By column**")

                    elif len(Group_By)>1 and len(Agg_column) ==1 and  len(Agg_functions) == 0 :
                        groups = []
                        targetvar = df[Group_By[0]].value_counts().index.tolist()
                        target = st.selectbox(f"Select {Group_By[0]} Group",targetvar)
                        groups.append(target)

                        j= 0
                        while j < len(Group_By) :

                            targetvar1 = df[Group_By[j+1]][df[Group_By[j]]==groups[-1]].value_counts().index.tolist()

                            target1 = st.selectbox(f"Select {Group_By[j+1]} Group",targetvar1)
                            groups.append(target1)
                            if j == len(Group_By)-2:
                                break
                            j= j+1

                        gkk = df.groupby(Group_By)[Agg_column[-1]]
                        gkk = pd.DataFrame(gkk.get_group(tuple(groups)))
                        gkk = gkk.reset_index(drop=True)
                        grp_cols = []
                        for i in range(len(Group_By)):
                             grp_cols.append(pd.DataFrame({Group_By[i]:[groups[i]] * gkk.shape[0]}))
                        all = pd.concat(grp_cols,axis=1)
                        final = pd.concat([all,gkk],axis=1)
                        st.table(final.style.set_table_styles(styles))

                    elif len(Group_By) == 1 and len(Agg_column) == 1 and  len(Agg_functions) == 0 :
                        targetvar = df[Group_By[0]].value_counts().index.tolist()
                        target = st.selectbox(f"Select {Group_By[0]} Group",targetvar)
                        gkk = df.groupby(Group_By)[Agg_column[-1]]
                        k = pd.DataFrame(gkk.get_group(target))
                        k = k.reset_index(drop=True)
                        l = pd.DataFrame({target:[target] * k.shape[0]})
                        all = pd.concat([l,k],axis=1)
                        st.table(all.style.set_table_styles(styles))


                    elif len(Group_By) == 0 and len(Agg_column) == 0 and  len(Agg_functions) > 0 :
                        st.warning("**Please select Group By column and Aggregate column**")

                    elif len(Group_By) >= 1 and len(Agg_column) == 0 and  len(Agg_functions) > 1 :
                        st.warning("**Please select Aggregate column**")

                    elif len(Group_By) == 1 and len(Agg_column) == 0 and len(Agg_functions) == 1 :
                        if Agg_functions[0] == 'count' :
                            gkk = df.groupby(by=Group_By,as_index=False).count()
                            st.table(gkk.style.set_table_styles(styles))
                        elif Agg_functions[0] == 'sum':
                            gkk = df.groupby(by=Group_By,as_index=False).sum()
                            st.table(gkk.style.set_table_styles(styles))
                        elif Agg_functions[0] == 'mean':
                            gkk = df.groupby(by=Group_By,as_index=False).mean()
                            st.table(gkk.style.set_precision(2).set_table_styles(styles))
                        elif Agg_functions[0] == 'median':
                            gkk = df.groupby(by=Group_By,as_index=False).median()
                            st.table(gkk.style.set_precision(2).set_table_styles(styles))
                        elif Agg_functions[0] == 'min':
                            gkk = df.groupby(by=Group_By,as_index=False).min()
                            st.table(gkk.style.set_table_styles(styles))
                        elif Agg_functions[0] == 'max':
                            gkk = df.groupby(by=Group_By,as_index=False).max()
                            st.table(gkk.style.set_table_styles(styles))
                        elif Agg_functions[0] == 'std':
                            gkk = df.groupby(by=Group_By,as_index=False).std()
                            st.table(gkk.style.set_precision(2).set_table_styles(styles))
                        elif Agg_functions[0] == 'var':
                            gkk = df.groupby(by=Group_By,as_index=False).var()
                            st.table(gkk.style.set_precision(2).set_table_styles(styles))

                    elif len(Group_By) > 1 and len(Agg_column) == 0 and  len(Agg_functions) == 1 :
                        if Agg_functions[0] == 'count' :
                            gkk = df.groupby(by=Group_By,as_index=False).count()
                            st.table(gkk)
                        elif Agg_functions[0] == 'sum':
                            gkk = df.groupby(by=Group_By,as_index=False).sum()
                            st.table(gkk)
                        elif Agg_functions[0] == 'mean':
                            gkk = df.groupby(by=Group_By,as_index=False).mean()
                            st.table(gkk.style.set_precision(2).set_table_styles(styles))
                        elif Agg_functions[0] == 'median':
                            gkk = df.groupby(by=Group_By,as_index=False).median()
                            st.table(gkk.style.set_precision(2).set_table_styles(styles))
                        elif Agg_functions[0] == 'min':
                            gkk = df.groupby(by=Group_By,as_index=False).min()
                            st.table(gkk.style.set_table_styles(styles))
                        elif Agg_functions[0] == 'max':
                            gkk = df.groupby(by=Group_By,as_index=False).max()
                            st.table(gkk.style.set_table_styles(styles))
                        elif Agg_functions[0] == 'std':
                            gkk = df.groupby(by=Group_By,as_index=False).std()
                            st.table(gkk.style.set_precision(2).set_table_styles(styles))
                        elif Agg_functions[0] == 'var':
                            gkk = df.groupby(by=Group_By,as_index=False).var()
                            st.table(gkk.style.set_precision(2).set_table_styles(styles))
#         else:
#             with rowmul2:
#                 st.warning("**Please select Group By column**")
                        
                        
def Transformations(df):
    trnsfor = f'<p style="font-family:sans-serif; font-size: 18px;">Transformations</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{trnsfor}</h1>**", unsafe_allow_html=True)
    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colnum.append(df[i].name)
    if len(colnum)>0:
        skewed=[]
        rowtr1,rowtrsp, rowtr2,rowtrsp1,rowtrsp2  = st.columns((1,.1,2.9,.5,1.5))
        with rowtr1:
            col = st.selectbox("SELECT VARIABLE",colnum)
        with rowtr2:
            st.write("##")
            st.info('**Make sure your Variable has Non-Zero Values and no Negative values to avoid error**')
        with rowtrsp2:
            st.markdown("**Hint:-**")
            st.markdown("**If Mean > Median : Right Skewed**")
            st.markdown("**If Mean < Median : Left Skewed**")
        rowtr11,rowtrsp1, rowtr12,rowtrsp12  = st.columns((4,.1,1,.2))
        with rowtr11:

            warnings.filterwarnings("ignore")
            st.write(f'**<FONT color="steelblue">Default Distribution</FONT>**',unsafe_allow_html=True)
            if  df[col].mean() == df[col].median():
                st.write(f"**Skewness : {df[col].skew():.2f}‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Mean : {df[col].mean():.2f} ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Median : {df[col].median():.2f}‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ (Distribution Seems to be Normal Distributed)**")
            elif  df[col].mean() > df[col].median():
                st.write(f"**Skewness : {df[col].skew():.2f}‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Mean : {df[col].mean():.2f} ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Median : {df[col].median():.2f}‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ (Distribution Seems to be Right Skewed)**")
            else:
                st.write(f"**Skewness : {df[col].skew():.2f}‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Mean : {df[col].mean():.2f} ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ Median : {df[col].median():.2f}‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ (Distribution Seems to be Left Skewed)**")

            fig, ax = plt.subplots()
            fig = plt.figure(figsize=(15,3.5))

            plt.subplot(141)
            ot=sns.boxplot(df[col])
            title= "Boxplot for {}"
            plt.title(title.format(df[col].name),fontsize=15)
            plt.xlabel(df[col].name, fontsize=15)

            plt.subplot(142)
            kdeorg=sns.distplot(df[col],fit=norm,fit_kws={"color":"red"})
            plt.xlabel(df[col].name,fontsize=15)
            plt.subplot(143)
            histiorg=sns.histplot(df[col])
            plt.xlabel(df[col].name,fontsize=15)
            plt.subplot(144)
            sc.probplot(df[col],plot=plt);
            plt.xlabel("Theoretical Quantiles",fontsize=15)
            plt.title("probability Plot",fontsize=15)
            plt. tight_layout()
            st.pyplot(fig)

            with rowtr12:
                st.write("##")
                st.warning("**Based on Default Distribution, ‎ ‎Select Right or Left Skewed to see the Transformed Distributions**")
                st.write("#")
                choice = st.radio("Select Distribution",('None','Right Skewed','Left Skewed'))
                if choice=='None':
                    if st.button('Submit'):
                        skewed.append('None')
                if choice=='Right Skewed':
                    if st.button('Submit'):
                        skewed.append('Right Skewed')
                if choice=='Left Skewed':
                    if st.button('Submit'):
                        skewed.append('Left Skewed')

        if 'None' in skewed:
            st.write("")
        elif 'Right Skewed' in skewed:
            st.write("##")
            st.write("##")
            trnsfor1 = f'<p style="font-family:sans-serif; font-size: 18px;">Distributions After Transformations</p>'
            st.markdown(f"**<h1 style='text-align: center; '>{trnsfor1}</h1>**", unsafe_allow_html=True)
            rowtr3,rowtrsp, rowtr4,rowtrsp4  = st.columns((2,.2,2,.2))
            with rowtr3:
                sqrt = f'<p style="font-family:sans-serif;color:steelblue; font-size: 15px;">Sqrt Transformation</p>'
                st.markdown(f"**<h1 style='text-align: center; '>{sqrt}</h1>**", unsafe_allow_html=True)
                fig, ax = plt.subplots()
                fig = plt.figure(figsize=(15,5))
                st.write(f"**Sqrt({df[col].name})‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎Skewness : {np.sqrt(df[col]).skew():.3f}**")
                plt.subplot(131)
                sqrtkde=sns.distplot(np.sqrt(df[col]),fit=norm,fit_kws={"color":"red"})
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(132)
                sqrthist=plt.hist(np.sqrt(df[col]))
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(133)
                sc.probplot(np.sqrt(df[col]),plot=plt);
                plt.title("probability Plot",fontsize=20)
                plt. tight_layout()
                st.pyplot(fig)

            with rowtr4:
                log = f'<p style="font-family:sans-serif;color:steelblue; font-size: 15px;">log10 Transformation</p>'
                st.markdown(f"**<h1 style='text-align: center; '>{log}</h1>**", unsafe_allow_html=True)
                fig, ax = plt.subplots()
                fig = plt.figure(figsize=(15,5))
                st.write(f"**log10({df[col].name})‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎Skewness : {np.log10(df[col]+0.0001).skew():.3f}**")
                plt.subplot(131)
                sns.distplot(np.log10(df[col]+0.0001),fit=norm,fit_kws={"color":"red"})
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(132)
                plt.hist(np.log10(df[col]+0.0001))
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(133)
                sc.probplot(np.log10(df[col]+0.0001),plot=plt);
                plt.title("probability Plot",fontsize=20)
                plt. tight_layout()
                st.pyplot(fig)

            rowtr5,rowtrsp, rowtr6,rowtrsp4  = st.columns((2,.2,2,.2))
            with rowtr5:
                st.write("")
                inv = f'<p style="font-family:sans-serif;color:steelblue; font-size: 15px;">Inverse Transformation</p>'
                st.markdown(f"**<h1 style='text-align: center; '>{inv}</h1>**", unsafe_allow_html=True)
                fig, ax = plt.subplots()
                fig = plt.figure(figsize=(15,5))
                st.write(f"**1/({df[col].name})‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎Skewness : {(1/(df[col]+0.0001)).skew():.3f}**")
                plt.subplot(131)
                sns.distplot(1/(df[col]+0.0001),fit=norm,fit_kws={"color":"red"})
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(132)
                plt.hist(1/(df[col]+0.0001))
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(133)
                sc.probplot(1/(df[col]+0.0001),plot=plt);
                plt.title("probability Plot",fontsize=20)
                plt. tight_layout()
                st.pyplot(fig)

            with rowtr6:
                st.write("")
                cox = f'<p style="font-family:sans-serif;color:steelblue; font-size: 15px;">Boxcox Transformation</p>'
                st.markdown(f"**<h1 style='text-align: center; '>{cox}</h1>**", unsafe_allow_html=True)
                fig, ax = plt.subplots()
                fig = plt.figure(figsize=(15,5))
                st.write(f"**Skewness : {pd.Series(sc.boxcox(df[col]+0.0001)[0]).skew():.3f}**")
                plt.subplot(131)
                sns.distplot(sc.boxcox(df[col]+0.0001)[0],fit=norm,fit_kws={"color":"red"})
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(132)
                plt.hist(sc.boxcox(df[col]+0.0001)[0])
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(133)
                sc.probplot(sc.boxcox(df[col]+0.0001)[0],plot=plt);
                plt.title("probability Plot",fontsize=20)
                plt. tight_layout()
                st.pyplot(fig)

        elif 'Left Skewed' in skewed:
            trnsfor1 = f'<p style="font-family:sans-serif; font-size: 18px;">Distributions After Transformations</p>'
            st.markdown(f"**<h1 style='text-align: center; '>{trnsfor1}</h1>**", unsafe_allow_html=True)
            rowtr3,rowtrsp, rowtr4,rowtrsp4  = st.columns((2,.2,2,.2))
            with rowtr3:
                sqrt = f'<p style="font-family:sans-serif;color:steelblue; font-size: 15px;">Sqrt Transformation</p>'
                st.markdown(f"**<h1 style='text-align: center; '>{sqrt}</h1>**", unsafe_allow_html=True)
                fig, ax = plt.subplots()
                fig = plt.figure(figsize=(15,5))
                st.write(f"**Sqrt(max({df[col].name}+1)-{df[col].name})‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎Skewness : {np.sqrt(max(df[col]+1)-df[col]).skew():.3f}**")
                plt.subplot(131)
                sns.distplot(np.sqrt(max(df[col]+1)-df[col]),fit=norm,fit_kws={"color":"red"})
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(132)
                plt.hist(np.sqrt(max(df[col]+1)-df[col]))
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(133)
                sc.probplot(np.sqrt(max(df[col]+1)-df[col]),plot=plt);
                plt.title("probability Plot",fontsize=20)
                plt. tight_layout()
                st.pyplot(fig)

            with rowtr4:
                log = f'<p style="font-family:sans-serif;color:steelblue; font-size: 15px;">log10 Transformation</p>'
                st.markdown(f"**<h1 style='text-align: center; '>{log}</h1>**", unsafe_allow_html=True)
                fig, ax = plt.subplots()
                fig = plt.figure(figsize=(15,5))
                st.write(f"**log10(max({df[col].name}+1)-{df[col].name})‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎Skewness : {np.log10(max(df[col]+1)-df[col]).skew():.3f}**")
                plt.subplot(131)
                sns.distplot(np.log10(max(df[col]+1)-df[col]),fit=norm,fit_kws={"color":"red"})
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(132)
                plt.hist(np.log10(max(df[col]+1)-df[col]))
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(133)
                sc.probplot(np.log10(max(df[col]+1)-df[col]),plot=plt);
                plt.title("probability Plot",fontsize=20)
                plt. tight_layout()
                st.pyplot(fig)

            rowtr5,rowtrsp, rowtr6,rowtrsp4  = st.columns((2,.2,2,.2))
            with rowtr5:
                st.write("")
                inv = f'<p style="font-family:sans-serif;color:steelblue; font-size: 15px;">Inverse Transformation</p>'
                st.markdown(f"**<h1 style='text-align: center; '>{inv}</h1>**", unsafe_allow_html=True)                    
                fig, ax = plt.subplots()
                fig = plt.figure(figsize=(15,5))
                st.write(f"**1/(max({df[col].name}+1)-{df[col].name})‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎Skewness : {(1/(max(df[col]+1)-df[col])).skew():.3f}**")
                plt.subplot(131)
                dis= (1/(max(df[col]+1)-df[col]))
                sns.distplot(dis,fit=norm,fit_kws={"color":"red"})
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(132)
                plt.hist(1/(max(df[col]+1)-df[col]))
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(133)
                sc.probplot(1/(max(df[col]+1)-df[col]),plot=plt);
                plt.title("probability Plot",fontsize=20)
                plt. tight_layout()
                st.pyplot(fig)

            with rowtr6:
                st.write("")
                cox = f'<p style="font-family:sans-serif;color:steelblue; font-size: 15px;">Boxcox Transformation</p>'
                st.markdown(f"**<h1 style='text-align: center; '>{cox}</h1>**", unsafe_allow_html=True)                    
                fig, ax = plt.subplots()
                fig = plt.figure(figsize=(15,5))
                st.write(f"**Skewness : {pd.Series(sc.boxcox(df[col])[0]).skew():.3f}**")
                plt.subplot(131)
                sns.distplot(sc.boxcox(df[col])[0],fit=norm,fit_kws={"color":"red"})
                plt.xlabel(df[col].name,fontsize=15)
                plt.subplot(132)
                plt.hist(sc.boxcox(df[col])[0])

                plt.subplot(133)
                sc.probplot(sc.boxcox(df[col])[0],plot=plt);
                plt.title("probability Plot",fontsize=20)
                plt. tight_layout()
                st.pyplot(fig)
    else:
        st.warning('**NO NUMERIC VARIABLE IS AVAILABLE**')
        
        
        
def Exp1(df):
    if 'type' not in st.session_state:
        st.session_state['type'] ='Categorical'
        
    colcatx=[]
    colconty=[]
    for i in df:
        if df[i].dtypes == "object" :
            #if df[i].nunique()<=50:
            if df[i].nunique()>0:
                colcatx.append(df[i].name)

        if df[i].dtypes != "object" :
            if df[i].nunique() <=5 :
                colcatx.append(df[i].name)

        if (df[i].dtypes!="object"):
            if df[i].nunique()>5 :
                colconty.append(df[i].name)
                
    types = {'Categorical':colcatx,'Numerical':colconty}
    
    column = st.selectbox('Select a column', types[st.session_state['type']])
    
    def handle_click(new_type):
        st.session_state.type = new_type
        
    def handle_click_wo_button():
        if st.session_state.kind_of_column:
            st.session_state.type = st.session_state.kind_of_column
            
    type_of_column = st.radio('what kind analysis',['Categorical','Numerical'],on_change = handle_click_wo_button,key = 'kind_of_column')
    
    if st.session_state['type'] == 'Categorical':
        dist = pd.DataFrame(df[column].value_counts()).head(20)
        st.bar_chart(dist)
        
    else:
        st.line_chart(df[[column]])


def Exp2(df,col='price'):
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])

    # Plot!
    st.plotly_chart(fig, use_container_width=True)



    
def Exp3(df):
#     age = st.slider('How old are you?', 0, 130, 25)
#     st.write("I'm ", age, 'years old')
#     values = st.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))
#     st.write('Values:', values)
#     from datetime import time
#     appointment = st.slider("Schedule your appointment:",value=(time(11, 30), time(12, 45)))
#     st.write("You're scheduled for:", appointment)
#     from datetime import datetime
#     start_time = st.slider("When do you start?",value=(datetime(2020, 1, 1, 0, 0,0),datetime(2025, 1, 1, 0, 0,0)),format="DD/MM/YY - hh:mm:ss")
#     #start_time = st.slider("When do you start?",value=datetime('2011-01-01 02:00:00'),format="MM/DD/YY - hh:mm")
#     st.write("Start time:", start_time)


    colnum=[]
    for i in df:
        if (df[i].dtypes!="object"):
            if (df[i].nunique()) >5 :
                colnum.append(df[i].name)
    rowscat1,rowscatsp, rowscat2  = st.columns((1,0.1,4))
    if len(colnum)>0:
        with rowscat1:
            line = st.form(key = 'Options')
            x = line.multiselect("Select One or More Continuous Variables",colnum)
            time = df.columns.tolist()
            y = line.selectbox("Time Stamped Variable",time)
            submit_button_l = line.form_submit_button(label='Submit')
        with rowscat2:
            mul_button = st.radio("",options = ['Head of Dataset','Tail of Dataset'])
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
            if mul_button=='Head of Dataset':
                st.table(df.head(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            elif mul_button=='Tail of Dataset':
                st.table(df.tail(5).style.set_precision(2).applymap(lambda x: f"color: {'red' if isinstance(x,str) else None}").set_table_styles(styles))
            
            if "load_stateline" not in st.session_state:
                st.session_state.load_stateline = False  
            
            if submit_button_l or st.session_state.load_stateline:
                st.session_state.load_stateline = True
                if x:
                    df.Timestamp = pd.to_datetime(df[y].astype(str),infer_datetime_format=True) 
                    df.index = df.Timestamp
                    df.sort_index(axis = 0,inplace=True)
                    with rowscat1:
                        l = pd.DataFrame(df.index.to_list())
                        l[0] = l[0].astype(str)
                        time_list = l[0].to_list()
                        time_list.insert(0,'None')
                        time_list1 = l[0].to_list()
                        time_list1.reverse()
                        time_list1.insert(0,'None')
                        line2 = st.form(key = 'Options2')
                        up = line2.selectbox("start",time_list)
                        lo = line2.selectbox("end",time_list1)
                        submit_button_l2 = line2.form_submit_button(label='Select Date Time Range')

                    if len(x) == 1:
                        if submit_button_l2 or st.session_state.load_stateline:
                            st.session_state.load_stateline = True
                            if (up!='None') and (lo!='None'):
                                df = df.loc[up:lo]
                            else:
                                df=df
                        else:
                            df= df
                        fig = px.line(df, x=df.index, y=x)
                        fig.update_layout(xaxis_title=f"{y}",yaxis_title=f"{x[0]}")
                        fig.update_layout(title_text=f"{x[0]} by {y}",title={
                                            'y':0.92,
                                            'x':0.5,
                                            'xanchor': 'center',
                                            'yanchor': 'top'},title_font_color="red")
                        fig.update_xaxes(rangeslider_visible=True)
                        fig.update_layout(
                                        autosize=False,
                                        width=1100,
                                        height=500)
                        with rowscat2:
                            st.plotly_chart(fig)
                            
                    else:
                        if submit_button_l2 or st.session_state.load_stateline:
                            st.session_state.load_stateline = True
                            if (up!='None') and (lo!='None'):
                                df = df.loc[up:lo]
                            else:
                                df=df
                        else:
                            df=df
                        fig = px.line(df, x=df.index, y=x)
                        fig.update_layout(xaxis_title=f"{y}")
                        fig.update_xaxes(rangeslider_visible=True)
                        fig.update_layout(
                                        autosize=False,
                                        width=1100,
                                        height=500)
                        with rowscat2:
                            st.plotly_chart(fig)          
                else:
                    with rowscat2:
                        st.write("##")
                        st.warning("**SELECT CONTINUOUS VARIABLE**")
    else:
        st.warning("**NO CONTINUOUS VARIABLE AVAILABLE**")
    
    
