import requests

# Replace 'your_api_key' with your actual TMDB API key
API_KEY = 'your_api_key'
BASE_URL = 'https://api.themoviedb.org/3/movie/'

def get_movie_by_id(movie_id):
    url = f"{BASE_URL}{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None