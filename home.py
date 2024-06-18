import streamlit as st
import pickle
import pandas as pd
import requests

def app():
    # Apply custom CSS to add a background image and style elements
    st.markdown(
        """
        <style>
        .stApp {
            background: url("https://user-images.githubusercontent.com/33485020/108069438-5ee79d80-7089-11eb-8264-08fdda7e0d11.jpg") no-repeat center center fixed;
            background-size: cover;
        }
        .title {
            font-size: 50px;
            text-align: center;
            background: linear-gradient(to left, yellow, red, yellow, orange, red, yellow);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
             font-weight: bold;
            animation: rainbow-text-animation 10s ease-in-out infinite;
        }
        .blue-bg {
            background-color: #DCDCDC; /* glass blue */
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            font-size: 20px;
            color: black; /* Text color */
        }
        .recommendation {
            background-color: #f0f8ff; /* AliceBlue color */
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
            color: black; /* Light blue text color for movie suggestions */
            margin: 5px 0;
        }
        .center-content {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .movie-container {
            padding: 10px;
            text-align: center;
            margin: 5px;
        }
        .movie-container img {
            width: 200px; /* Increase the size of the movie images */
        }
        .custom-spinner-text {
            color: red; 
            font-size: 18px;
            font-weight: bold;
        }
       
        @keyframes rainbow-text-animation {
            0% {
                background-position: 50%;
            }
            50% {
                background-position: 100% ;
            }
            100% {
                background-position: 50%;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    def fetch_poster(movie_id):
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=9b2490ef93e7d70561e4e1ccf2d30da2&language=en-US')
        data = response.json()
        return f'https://image.tmdb.org/t/p/w185/{data["poster_path"]}'

    # Function to recommend movies
    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:7]

        recommended_movies = []
        recommended_movies_poster = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            
            recommended_movies.append(movies.iloc[i[0]].title)
            # Fetch poster from API
            recommended_movies_poster.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_poster
    

    # Load the movie data and similarity matrix
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    # Title and description
    st.markdown('<h1 class="title">HUNT FOR TOP FLICKS</h1>', unsafe_allow_html=True)
    st.markdown('<div class="blue-bg">Search a movie to get recommendations.</div>', unsafe_allow_html=True)

    # Center the select box and search button
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    selected_movie = st.selectbox('Search movies', movies['title'].values)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button('Search Movie'):
        # Create a custom spinner text
        with st.empty():
            spinner_placeholder = st.empty()
            spinner_placeholder.markdown('<div class="custom-spinner-text">Finding recommendations...</div>', unsafe_allow_html=True)


            recommendation, poster = recommend(selected_movie) 

            if len(recommendation) > 0 and len(poster) > 0:
                col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

                for idx, col in enumerate([col1, col2, col3, col4, col5, col6, col7]):
                    with col:
                        st.markdown('<div class="movie-container">', unsafe_allow_html=True)
                        st.image(poster[idx])
                        st.markdown(f'<h4 style="color:lightblue;">{recommendation[idx]}</h4>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    app()
