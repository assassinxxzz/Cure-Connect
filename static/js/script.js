document.addEventListener('DOMContentLoaded', function() {
    const reviews = [
        { name: 'John Doe', rating: '★★★★☆', feedback: 'Great experience with the service! Very satisfied.' },
        // Add more reviews as needed
    ];

    const reviewContainer = document.getElementById('reviewContainer');
    const scrollLeftBtn = document.getElementById('scrollLeft');
    const scrollRightBtn = document.getElementById('scrollRight');

    // Function to create and append review cards
    function createReviewCard(review) {
        const reviewCard = document.createElement('div');
        reviewCard.classList.add('review-card');

        const reviewHeader = document.createElement('div');
        reviewHeader.classList.add('review-header');
        reviewHeader.innerHTML = `
            <h3>${review.name}</h3>
            <div class="star-ratings">${review.rating}</div>
        `;

        const reviewContent = document.createElement('p');
        reviewContent.classList.add('review-content');
        reviewContent.textContent = `"${review.feedback}"`;

        reviewCard.appendChild(reviewHeader);
        reviewCard.appendChild(reviewContent);

        reviewContainer.appendChild(reviewCard);
    }

    // Loop through the reviews array and create review cards
    reviews.forEach(review => {
        createReviewCard(review);
    });

    // Event listener for left arrow scroll
    scrollLeftBtn.addEventListener('click', function() {
        reviewContainer.scrollLeft -= 300; // Adjust the scroll distance as needed
    });

    // Event listener for right arrow scroll
    scrollRightBtn.addEventListener('click', function() {
        reviewContainer.scrollLeft += 300; // Adjust the scroll distance as needed
    });
});
