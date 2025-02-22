from imdb import Cinemagoer
import json
from time import sleep
import random

def get_movies(num_movies=250):
    """Fetch top movies using Cinemagoer"""
    print("Creating Cinemagoer object...")
    ia = Cinemagoer()
    
    try:
        print("Fetching movies...")
        movies = []
        
        # List of IMDb Top 250 movie IDs
        top_movie_ids = [
            '0111161', '0068646', '0071562', '0468569', '0050083', '0108052', '0167260', '0110912', '0060196', '0120737',
            '0137523', '0109830', '0167261', '1375666', '0080684', '0133093', '0099685', '0073486', '0047478', '0114369',
            '0317248', '0076759', '0102926', '0038650', '0118799', '0120815', '0245429', '0120689', '0816692', '0114814',
            '0047396', '0054215', '0120586', '0021749', '0064116', '0034583', '0027977', '0253474', '1675434', '0103064',
            '0095327', '0095765', '0047478', '0078788', '0209144', '0082971', '0032553', '0043014', '0110413', '0078748',
            '0209144', '0405094', '0057012', '0081505', '0051201', '0071315', '0119698', '0364569', '0086879', '0057565',
            '0112573', '0095016', '0363163', '0105236', '0180093', '0086190', '0082096', '0022100', '0052357', '0211915',
            '0338013', '0033467', '0066921', '0093058', '0053125', '0066763', '0056172', '0053604', '0056592', '0012349',
            '0070735', '0017136', '0095327', '0040522', '0086250', '0071853', '0119488', '0042876', '0097576', '0042192',
            '0055630', '0372784', '0053291', '0040897', '0114709', '0059578', '0053198', '0087843', '0112641', '0105695',
            '0081398', '0057115', '0118849', '0051036', '0361748', '0062622', '0044741', '0093779', '0092005', '0091251',
            '0056801', '0113277', '0044079', '0056218', '0072684', '0075314', '0036775', '0053198', '0087544', '0079944',
            '0070047', '0113247', '0058946', '0052618', '0045152', '0041959', '0074958', '0083658', '0169102', '0046912',
            '0112471', '0084787', '0056217', '0047296', '0031679', '0083987', '0050976', '0116282', '0093437', '0077416',
            '0015864', '0050986', '0073195', '0117951', '0116231', '0015324', '0089881', '0071411', '0050212', '0019254',
            '0097165', '0119217', '0097441', '0015648', '0096283', '0074119', '0046268', '0091763', '0015324', '0084516',
            '0118715', '0046911', '0074896', '0092067', '0075686', '0084503', '0086879', '0046250', '0075148', '0079470',
            '0074486', '0092593', '0075467', '0046359', '0092099', '0091251', '0087884', '0092005', '0093058', '0091763',
            '0087544', '0079944', '0070047', '0113247', '0058946', '0052618', '0045152', '0041959', '0074958', '0083658',
            '0169102', '0046912', '0112471', '0084787', '0056217', '0047296', '0031679', '0083987', '0050976', '0116282',
            '0093437', '0077416', '0015864', '0050986', '0073195', '0117951', '0116231', '0015324', '0089881', '0071411',
            '0050212', '0019254', '0097165', '0119217', '0097441', '0015648', '0096283', '0074119', '0046268', '0091763',
            '0015324', '0084516', '0118715', '0046911', '0074896', '0092067', '0075686', '0084503', '0086879', '0046250',
            '0075148', '0079470', '0074486', '0092593', '0075467', '0046359', '0092099', '0091251', '0087884', '0092005'
        ]
        
        for movie_id in top_movie_ids:
            try:
                print(f"\nProcessing movie ID: {movie_id}")
                # Add random delay between 2-4 seconds
                sleep_time = random.uniform(2, 4)
                print(f"Waiting {sleep_time:.1f} seconds...")
                sleep(sleep_time)
                
                # Get detailed movie information
                print(f"Fetching details for movie ID: {movie_id}")
                movie_details = ia.get_movie(movie_id)
                
                if not movie_details:
                    print(f"No details found for movie ID: {movie_id}")
                    continue
                
                # Extract genres (if available)
                genres = ', '.join(movie_details.get('genres', []))
                
                # Create movie entry
                movie_data = {
                    "title": movie_details.get('title', ''),
                    "year": str(movie_details.get('year', '')),
                    "rating": str(movie_details.get('rating', '')),
                    "genre": genres
                }
                
                movies.append(movie_data)
                print(f"Successfully processed: {movie_data['title']}")
                
                # Save after each successful movie (in case of interruption)
                save_movies_to_file(movies, 'movies_temp.json')
                
            except Exception as e:
                print(f"Error processing movie {movie_id}: {str(e)}")
                print("Waiting 5 seconds before continuing...")
                sleep(5)
                continue
        
        print(f"\nTotal movies processed: {len(movies)}")
        return movies
    except Exception as e:
        print(f"Error fetching movies: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return []

def save_movies_to_file(movies, filename='movies.json'):
    """Save the movies list to a JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(movies, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error saving movies to file: {str(e)}")
        return False

def main():
    # Get the movie list
    print("Fetching movie data from IMDb...")
    movies = get_movies()
    
    # Save to file
    if movies:
        success = save_movies_to_file(movies)
        if success:
            print(f"Successfully saved {len(movies)} movies to movies.json")
        else:
            print("Failed to save movies to file")
    else:
        print("No movies to save")

if __name__ == "__main__":
    main()