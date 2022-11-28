import streamlit as st 
from PIL import Image 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

df1 = pd.read_csv("Dietary.csv")
df2 = pd.read_csv("Biochemical.csv")

df2 = df2.replace('1-2022', '8-2022')
df2 = df2.replace('2-2022', '9-2022')
df2_1 = df2[df2.Month == '8-2022']
df2_2 = df2[df2.Month == '9-2022']

df3 = pd.read_csv("Clinical.csv")
df3 = df3.replace('1-2022', '8-2022')
df3 = df3.replace('2-2022', '9-2022')
df3_1 = df3[df3.Month == '8-2022']
df3_2 = df3[df3.Month == '9-2022']

df4 = pd.read_csv("Anthropometric.csv")
df4 = df4.replace('1-2022', '8-2022')
df4 = df4.replace('2-2022', '9-2022')
df4_1 = df4[df4.Month == '8-2022']
df4_2 = df4[df4.Month == '9-2022']

df5 = pd.read_csv("Nutrients_New.csv")



























####################################

st.markdown("# Nutrition Project")
st.sidebar.markdown("## Side Panel" 
	)
st.sidebar.markdown("Use this panel to explore the dataset and create own viz.")

st.title('Quick  Explore')
st.sidebar.subheader(' Quick  Explore')
st.markdown("Tick the box on the side panel to explore the dataset.")
if st.sidebar.checkbox('Basic info'):
    if st.sidebar.checkbox('Dataset Quick Look'):
        st.subheader('Dataset Quick Look:')
        #Drop down menu
        option = st.selectbox('Select Dataset',('Dietary','Biochemical','Clinical','Anthropometric','Nutrients'))
        if option == 'Dietary':
            st.write(df1)
        elif option == 'Biochemical':
            st.write(df2)
        elif option == 'Clinical':
            st.write(df3)
        elif option == 'Anthropometric':
            st.write(df4)
        elif option == 'Nutrients':
            st.write(df5)
    if st.sidebar.checkbox("Show Columns"):
        st.subheader("Columns:")
        #Drop down menu
        option = st.selectbox('Select Dataset',('Dietary','Biochemical','Clinical','Anthropometric','Nutrients'), key = '1')
        if option == 'Dietary':
            st.write(df1.columns)
        elif option == 'Biochemical':
            st.write(df2.columns)
        elif option == 'Clinical':
            st.write(df3.columns)
        elif option == 'Anthropometric':
            st.write(df4.columns)
        elif option == 'Nutrients':
            st.write(df5.columns)
    # if st.sidebar.checkbox('Column Names'):
    #     st.subheader('Column Names')
    #     st.write(df.columns())
    if st.sidebar.checkbox('Statistical Description'):
        st.subheader('Statistical Description')
        #Drop down menu
        option = st.selectbox('Select Dataset',('Dietary','Biochemical','Clinical','Anthropometric','Nutrients'), key = '2')
        if option == 'Dietary':
            st.write(df1.describe())
        elif option == 'Biochemical':
            st.write(df2.describe())
        elif option == 'Clinical':
            st.write(df3.describe())
        elif option == 'Anthropometric':
            st.write(df4.describe())
        elif option == 'Nutrients':
            st.write(df5.describe())
    if st.sidebar.checkbox('Missing Values?'):
        st.subheader('Missing Values')
        #Drop down menu
        option = st.selectbox('Select Dataset',('Dietary','Biochemical','Clinical','Anthropometric','Nutrients'), key = '3')
        if option == 'Dietary':
            st.write(df1.isnull().sum())
        elif option == 'Biochemical':
            st.write(df2.isnull().sum())
        elif option == 'Clinical':
            st.write(df3.isnull().sum())
        elif option == 'Anthropometric':
            st.write(df4.isnull().sum())
        elif option == 'Nutrients':
            st.write(df5.isnull().sum())

if st.sidebar.checkbox('Deficiency Detection'):
    if st.sidebar.checkbox('Dietary Deficiency'):
        num = st.selectbox('Enter Aadhaar Number', df1.Aadhaar)
        test = df3_1[df3_1.Aadhaar == num]
        test=test.drop(columns=test.columns[(test == 0).any()])
        value=test.Aadhaar.values
        value1=test.columns.values
        for i in range(2,len(value1)):
            new=df5.loc[df5["DSym"]==value1[i]]
            if i==2:
                temp=new.Nutrients.values
            else:
                temp=np.intersect1d(temp,new.Nutrients.values)
            st.write("Deficiencies related to symptom",value1[i],"are",new.Nutrients.values)
        st.write("Common deficiencies for all the given symptoms",temp)
    if st.sidebar.checkbox('Food Recommendation'):
        for i in range(len(temp)):
            source=df5.loc[df5["Nutrients"]==temp[i]]
            source=source[["Nutrients","Source"]]
            source=source.drop_duplicates()
            for j in range(len(source)):
                st.write("Recommended food to cut off",source.Nutrients.values[0],"deficiency are",source.Source.values[j])

if st.sidebar.checkbox('Data Visualization'):
    if st.sidebar.checkbox('Biochemical and Anthropometric'):
        ex=np.ones(124,dtype=float)
        ex[0]=ex[0]*0.01
        ex[1]=ex[1]*0.08
        ex[2]=0.2*ex[2]
        ex[3]=0.2*ex[3]
        for i in range(4,124):
            ex[i]=ex[i]*(i-3)
        new=np.ones(124,dtype=float)
        new_min=np.ones(124,dtype=float)
        new_min[0]=17
        new_min[1]=15
        new_min[2]=11
        new_min[3]=11
        new[0]=22
        new[1]=20
        new[2]=15
        new[3]=13
        for i in range(4,23):
            new[i]=13
            new_min[i]=11
        for i in range(23,69):
            new[i]=18
            new_min[i]=14
        for i in range(69,124):
            new[i]=14.9
            new_min[i]=12.4
        df4 = df4.replace('Gender.Male', 'Male')
        df4 = df4.replace('Gender.Female', 'Female')
        new_df=pd.merge(df2,df4,on="Aadhaar",how="inner")
        new_df_1=new_df[new_df["Month_x"]==new_df["Month_y"]]
        new_df_1=new_df_1[new_df_1["Month_x"]=="8-2022"]
        new_df_2=new_df[new_df["Month_x"]==new_df["Month_y"]]
        new_df_2=new_df_2[new_df_2["Month_x"]=="9-2022"]
        new_df_1_1=new_df_1[new_df_1["Gender"]=="Male"]
        new_df_1_2=new_df_1[new_df_1["Gender"]=="Female"]
        new_df_2_1=new_df_2[new_df_2["Gender"]=="Male"]
        new_df_2_2=new_df_2[new_df_2["Gender"]=="Female"]
        df_rl_1 = pd.DataFrame({'Age Group - Men': ['NewBorn','1 week','1 month','0.2-18','18-64','64+'],'Min': [17, 15, 11, 11, 14, 12.4],'Max': [22, 20, 15, 13, 18, 14.9]})
        df_rl_2 = pd.DataFrame({'Age Group - Women': ['NewBorn','1 week','1 month','0.2-18','18-64','64+'],'Min': [17, 15, 11, 11, 12, 11],'Max': [22, 20, 15, 13, 16, 13.8]})

        df_rl_1.insert(loc=3,column="Min_Age",value=[0,0.0191781,0.0833334,0.2,18,64])
        df_rl_1.insert(loc=4,column="Max_Age",value=[0.0191781,0.0833334,0.2,18,64,120])
        df_rl_2.insert(loc=3,column="Min_Age",value=[0,0.0191781,0.0833334,0.2,18,64])
        df_rl_2.insert(loc=4,column="Max_Age",value=[0.0191781,0.0833334,0.2,18,64,120])
        
        exw=np.ones(124,dtype=float)
        exw[0]=exw[0]*0.01
        exw[1]=exw[1]*0.08
        exw[2]=0.2*exw[2]
        exw[3]=0.2*exw[3]
        for i in range(4,124):
            exw[i]=exw[i]*(i-3)
        neww=np.ones(124,dtype=float)
        neww_min=np.ones(124,dtype=float)
        neww_min[0]=17
        neww_min[1]=15
        neww_min[2]=11
        neww_min[3]=11
        neww[0]=22
        neww[1]=20
        neww[2]=15
        neww[3]=13
        for i in range(4,23):
            neww[i]=13
            neww_min[i]=11
        for i in range(23,69):
            neww[i]=16
            neww_min[i]=12
        for i in range(69,124):
            neww[i]=13.8
            neww_min[i]=11
        average_hb_men_1= new_df_1_1.Haemoglobin.sum()/(len(new_df_1_1))
        average_hb_men_2= new_df_1_2.Haemoglobin.sum()/(len(new_df_1_2))
        average_hb_women_1= new_df_2_1.Haemoglobin.sum()/(len(new_df_2_1))
        average_hb_women_2= new_df_2_2.Haemoglobin.sum()/(len(new_df_2_2))
        averages={"average_hb_men_1":average_hb_men_1,"average_hb_men_2":average_hb_men_2,"average_hb_women_1":average_hb_women_1,"average_hb_women_2":average_hb_women_2}
        df_grp_1=new_df_1_1.groupby(["Age","Haemoglobin"],as_index=False).mean("Haemoglobin")
        df_grp_1=df_grp_1[["Age","Haemoglobin"]]
        df_grp_1=df_grp_1.groupby(["Age"],as_index=False).mean()
        #df_grp_1
        df_grp_2=new_df_1_2.groupby(["Age","Haemoglobin"],as_index=False).mean("Haemoglobin")
        df_grp_2=df_grp_2[["Age","Haemoglobin"]]
        df_grp_2=df_grp_2.groupby(["Age"],as_index=False).mean()
        #df_grp_2
        df_grp_3=new_df_2_1.groupby(["Age","Haemoglobin"],as_index=False).mean("Haemoglobin")
        df_grp_3=df_grp_3[["Age","Haemoglobin"]]
        df_grp_3=df_grp_3.groupby(["Age"],as_index=False).mean()
        df_grp_4=new_df_2_2.groupby(["Age","Haemoglobin"],as_index=False).mean("Haemoglobin")
        df_grp_4=df_grp_4[["Age","Haemoglobin"]]
        df_grp_4=df_grp_4.groupby(["Age"],as_index=False).mean()
        st.subheader('Data Visualization')
        #Drop down menu
        option = st.selectbox('Select Dataset',('Haemoglobin Range for Men', 'Haemoglobin', 'Haemoglobin Value - Men - 8-2022', 'Haemoglobin Value - Men - 9-2022', 'Haemoglobin Range for Women (gm/dL)', 'Haemoglobin Value - Women - 8-2022', 'Haemoglobin Value - Women - 9-2022', 'Average Haemoglobin value by age - Male - 8-2022', 'Average Haemoglobin value by age - Male - 9-2022', 'Average Haemoglobin value by age - Female - 8-2022'), key = '4')
        if option == 'Haemoglobin Range for Men':
            fig1=go.Figure(data=go.Scattergl(x=df_rl_1["Age Group - Men"],y=df_rl_1["Min"],mode="markers",marker_color="green"))
            fig2=go.Figure(data=go.Scattergl(x=df_rl_1["Age Group - Men"],y=df_rl_1["Max"],mode="markers",marker_color="red"))
            fig1.update_traces(name="Minimum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig2.update_traces(name="Maximum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig3=go.Figure(data=fig1.data + fig2.data)
            fig3.update_traces(mode="lines+markers")
            fig3.update_layout(title='Haemoglobin Range for Men (gm/dL)')
            fig3.update_traces(legendgrouptitle_text="Range")
            st.plotly_chart(fig3, use_container_width=True)

        elif option == 'Haemoglobin':
            fig1=go.Figure(data=go.Scattergl(x=new_df_1_1["Age"],y=new_df_1_1["Haemoglobin"],mode="markers",marker_color="violet"))
            fig1.update_traces(hovertemplate="<br>".join(["Age : %{x}","Haemoglobin (gm/dL): %{y}","Aadhaar : %{new_df_1.Aadhaar}"]))
            fig1.update_layout(title='Haemoglobin (gm/dL)')
            st.plotly_chart(fig1, use_container_width=True) 

        elif option == 'Haemoglobin Value - Men - 8-2022':
            fig1=go.Figure(data=go.Scattergl(x=ex,y=new,mode="lines",marker_color="green"))
            fig2=go.Figure(data=go.Scattergl(x=ex,y=new_min,mode="lines",marker_color="red"))
            fig3=go.Figure(data=go.Scattergl(x=new_df_1_1["Age"],y=new_df_1_1["Haemoglobin"],mode="markers",marker_color="violet"))
            fig1.update_traces(name="Minimum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig2.update_traces(name="Maximum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig4=go.Figure(data=fig1.data+fig2.data)
            fig4.update_traces(mode="lines")
            fig5=go.Figure(data=fig4.data+fig3.data)
            fig5.update_layout(title='Haemoglobin Value - Men - 8-2022')
            fig5.update_traces(legendgrouptitle_text="Range")
            st.plotly_chart(fig5, use_container_width=True)

        elif option == 'Haemoglobin Value - Men - 9-2022':
            fig1=go.Figure(data=go.Scattergl(x=ex,y=new,mode="lines",marker_color="green"))
            fig2=go.Figure(data=go.Scattergl(x=ex,y=new_min,mode="lines",marker_color="red"))
            fig3=go.Figure(data=go.Scattergl(x=new_df_1_2["Age"],y=new_df_1_2["Haemoglobin"],mode="markers",marker_color="violet"))
            fig1.update_traces(name="Minimum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig2.update_traces(name="Maximum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig4=go.Figure(data=fig1.data+fig2.data)
            fig4.update_traces(mode="lines")
            fig5=go.Figure(data=fig4.data+fig3.data)
            fig5.update_layout(title='Haemoglobin Value - Men - 9-2022')
            fig5.update_traces(legendgrouptitle_text="Range")
            st.plotly_chart(fig5, use_container_width=True)
        elif 'Haemoglobin Range for Women (gm/dL)':
            fig1=go.Figure(data=go.Scattergl(x=df_rl_2["Age Group - Women"],y=df_rl_2["Min"],mode="markers",marker_color="green"))
            fig2=go.Figure(data=go.Scattergl(x=df_rl_2["Age Group - Women"],y=df_rl_2["Max"],mode="markers",marker_color="red"))
            fig1.update_traces(name="Minimum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig2.update_traces(name="Maximum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig3=go.Figure(data=fig1.data + fig2.data)
            fig3.update_traces(mode="lines+markers")
            fig3.update_layout(title='Haemoglobin Range for Women (gm/dL)')
            fig3.update_traces(legendgrouptitle_text="Range")
            st.plotly_chart(fig3, use_container_width=True)
        elif 'Haemoglobin Value - Women - 8-2022':
            fig1=go.Figure(data=go.Scattergl(x=exw,y=neww,mode="lines",marker_color="green"))
            fig2=go.Figure(data=go.Scattergl(x=exw,y=neww_min,mode="lines",marker_color="red"))
            fig3=go.Figure(data=go.Scattergl(x=new_df_2_1["Age"],y=new_df_2_1["Haemoglobin"],mode="markers",marker_color="violet"))
            fig1.update_traces(name="Minimum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig2.update_traces(name="Maximum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig4=go.Figure(data=fig1.data+fig2.data)
            fig4.update_traces(mode="lines")
            fig5=go.Figure(data=fig4.data+fig3.data)
            fig5.update_layout(title='Haemoglobin Value - Women - 8-2022')
            fig5.update_traces(legendgrouptitle_text="Range")
            st.plotly_chart(fig5, use_container_width=True)
        elif 'Haemoglobin Value - Women - 9-2022':
            fig1=go.Figure(data=go.Scattergl(x=exw,y=neww,mode="lines",marker_color="green"))
            fig2=go.Figure(data=go.Scattergl(x=exw,y=neww_min,mode="lines",marker_color="red"))
            fig3=go.Figure(data=go.Scattergl(x=new_df_2_2["Age"],y=new_df_2_2["Haemoglobin"],mode="markers",marker_color="violet"))
            fig1.update_traces(name="Minimum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig2.update_traces(name="Maximum",hovertemplate="<br>".join(["Age_Group : %{x}","Haemoglobin (gm/dL): %{y}"]))
            fig4=go.Figure(data=fig1.data+fig2.data)
            fig4.update_traces(mode="lines")
            fig5=go.Figure(data=fig4.data+fig3.data)
            fig5.update_layout(title='Haemoglobin Value - Women - 9-2022')
            fig5.update_traces(legendgrouptitle_text="Range")
            st.plotly_chart(fig5, use_container_width=True)
        elif 'Average Haemoglobin value by age - Male - 8-2022':
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=df_grp_1["Age"],
                y=df_grp_1["Haemoglobin"],
                name='Average Haemoglobin value by age - Male - 8-2022',
                marker_color='indianred'
            ))
            #fig.add_trace(go.Bar(
            #    x=df_grp_2["Age"],
            #    y=df_grp_2["Haemoglobin"],
            #    name='Average Haemoglobin value by age - Male - 9-2022',
            #    marker_color='pink'
            #))

            # Here we modify the tickangle of the xaxis, resulting in rotated labels.
            fig.update_layout(barmode='group', xaxis_tickangle=-45)
            fig.update_layout(title='Average Haemoglobin value by age - Male - 8-2022')
            st.plotly_chart(fig, use_container_width=True)
        elif 'Average Haemoglobin value by age - Male - 9-2022':
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=df_grp_2["Age"],
                y=df_grp_2["Haemoglobin"],
                name='Average Haemoglobin value by age - Male - 9-2022',
                marker_color='pink'
            ))
            fig.update_layout(barmode='group', xaxis_tickangle=-45)
            fig.update_layout(title='Average Haemoglobin value by age - Male - 9-2022')
            st.plotly_chart(fig, use_container_width=True)
        elif 'Average Haemoglobin value by age - Female - 8-2022':
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x = df_grp_3["Age"],
                y = df_grp_3["Haemoglobin"],
                name = 'Average Haemoglobin value by age - Female - 8 - 2022',
                marker_color = 'indinared'
            ))
            fig.update_layout(barmode='group', xaxis_tickangle=-45)
            fig.update_layout(title='Average Haemoglobin value by age - Female - 8- 2022')
            st.plotly_chart(fig, use_container_width=True)