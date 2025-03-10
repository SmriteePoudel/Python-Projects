import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

# Load movie data
movies = pd.read_csv("movies.csv")  
ratings = pd.read_csv("ratings.csv")  

# Data exploration
print(movies.head())
print(ratings.describe())

# Visualizing rating distribution
plt.figure(figsize=(8,5))
sns.histplot(ratings['rating'], bins=10, kde=True, color='blue')
plt.xlabel("Ratings")
plt.ylabel("Frequency")
plt.title("Distribution of Movie Ratings")
plt.show()


vectorizer = TfidfVectorizer(stop_words='english')
movies['genres'] = movies['genres'].fillna('')  
tfidf_matrix = vectorizer.fit_transform(movies['genres'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def recommend_movies(title, num_recommendations=5):
    if title not in movies['title'].values:
        return "Movie not found. Please check the title."
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies.iloc[movie_indices][['title', 'genres']]


reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.2)
model = SVD()
model.fit(trainset)


def predict_rating(user_id, movie_id):
    return model.predict(user_id, movie_id).est

# Example usage
bollywood_movies = [
    "Dilwale Dulhania Le Jayenge (1995)",
    "Kabhi Khushi Kabhie Gham (2001)",
    "Zindagi Na Milegi Dobara (2011)",
    "3 Idiots (2009)",
    "Gully Boy (2019)"
]

for movie in bollywood_movies:
    print(f"Recommended movies for {movie}:")
    print(recommend_movies(movie, 5))
    print("\n")

print("Predicted rating for user 1 and movie 1:", predict_rating(1, 1))