document.querySelectorAll('.agreeBtn, .disagreeBtn').forEach(button => {
    button.addEventListener('click', function() {
        const postId = this.getAttribute('data-post-id');
        const isAgree = this.classList.contains('agreeBtn');
        const url = isAgree ? '{% url "agree_post" 0 %}'.replace('0', postId) : '{% url "disagree_post" 0 %}'.replace('0', postId);
        
        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            },
            credentials: 'same-origin'
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Update button color based on the clicked button
            this.style.backgroundColor = isAgree ? 'green' : 'red';

            // Update agree and disagree counts as before
            const agreeCount = data.agree_count;
            const disagreeCount = data.disagree_count;
            document.querySelector(`.agree-count[data-post-id="${postId}"]`).innerText = agreeCount;
            document.querySelector(`.disagree-count[data-post-id="${postId}"]`).innerText = disagreeCount;
        })
        .catch(error => {
            console.error('There was an error with the fetch operation:', error);
        });
    });
});
