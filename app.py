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
    # Top-N is hardcoded to 5 recommendations
    
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
                result = recommend_by_genre(genre_name, df, 5)
                
                if "error" in result:
                    st.error(result["error"])
                else:
                    st.success(f"Top {len(result['data'])} movies in '{genre_name}':")
                    
                    # Display in a grid format with up to 5 columns per row
                    cols_per_row = 5
                    for i in range(0, len(result["data"]), cols_per_row):
                        cols = st.columns(cols_per_row)
                        for j in range(cols_per_row):
                            if i + j < len(result["data"]):
                                item = result["data"][i + j]
                                with cols[j]:
                                    if item.get('Poster') and pd.notnull(item['Poster']):
                                        st.image(item['Poster'], use_container_width=True)
                                    st.markdown(f"**{item['Movie']}**")
                                    st.write(f"🎭 {item['Genre']}")
                                    if pd.notnull(item['Rating']):
                                        st.write(f"⭐ {item['Rating']}")
                                    st.write("---")
        else:
            st.warning("Please select a genre.")
else:
    st.warning("Please ensure dataset.csv is in the project folder.")
