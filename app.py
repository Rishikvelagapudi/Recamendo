import streamlit as st
import pandas as pd
from recommender import recommend_by_movie, recommend_by_genre

# Set page configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎥",
    layout="centered"
)

# Load Dataset
@st.cache_data
def load_data():
    try:
        return pd.read_csv("dataset.csv")
    except FileNotFoundError:
        st.error("Error: dataset.csv not found!")
        return None

df = load_data()

# App Title
st.title("🎥 AI Movie Recommendation System")
st.markdown("Discover your next favorite movie based on your interests!")

if df is not None:
    # Sidebar for preferences
    st.sidebar.header("Recommendation Options")
    option = st.sidebar.radio("How would you like to get recommendations?", 
                              ("By Movie Name", "By Genre"))
    
    # Number of recommendations
    top_n = st.sidebar.slider("Number of recommendations", min_value=1, max_value=20, value=5)

    if option == "By Movie Name":
        st.subheader("Search by Movie Name")
        movie_name = st.text_input("Enter a movie you like (e.g., Interstellar, Batman):")
        
        if st.button("Recommend Movies"):
            if movie_name.strip():
                with st.spinner("Finding similar movies..."):
                    result = recommend_by_movie(movie_name, df, top_n)
                    
                    if "error" in result:
                        st.error(result["error"])
                    else:
                        st.success(f"Top {len(result['data'])} movies similar to '{movie_name}':")
                        for item in result["data"]:
                            st.write("---")
                            col1, col2 = st.columns([1, 3])
                            with col1:
                                if item.get('Poster') and pd.notnull(item['Poster']):
                                    st.image(item['Poster'], use_container_width=True)
                            with col2:
                                st.markdown(f"**{item['Movie']}**")
                                st.write(f"🎭 Genre: {item['Genre']}")
                                if pd.notnull(item['Rating']):
                                    st.write(f"⭐ Rating: {item['Rating']}")
                                st.write(f"📊 Similarity Score: {item['Similarity Score']}")
            else:
                st.warning("Please enter a movie name.")

    elif option == "By Genre":
        st.subheader("Search by Genre")
        
        # Get unique genres from the dataset
        # We split by comma if there are multiple genres and get unique values
        all_genres = set()
        for genres in df['Genre'].dropna():
            for g in genres.split(','):
                all_genres.add(g.strip())
        unique_genres = sorted(list(all_genres))
        
        genre_name = st.selectbox("Choose a Genre:", [""] + unique_genres)
        
        if st.button("Recommend Movies"):
            if genre_name:
                with st.spinner("Finding top movies in this genre..."):
                    result = recommend_by_genre(genre_name, df, top_n)
                    
                    if "error" in result:
                        st.error(result["error"])
                    else:
                        st.success(f"Top {len(result['data'])} movies in '{genre_name}':")
                        for item in result["data"]:
                            st.write("---")
                            col1, col2 = st.columns([1, 3])
                            with col1:
                                if item.get('Poster') and pd.notnull(item['Poster']):
                                    st.image(item['Poster'], use_container_width=True)
                            with col2:
                                st.markdown(f"**{item['Movie']}**")
                                st.write(f"🎭 Genre: {item['Genre']}")
                                if pd.notnull(item['Rating']):
                                    st.write(f"⭐ Rating: {item['Rating']}")
            else:
                st.warning("Please select a genre.")
else:
    st.warning("Please ensure dataset.csv is in the project folder.")
