document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generateBtn');
    const movieCard = document.getElementById('movieCard');
    const loadingElement = document.getElementById('loading');
    
    async function generateMovie() {
        loadingElement.style.display = 'block';
        movieCard.style.display = 'none';

        try {
            const response = await fetch('movies.json');
            const movies = await response.json();
            
            const randomMovie = movies[Math.floor(Math.random() * movies.length)];
            
            document.getElementById('movieTitle').textContent = randomMovie.title;
            document.getElementById('movieYear').textContent = randomMovie.year;
            document.getElementById('movieRating').textContent = randomMovie.rating;
            document.getElementById('movieGenre').textContent = randomMovie.genre;
            
            movieCard.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            alert('Error loading movies. Please try again.');
        } finally {
            loadingElement.style.display = 'none';
        }
    }

    generateBtn.addEventListener('click', generateMovie);
});
