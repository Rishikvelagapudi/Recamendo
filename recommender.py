import pandas as pd
from similarity import get_similarity_matrix

def recommend_by_movie(movie_name: str, df: pd.DataFrame, top_n: int = 5):
    """
    Recommends movies similar to the given movie name.
    
    Args:
        movie_name: The name of the movie the user likes.
        df: Pandas DataFrame containing the dataset.
        top_n: Number of recommendations to return.
        
    Returns:
        A list of dictionaries containing recommended movies and their similarity scores.
    """
    # Case-insensitive matching for the movie name
    movie_name_lower = movie_name.lower()
    df_lower_names = df['Movie'].str.lower()
    
    if movie_name_lower not in df_lower_names.values:
        return {"error": "Movie not found in the dataset. Please try another one."}
    
    # Get the index of the movie that matches the name
    idx = df_lower_names[df_lower_names == movie_name_lower].index[0]
    
    # Calculate similarity matrix dynamically
    cosine_sim = get_similarity_matrix(df)
    
    # Get pairwise similarity scores for all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on the similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the scores of the top_n most similar movies
    # We slice from 1 to top_n+1 to exclude the movie itself (score of 1.0)
    top_movie_indices = sim_scores[1:top_n+1]
    
    recommendations = []
    for i, score in top_movie_indices:
        recommendations.append({
            "Movie": df['Movie'].iloc[i],
            "Genre": df['Genre'].iloc[i],
            "Rating": df.get('Rating', pd.Series([None]*len(df))).iloc[i],
            "Poster": df.get('Poster', pd.Series([None]*len(df))).iloc[i],
            "Similarity Score": f"{score * 100:.2f}%"
        })
        
    return {"data": recommendations}


def recommend_by_genre(genre_name: str, df: pd.DataFrame, top_n: int = 5):
    """
    Recommends top-rated movies for a specific genre.
    
    Args:
        genre_name: The genre chosen by the user.
        df: Pandas DataFrame containing the dataset.
        top_n: Number of recommendations to return.
        
    Returns:
        A list of dictionaries containing recommended movies.
    """
    # Filter the dataset by genre (case-insensitive and partial match)
    filtered_df = df[df['Genre'].str.contains(genre_name, case=False, na=False)]
    
    if filtered_df.empty:
        return {"error": f"No movies found for the genre: {genre_name}"}
    
    # If Rating exists, sort by Rating in descending order
    if 'Rating' in filtered_df.columns:
        filtered_df = filtered_df.sort_values(by='Rating', ascending=False)
        
    # Get the top N movies
    top_movies = filtered_df.head(top_n)
    
    recommendations = []
    for _, row in top_movies.iterrows():
        recommendations.append({
            "Movie": row['Movie'],
            "Genre": row['Genre'],
            "Rating": row.get('Rating', 'N/A'),
            "Poster": row.get('Poster', None)
        })
        
    return {"data": recommendations}
