import streamlit as st
import plotly.express as px
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Student Grades Dashboard", layout="wide")

# Data
data = {
    'name': ['lee', 'park', 'kim'],
    'grade': [2, 2, 2],
    'number': [1, 2, 3],
    'kor': [90, 88, 99],
    'eng': [91, 89, 99],
    'math': [81, 77, 99],
    'info': [100, 100, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Student Grades Dashboard")

# Display raw data
st.subheader("Raw Data")
st.dataframe(df)

# Bar chart for individual subject scores
st.subheader("Individual Subject Scores")
fig_bar = px.bar(df, 
                 x='name', 
                 y=['kor', 'eng', 'math', 'info'],
                 barmode='group',
                 title='Subject Scores by Student',
                 labels={'value': 'Score', 'name': 'Student', 'variable': 'Subject'})
st.plotly_chart(fig_bar, use_container_width=True)

# Radar chart for comparing students
st.subheader("Student Performance Comparison")
# Prepare data for radar chart
subjects = ['kor', 'eng', 'math', 'info']
radar_data = pd.melt(df, id_vars=['name'], value_vars=subjects, 
                     var_name='subject', value_name='score')

fig_radar = px.line_polar(radar_data, 
                         r='score', 
                         theta='subject', 
                         color='name',
                         line_close=True,
                         title='Student Performance Across Subjects')
st.plotly_chart(fig_radar, use_container_width=True)

# Heatmap for score distribution
st.subheader("Score Distribution Heatmap")
fig_heatmap = px.imshow(df[['kor', 'eng', 'math', 'info']].values,
                       x=['Korean', 'English', 'Math', 'Info'],
                       y=df['name'],
                       title='Score Distribution',
                       color_continuous_scale='Viridis')
st.plotly_chart(fig_heatmap, use_container_width=True)

# Average scores per student
st.subheader("Average Scores per Student")
df['average'] = df[['kor', 'eng', 'math', 'info']].mean(axis=1)
fig_avg = px.bar(df, 
                x='name', 
                y='average',
                title='Average Score per Student',
                labels={'average': 'Average Score', 'name': 'Student'})
st.plotly_chart(fig_avg, use_container_width=True)