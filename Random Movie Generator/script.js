document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-btn');
    const movieInfo = document.getElementById('movie-info');
    const movieTitle = document.getElementById('movie-title');
    const movieYear = document.getElementById('movie-year');
    const movieRating = document.getElementById('movie-rating');
    
    let movies = [];

    // Load movies from JSON file
    fetch('movies.json')
        .then(response => response.json())
        .then(data => {
            movies = data;
        })
        .catch(error => console.error('Error loading movies:', error));

    generateBtn.addEventListener('click', function() {
        if (movies.length === 0) {
            alert('Movie data not loaded yet. Please try again.');
            return;
        }

        const randomMovie = movies[Math.floor(Math.random() * movies.length)];
        
        movieTitle.textContent = randomMovie.title;
        movieYear.textContent = `Year: ${randomMovie.year}`;
        movieRating.textContent = `IMDB Rating: ${randomMovie.rating}`;
        
        movieInfo.classList.remove('hidden');
    });
});