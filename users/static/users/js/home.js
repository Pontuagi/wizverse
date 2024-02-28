// home.js
function buttonColor(postId) {
    const agreeButton = document.getElementById(`agreeBtn-${postId}`);
  const disagreeButton = document.getElementById(`disagreeBtn-${postId}`);

  // Update agree button style on click
  agreeButton.addEventListener('click', () => {
    agreeButton.classList.add('bg-green-500');
    agreeButton.classList.remove('bg-blue-300');

    // Reset disagree button if it's red
    if (disagreeButton.classList.contains('bg-red-500')) {
      disagreeButton.classList.remove('bg-red-300');
      disagreeButton.classList.add('bg-blue-300');
    }
  });

  // Update disagree button style on click
  disagreeButton.addEventListener('click', () => {
    disagreeButton.classList.add('bg-red-500');
    disagreeButton.classList.remove('bg-blue-300');

    // Reset agree button if it's green
    if (agreeButton.classList.contains('bg-green-500')) {
      agreeButton.classList.remove('bg-green-500');
      agreeButton.classList.add('bg-blue-300');
    }
  });
}

