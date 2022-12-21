import base64
from TimeSaver_Functions import *
#from TimeSaver_Functions_full import *
import streamlit as st
import hydralit_components as hc
from PIL import Image

img=Image.open('download.png')

st.set_page_config(page_title = 'TimeSaver - EDA',layout="wide",page_icon=img)

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.markdown(custom_streamlit_named_footer, unsafe_allow_html=True)

#st.markdown(custom_streamlit_linkedin_footer, unsafe_allow_html=True)

st.markdown(CSS_Adjustments, unsafe_allow_html=True)

upload1,uploadsp,upload2 = st.columns((2,.1,2))

with upload1:
    
    ttl = f'<p style="font-family:cursive; font-size: 30px;">TimeSaver!</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{ttl}</h1>**", unsafe_allow_html=True)
    st.markdown("**TimeSaver is a Semi-Automated Exploratory Data Analysis Web App which can save lot of time and efforts from writting code for basic visualizations and statistical analysis. It helps in finding meaningful insights by doing preliminary analysis.‎ ‎ ‎ ‎ ‎(‎ ‎Made By [RAVINDER](https://www.linkedin.com/in/ravinder-j-37849b244/)‎ ‎)‎ ‎ ‎ ‎ ‎[Email](mailto:timesaver.ds@gmail.com)**")
    
with upload2:
    data = st.file_uploader("Upload Clean Dataset", type=["csv"])
    
if data is not None:
    import pandas as pd
    df = pd.read_csv(data,encoding='latin-1').iloc[0:500000,:]
    #df = pd.read_csv(data).iloc[0:500000,:]
    data_name = f'<p style="font-family:sans-serif; color:#AC123E;font-size: 22px;">{data.name.split(".")[0]}</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{data_name}</h1>**", unsafe_allow_html=True)
    
    option_data = [
        {'icon': "", 'label':"About Dataset"},
        {'icon': "",'label':"Missing Values"},
        {'icon': "", 'label':"Outliers"},
        {'icon': "", 'label':"Uni & Bi-Variate Analysis"},
        {'icon': "", 'label':"Multi Variate Analysis"},
        {'icon': "", 'label':"Time Series Analysis"},
        {'icon': "", 'label':"Group By"},
        {'icon': "", 'label':"Transformations"}]#,
        #{'icon': "", 'label':"Full Report"}]#,
        #{'icon': "", 'label':"Exp2"}]

    over_theme = {'txc_inactive': '#FFFFFF'}
    font_fmt = {'font-class':'h2','font-size':'150%'}
    menu_id = hc.option_bar(option_definition=option_data,override_theme=over_theme,
                            font_styling=font_fmt,key='PrimaryOption',horizontal_orientation=True)

    if menu_id == "About Dataset":
        About_Dataset(df)
                
    if menu_id == "Missing Values":
        Missing_values(df)

    if menu_id == "Outliers":
        Outliers(df)

    if menu_id == "Uni & Bi-Variate Analysis":
        option2_data = [
            {'icon':"",'label':"Univariate Categorical"},
            {'icon': "", 'label':"Univariate Continuous"},
            {'icon': "", 'label':"Bivariate Continuous Vs Continuous"},
            {'icon': "", 'label':"Bivariate Continuous Vs Categorical"},
            {'icon': "", 'label':"Bivariate Categorical Vs Categorical"}]
        
        over_theme = {'txc_inactive': '#FFFFFF'}
        font_fmt = {'font-class':'h2','font-size':'150%'}
        menu_id2 = hc.option_bar(option_definition=option2_data,override_theme=over_theme,
                                 font_styling=font_fmt,horizontal_orientation=True)

        if menu_id2 == "Univariate Categorical":
            Univariate_Categorical(df)
            
        if menu_id2 == "Univariate Continuous":
            Univariate_Continuous(df)

        if menu_id2 == "Bivariate Continuous Vs Continuous":
            Bivariate_Continuous_Vs_Continuous(df)            

        if menu_id2 == "Bivariate Continuous Vs Categorical":
            Bivariate_Continuous_Vs_Categorical(df)
            
        if menu_id2 == "Bivariate Categorical Vs Categorical":
            Bivariate_Categorical_Vs_Categorical(df)            
            
    if menu_id == "Multi Variate Analysis":
        Multi_Variate_Analysis(df)
        
    if menu_id == "Time Series Analysis":
        option3_data = [
            {'icon':"",'label':"Line Plot"},
            {'icon':"",'label':"Time Resampling"},
            {'icon': "", 'label':"ETS Decomposition"},
            {'icon': "", 'label':"Stationarity Check"},
            {'icon': "", 'label':"ACF and PACF Plots"}]#,
            #{'icon': "", 'label':"Exp2"}]

        over_theme = {'txc_inactive': '#FFFFFF'}
        font_fmt = {'font-class':'h2','font-size':'150%'}
        menu_id3 = hc.option_bar(option_definition=option3_data,override_theme=over_theme,
                                 font_styling=font_fmt,horizontal_orientation=True)

        if menu_id3 == "Line Plot":
            Line_Plot(df)
            
        if menu_id3 == "Time Resampling":
            Time_Resampling(df)
            
        if menu_id3 == "ETS Decomposition":
            ETS_Decomposition(df)
            
        if menu_id3 == "Stationarity Check":
            Stationarity_Check(df)
        
        if menu_id3 == "ACF and PACF Plots":
            ACF_PACF(df)
            
#         if menu_id3 == "Exp2":
#             Exp2(df)
               
        
    if menu_id == "Group By":
        Group_By(df)
         
    if menu_id == "Transformations":
        Transformations(df)
        
    if menu_id == "Full Report":
        full (df)
        #About_Dataset(df)
        #st.write("*-"*280)
        #Missing_values(df)
        #st.write("*-"*280)
        #Outliers_full(df)
        #Univariate_Continuous_full(df)
        #Univariate_Categorical_full(df)
        
        
    if menu_id == "Exp1":
        Exp1(df)
        
    if menu_id == "Exp2":
        Exp2(df,col='price')
        
    if menu_id == "Exp3":
        Exp3(df)
                 
else:
    option_data = [
        {'icon': "", 'label':"About Dataset"},
        {'icon': "",'label':"Missing Values"},
        {'icon': "", 'label':"Outliers"},
        {'icon': "", 'label':"Uni & Bi-Variate Analysis"},
        {'icon': "", 'label':"Multi Variate Analysis"},
        {'icon': "", 'label':"Time Series Analysis"},
        {'icon': "", 'label':"Group By"},
        {'icon': "", 'label':"Transformations"}]#,
        #{'icon': "", 'label':"Full Report"}]

    over_theme = {'txc_inactive': '#FFFFFF'}
    font_fmt = {'font-class':'h2','font-size':'150%'}
    menu_id = hc.option_bar(option_definition=option_data,override_theme=over_theme,
                            font_styling=font_fmt,key='PrimaryOption',horizontal_orientation=True)
    rowh1,rowhsp, rowh2  = st.columns((2,.3,2))
    with rowh1:
        from PIL import Image
        img = Image.open("3d-ManCSV2.png")
        st.image(img)
        
    with rowh2:
        st.write('##')
        st.write('##')
        instruct = f'<p style="font-family:sans-serif;color:steelblue; font-size: 15px;">INSTRUCTIONS</p>'
        st.markdown(f"**<h1 style='text-align: left; '>{instruct}</h1>**", unsafe_allow_html=True)         
        st.write('- **It accepts only CSV format file of size maximum 200MB**')
        st.write('- **It accepts only 5 Lac Rows in the dataset even if the data has more more than 5 Lac Rows**')
        st.write('- **Dataset should be free from special characters for better Analysis**')
        
    quote = f'<p style="font-family:cursive;color:blue; font-size: 20px;">\" Data will talk to you if you are willing to listen \"</p>'
    st.markdown(f"**<h1 style='text-align: center; '>{quote}</h1>**", unsafe_allow_html=True)   
        
# social1,social2,social3 = st.columns((2,2,2))
# icon_size=20
# with social1:
#     st_button2('linkedin', 'https://www.linkedin.com/in/ravinder-j-37849b244/', 'linkedin', icon_size)
    
# with social2:
#     st_button2('Email', 'https://sendfox.com/dataprofessor/', 'Mail', icon_size)
    
# with social3:
#     st_button2('linkedin', 'https://www.linkedin.com/in/ravinder-j-37849b244/', 'linkedin', icon_size)
     