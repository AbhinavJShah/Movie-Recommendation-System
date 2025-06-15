Movie Recommendation System

Description:
This project is a Content-Based Movie Recommendation System that suggests movies similar to a selected movie. 
It uses movie metadata like genres, cast, crew, keywords, and overview to find similar movies.
The system is deployed with a simple user interface using Streamlit.

Technologies Used:
- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit

How to Run:
1. Install the required libraries:
   pip install -r requirements.txt

2. Run the Streamlit app:
   streamlit run app.py

Project Files:
- app.py : Streamlit frontend application.
- movie_recommender.ipynb : Jupyter Notebook with data processing and model building.
- movies.csv : Final processed movie metadata.
- requirements.txt : List of required Python packages.
- README.txt : Project documentation.

Working:
- The dataset from TMDB is processed by combining important features.
- A "tags" feature is created that combines overview, genres, keywords, cast, and crew.
- Text processing and feature extraction are done using CountVectorizer.
- Cosine similarity is used to find and recommend similar movies.
- The user selects a movie through Streamlit and receives top 5 similar movies as recommendations.

Credits:
- The Movie Database (TMDB) for the dataset.
- Scikit-learn and Streamlit communities.