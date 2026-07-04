# AI Recommendation System Using Content-Based Filtering

## Project Overview
This project is an AI-powered Recommendation System that suggests items (movies) based on a user's interests. It uses Content-Based Filtering with TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity to find movies similar to a user's favorite movie. It also supports simple genre-based filtering. 

The project does not require deep learning and is built entirely using Python, Pandas, Scikit-learn, and Streamlit for the graphical user interface.

## Workflow
1. **Load Dataset**: Read the `dataset.csv` file using Pandas.
2. **Clean & Prepare Data**: Handle missing values and format data.
3. **Take User Input**: Accept user preference (Movie name or Genre) via Streamlit GUI.
4. **Feature Extraction**: Convert text features (Genres) into numerical vectors using `TfidfVectorizer`.
5. **Calculate Similarity**: Compute the Cosine Similarity between movie vectors.
6. **Generate Recommendations**: Rank movies based on similarity scores or ratings.
7. **Display Results**: Show the top-N recommended movies to the user.

## Technologies Used
* **Python**: Core programming language.
* **Pandas**: Data manipulation and loading.
* **NumPy**: Numerical operations.
* **Scikit-learn**: For `TfidfVectorizer` and `cosine_similarity`.
* **Streamlit**: Web interface for the application.

## Installation

1. Clone or download this repository.
2. Ensure you have Python installed.
3. Install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:

```bash
streamlit run app.py
```

2. Open the URL provided in your terminal (usually `http://localhost:8501`).
3. Use the sidebar to choose how you want to search:
   - **By Movie Name**: Enter a movie like "Interstellar" to get similar recommendations using AI.
   - **By Genre**: Select a genre like "Action" to get the top-rated movies in that genre.
4. Adjust the slider to see Top-5, Top-10, or Top-20 recommendations.

## Screenshots

*(Create a `screenshots` folder and place screenshots of your working app here, for example: `screenshots/output.png`)*

## Project Structure
- `dataset.csv`: Contains the sample movie data (Movie, Genre, Rating).
- `similarity.py`: Core machine learning logic (TF-IDF & Cosine Similarity).
- `recommender.py`: Functions to generate recommendations.
- `app.py`: Streamlit frontend application.
- `requirements.txt`: Python dependencies.
- `README.md`: This documentation file.

## Future Improvements
- User login system to save user history.
- Implement Collaborative filtering.
- Hybrid recommendation system (Content + Collaborative).
- Fetch Movie posters dynamically using a public API (like OMDB or TMDB).
- Voice-based recommendations.
- Advanced search suggestions and genre filters.
- Deployment on Streamlit Cloud or Render.
