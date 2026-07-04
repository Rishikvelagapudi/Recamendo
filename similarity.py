import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity_matrix(df: pd.DataFrame, feature_col: str = 'Genre'):
    """
    Calculates the TF-IDF matrix and the cosine similarity matrix
    based on the specified feature column.
    
    Args:
        df: Pandas DataFrame containing the dataset.
        feature_col: The column containing text features (default is 'Genre').
        
    Returns:
        cosine_sim: A cosine similarity matrix.
    """
    # Initialize the TF-IDF Vectorizer
    # We use stop_words='english' to remove common English words if any exist in genres
    tfidf = TfidfVectorizer(stop_words='english')
    
    # Fill any missing values in the feature column with an empty string
    df[feature_col] = df[feature_col].fillna('')
    
    # Fit and transform the data into a TF-IDF matrix
    tfidf_matrix = tfidf.fit_transform(df[feature_col])
    
    # Compute the cosine similarity matrix from the TF-IDF matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    return cosine_sim
