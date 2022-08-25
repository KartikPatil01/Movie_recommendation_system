import streamlit as st
import pickle
import requests
import pandas as pd
from requests.structures import CaseInsensitiveDict
import numpy as np

my_name = 'kartik'

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=53f7e3dc5179faa614fb0a4a97f25cfe',headers=headers)
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']

# recommendation function to recommend the top 5 movies
def recommend(movie):
    movie_index = new_df[new_df["title"] == movie].index[0]
    distance = similarity[movie_index]
    movies = sorted(enumerate(distance),reverse= True , key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    recommended_id = []
    for i in movies:
        movie_id = movies_list.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)
        recommended_movies_poster.append(poster)
        # fetch poster from api
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_id.append(movie_id)

    return recommended_movies , recommended_movies_poster , recommended_id


def setSessionId(Id):
    st.session_state["movieId"] = Id

def setSessionname(name):
    st.session_state["moviename"] = name

def main_page():
    #st.sidebar.markdown("# Recommender ")
    st.title('Movie Recommender System')

    # insert the select box
    selected_movie_name = st.selectbox('Select the Movie ',
                                       m_list)
    name , poster , ids = recommend(selected_movie_name)


    if st.button("Recommend"):
        name , poster , ids = recommend(selected_movie_name)
        #movie_name = name

        setSessionId(ids)
        setSessionname(selected_movie_name)
        col1 , col2 , col3 , col4 , col5 = st.columns(5)
        with col1:
            st.text(name[0])
            #st.image(poster[0])
            #setSessionId(ids[0])
            st.markdown(f'''
                    <img src={poster[0]} height = 192, width = 128 > ''',
                       unsafe_allow_html=True
                )

        with col2:
            st.text(name[1])
            #setSessionId(ids[1])
            st.markdown(f'''
                            <img  src={poster[1]} height = 192, width = 128 >  ''',
                        unsafe_allow_html=True
                        )

        with col3:
            st.text(name[2])
            #setSessionId(ids[2])
            st.markdown(f''' 
                        <img src={poster[2]} height = 192, width = 128 >
                        </a>''',
                        unsafe_allow_html=True
                        )

        with col4:
            st.text(name[3])
            #setSessionId(ids[3])
            st.markdown(f'''
                            <img src={poster[3]} height = 192, width = 128 >
                        </a>''',
                        unsafe_allow_html=True
                        )

        with col5:
            st.text(name[4])
            #setSessionId(ids[4])
            st.markdown(f'''
                            <img src={poster[4]} height = 192, width = 128 >
                        </a>''',
                        unsafe_allow_html=True
                        )


def movie_1():
    val = st.session_state.movieId[0]
    response = requests.get(f'https://api.themoviedb.org/3/movie/{val}?api_key=53f7e3dc5179faa614fb0a4a97f25cfe',
                            headers=headers)
    data = response.json()
    with st.container():
        st.header('{}'.format(data['original_title']))
        image_column , text_columns = st.columns((1,2))

        with image_column:
            st.image("http://image.tmdb.org/t/p/w500/"+data['poster_path'])

        with text_columns:
            st.subheader('Overview')
            st.write('{}'.format(data['overview']))
            geners = []
            for val in data['genres']:
                geners.append(val['name'])
            date = data['release_date']
            rating = data['vote_average']
            status = data['status']
            comp = ''
            for val in data['production_companies']:
                comp += '{}  ,'.format(val['name'])

            budg = data['budget']
            st.write(
                f'''
                **Rating** \t :  {rating} \n
                **Status**  :  {status} \n
                **Release Date** : {date} \n
                **Genres** : {" , ".join(geners)} \n
                **Production Company** : {comp} \n
                **Budget** : {budg} \n
                '''
            )

def movie_2():
    val = st.session_state.movieId[1]
    response = requests.get(f'https://api.themoviedb.org/3/movie/{val}?api_key=53f7e3dc5179faa614fb0a4a97f25cfe',
                            headers=headers)
    data = response.json()
    with st.container():
        st.header('{}'.format(data['original_title']))
        image_column , text_columns = st.columns((1,2))

        with image_column:
            st.image("http://image.tmdb.org/t/p/w500/"+data['poster_path'])

        with text_columns:
            st.subheader('Overview')
            st.write('{}'.format(data['overview']))
            geners = []
            for val in data['genres']:
                geners.append(val['name'])
            date = data['release_date']
            rating = data['vote_average']
            status = data['status']
            comp = ''
            for val in data['production_companies']:
                comp += '{}  ,'.format(val['name'])

            budg = data['budget']
            st.write(
                f'''
                **Rating** \t :  {rating} \n
                **Status**  :  {status} \n
                **Release Date** : {date} \n
                **Genres** : {" , ".join(geners)} \n
                **Production Company** : {comp} \n
                **Budget** : {budg} \n
                '''
            )

def movie_3():
    val = st.session_state.movieId[2]
    response = requests.get(f'https://api.themoviedb.org/3/movie/{val}?api_key=53f7e3dc5179faa614fb0a4a97f25cfe',
                            headers=headers)
    data = response.json()
    with st.container():
        st.header('{}'.format(data['original_title']))
        image_column , text_columns = st.columns((1,2))

        with image_column:
            st.image("http://image.tmdb.org/t/p/w500/"+data['poster_path'])

        with text_columns:
            st.subheader('Overview')
            st.write('{}'.format(data['overview']))
            geners = []
            for val in data['genres']:
                geners.append(val['name'])
            date = data['release_date']
            rating = data['vote_average']
            status = data['status']
            comp = ''
            for val in data['production_companies']:
                comp += '{}  ,'.format(val['name'])

            budg = data['budget']
            st.write(
                f'''
                **Rating** \t :  {rating} \n
                **Status**  :  {status} \n
                **Release Date** : {date} \n
                **Genres** : {" , ".join(geners)} \n
                **Production Company** : {comp} \n
                **Budget** : {budg} \n
                '''
            )

def movie_4():
    val = st.session_state.movieId[3]
    response = requests.get(f'https://api.themoviedb.org/3/movie/{val}?api_key=53f7e3dc5179faa614fb0a4a97f25cfe',
                            headers=headers)
    data = response.json()
    with st.container():
        st.header('{}'.format(data['original_title']))
        image_column , text_columns = st.columns((1,2))

        with image_column:
            st.image("http://image.tmdb.org/t/p/w500/"+data['poster_path'])

        with text_columns:
            st.subheader('Overview')
            st.write('{}'.format(data['overview']))
            geners = []
            for val in data['genres']:
                geners.append(val['name'])
            date = data['release_date']
            rating = data['vote_average']
            status = data['status']
            comp = ''
            for val in data['production_companies']:
                comp += '{}  ,'.format(val['name'])

            budg = data['budget']
            st.write(
                f'''
                **Rating** \t :  {rating} \n
                **Status**  :  {status} \n
                **Release Date** : {date} \n
                **Genres** : {" , ".join(geners)} \n
                **Production Company** : {comp} \n
                **Budget** : {budg} \n
                '''
            )

def movie_5():
    st.sidebar.write('movie5')
    val = st.session_state.movieId[4]
    response = requests.get(f'https://api.themoviedb.org/3/movie/{val}?api_key=53f7e3dc5179faa614fb0a4a97f25cfe',
                            headers=headers)
    data = response.json()
    with st.container():
        st.header('{}'.format(data['original_title']))
        image_column , text_columns = st.columns((1,2))

        with image_column:
            st.image("http://image.tmdb.org/t/p/w500/"+data['poster_path'])

        with text_columns:
            st.subheader('Overview')
            st.write('{}'.format(data['overview']))
            geners = []
            for val in data['genres']:
                geners.append(val['name'])
            date = data['release_date']
            rating = data['vote_average']
            status = data['status']
            comp = ''
            for val in data['production_companies']:
                comp += '{}  ,'.format(val['name'])

            budg = data['budget']
            st.write(
                f'''
                **Rating** \t :  {rating} \n
                **Status**  :  {status} \n
                **Release Date** : {date} \n
                **Genres** : {" , ".join(geners)} \n
                **Production Company** : {comp} \n
                **Budget** : {budg} \n
                '''
            )



if __name__ == '__main__':
    st.set_page_config(layout='wide')

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1M2Y3ZTNkYzUxNzlmYWE2MTRmYjBhNGE5N2YyNWNmZSIsInN1YiI6IjYyMWRlZWU1OWYxYmU3MDA0NDY2ZDgxNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.O5N5jJwnHjSIQL_3fqFzBozPxHH6t_7QB5ZH2FVKvGw"

    movies_list = pickle.load(open("my_movies.pkl", "rb"))

    similarity = pickle.load(open("similarity.pkl", "rb"))

    # fetch the movie titles
    m_list = movies_list["title"].values
    new_df = pd.DataFrame(movies_list)

    if "movieId" not in st.session_state:
        st.session_state["movieId"] = ""

    if "moviename" not in st.session_state:
        st.session_state["moviename"] = ""

    movie_name =[]
    #print(movie_name)

    pages_name = {

        'Recommender': main_page,
        (f'{movie_name[0]}' if len(movie_name) > 1 else 'movie1'): movie_1,
        (f'{movie_name[1]}' if len(movie_name) > 1 else 'movie2'): movie_2,
        (f'{movie_name[2]}' if len(movie_name) > 1 else 'movie3'): movie_3,
        (f'{movie_name[3]}' if len(movie_name) > 1 else 'movie4'): movie_4,
        (f'{movie_name[4]}' if len(movie_name) > 1 else 'movie5'): movie_5
    }
    print(st.session_state.moviename)
    select_page = st.sidebar.selectbox("Select a option ", pages_name.keys())
    pages_name[select_page]()



