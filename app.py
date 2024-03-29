import streamlit as st
import pickle
import pandas
import requests
##LAYOUT
#st.set_page_config(layout='wide')


### variables

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key=8ac9a884a43af2dffd56f8e7a50133d1"
    response=requests.get(url)
    data=response.json()
    return "https://image.tmdb.org/t/p/w185/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetching poster
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters


movies_list=pickle.load(open('movies.pkl','rb'))
movies=movies_list
movies_list=movies_list['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))

###webapp
st.title('Movie Recommender Sysetm')

selected_movie_name=st.selectbox(
    'What have you watched recently??',
    movies_list
)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)

    col1,col2,col3,col4,col5 = st.columns(5,gap="medium")
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

