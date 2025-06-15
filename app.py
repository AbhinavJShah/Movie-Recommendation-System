import streamlit as st
import pickle 
import pandas as pd
import requests

def poster_fetch(id):
    requests.get('https://api.themoviedb.org/3/keyword/1363/movies?api_key=e00e6b991e8c3257fa29d03c158f6b2a&include_adult=false&language=en-US&page=1')

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:7]
    recomended_movies = []
    for i in distances[1:6]:
        movie_id = i[0]
        ##To fetch the poster

        recomended_movies.append(movies.iloc[i[0]].title)

    return recomended_movies


movie_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommendation System')

selected_movie = st.selectbox(
'What movie are you looking for?',
movies['title'].values
)

if st.button('Recommend'):
    recomenddations = recommend(selected_movie)
    for i in recomenddations:
        st.write(i)
