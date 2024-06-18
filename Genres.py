import streamlit as st
import pandas as pd
import pickle

def app():
    # Apply custom CSS to add a background image and style elements
    st.markdown(
        """
        <style>
        .stApp {
            background: url("https://rebeccabookreview.files.wordpress.com/2021/04/genre_cloud.png?w=1200") no-repeat center center fixed;
            background-size: cover;
        }
        .title {
            font-size: 50px;
            text-align: center;
            background: linear-gradient(to right, yellow, blue, yellow, orange, red, indigo);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
            animation: rainbow-text-animation 10s ease-in-out infinite;
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
            margin-bottom: 20px;
        }
        .movie-container {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    def recommend_genre(selected_genre):
        # Filtering the movies dataframe to get only the movies that contain the given genre
        movies_genre = mov_details[mov_details['genres'].apply(lambda x: selected_genre in x)]

        recommended_genres = []

        # Iterating through the filtered dataframe and collecting titles
        for i in range(len(movies_genre)):
            recommended_genres.append(movies_genre.iloc[i].title)
        return recommended_genres[:7]  # Limiting to 7 recommendations

    mov_details = pickle.load(open('mov_details.pkl', 'rb'))

    # Title and description
    st.markdown('<h1 class="title">GENRE-BASED RECOMMENDATIONS</h1>', unsafe_allow_html=True)

    # Center the selectbox and search button
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    selected_genre = st.selectbox('Select genre', mov_details['genres'].explode().unique())
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button('Search Genres'):
        # Create a custom spinner text
        with st.spinner('Finding recommendations...'):
            if selected_genre:
                recommendation = recommend_genre(selected_genre)

                if recommendation:
                    for movie in recommendation:
                        st.markdown(f'<div class="recommendation">{movie}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
