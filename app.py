import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title('Movie recommender System')

def recommend(movie):
    movie_index = df[df['Title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(enumerate(distances),reverse=True,key = lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(df.iloc[i[0]].Title)
    return recommended_movies

movies_dict = pickle.load(open('df.pkl','rb'))
df = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie_name = st.selectbox(
'Name the movie you liked',
df['Title'].values
    )
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
