import pickle
from flask import Flask, request, jsonify, render_template
import pandas as pd
import requests

TMDB_API_KEY = "YOUR-TMDB-API-KEY"

try:

    movies = pickle.load(open('df.pkl','rb')) 
    similarity = pickle.load(open('similarity.pkl','rb'))
    print("Models loaded successfully!")
    
except Exception as e:
    print(f"Error loading models: {e}")
    exit()

app = Flask(__name__)


def fetch_poster(movie_id):
    """TMDB API se movie poster ka URL fetch karta hai."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    try:
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        return "https://via.placeholder.com/500x750.png?text=No+Poster" 
    except Exception:
        return "https://via.placeholder.com/500x750.png?text=Error"



def recommend(movie_title, count=5):
    """Recommendation nikalta hai aur posters ke URLs aur IDs bhi deta hai."""
    try:

        index = movies[movies['title'].str.lower() == movie_title.lower()].index[0]
    except IndexError:
        return {"names": ["Movie not found in the dataset. Please check the spelling."], "posters": [], "ids": []}


    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_ids = []


    for i in distances[1:count+1]: 

        id = int(movies.iloc[i[0]].id) 
        
        recommended_movie_posters.append(fetch_poster(id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_ids.append(id)
        
    return {"names": recommended_movie_names, "posters": recommended_movie_posters, "ids": recommended_movie_ids}





@app.route('/')
def home():
    """index.html ko load karta hai aur titles ki list bhejta hai autocomplete ke liye."""

    movie_list = movies['title'].astype(str).tolist()
    return render_template('index.html', movies_list=movie_list)


@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    movie_name = data.get('movie_name', '')

    count = int(data.get('count', 5)) 
    
    results = recommend(movie_name, count=count) 

    return jsonify({
        'recommendations': results['names'], 
        'posters': results['posters'],
        'ids': results['ids'] 
    })

if __name__ == '__main__':

    app.run(debug=True)