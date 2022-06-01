import streamlit as st
import pickle
import requests
import pandas as pd
import numpy as np

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']

# recommendation function to recommend the top 5 movies
def recommend(movie):
    movie_index = new_df[new_df["title"] == movie].index[0]
    distance = similarity[movie_index]
    movies = sorted(enumerate(distance),reverse= True , key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies:
        movie_id = movies_list.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)
        recommended_movies_poster.append(poster)
        # fetch poster from api
        recommended_movies.append(movies_list.iloc[i[0]].title)

    return recommended_movies , recommended_movies_poster

#load the pickle
movies_list = pickle.load(open("my_movies.pkl","rb"))

similarity = pickle.load(open("similarity.pkl","rb"))

# fetch the movie titles
m_list = movies_list["title"].values
print(m_list)
new_df = pd.DataFrame(movies_list)

# print(movies_list[movies_list['title'] == 'Avatar'].index)
# title of the api
st.title('Movie Recommender System')

# insert the select box
selected_movie_name = st.selectbox('Select the Movie ',
                      m_list)

if st.button("Recommend"):
    name , poster = recommend(selected_movie_name)

    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])