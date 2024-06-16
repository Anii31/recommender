import streamlit as st
import pandas as pd
import pickle

# Function to apply CSS for styling
def set_style():
    st.markdown(
        """
        <style>
        .stApp {
            background: url("https://images.all-free-download.com/images/graphiclarge/movie_poster_background_art_vector_530172.jpg") no-repeat center center fixed;
            background-size: cover;
        }
        
      .title {
    font-size: 2.5rem;
    color: #8A2BE2; /* Set title color to Blue Violet (#8A2BE2) */
    font-weight: bold;
    margin-bottom: 1rem;
    text-align: center;
}

        
        .details-item {
            margin-bottom: 10px;
            color: white; /* Set text color to white */
        }
        .details-item strong {
            color: #ffa500; /* Example: Set strong tag color to orange */
        }
        .recommendation {
            margin-top: 20px;
            padding: 10px;
            background-color: #ffe6e6;
            border-left: 4px solid #ff3333;
            border-radius: 5px;
            color: black; /* Set recommendation text color to black */
        }
        .explore {
            background-color: #fffacd; /* Cream color for text background */
            padding: 10px;
            margin-bottom: 20px;
            text-align: center;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def app():
    set_style()
    
    st.markdown('<div class="explore">Explore details of your favorite movies.</div>', unsafe_allow_html=True)

    def get_movie_details(movie, movies):
        try:
            movie_details = movies[movies['title'] == movie].iloc[0]
            details = {
                "Title": movie_details['title'],
                "Genres": movie_details['genres'],
                "Overview": movie_details['overview'],
                "Cast": movie_details['cast'],
                "Director": movie_details['Director']
            }
            return details
        except IndexError:
            return None

    # Load movie details
    mov_details = pickle.load(open('mov_details.pkl', 'rb'))
    movies = pd.DataFrame(mov_details)

    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    selected_movie = st.selectbox('Search movies', movies['title'].values)

    if st.button('Search'):
        with st.spinner('Finding details...'):
            movie_details = get_movie_details(selected_movie, movies)

            if movie_details:
                st.markdown('<div class="details-container">', unsafe_allow_html=True)
                st.markdown('<h2 class="title">Movie Details:</h2>', unsafe_allow_html=True)
                for key, value in movie_details.items():
                    st.markdown(f'<p class="details-item"><strong>{key}:</strong> {value}</p>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="recommendation">No details found for the selected movie.</div>', unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    app()
