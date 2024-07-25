
// Dark Mode

$(document).ready(function () {
    let darkmode_V = $('#darkmode');

    if (darkmode_V.length) {
        darkmode_V.on('click', function() {
            const body = $('#body');
            const checkbox = $('.primary-nav input[type="checkbox"]');

            if (darkmode_V.prop('checked')) {
                body.addClass('dark-mode');
                checkbox.css('backgroundImage', 'url("https://cdn.wallpapersafari.com/57/21/c8YQa7.jpg")');
            } else {
                body.removeClass('dark-mode');
                checkbox.css('backgroundImage', 'url("http://getwallpapers.com/wallpaper/full/8/4/d/924696-large-sunny-day-background-1920x1080-for-4k-monitor.jpg")');
            }
        });
    } else {
        console.error('Darkmode checkbox not found.');
    }
});




// search
document.addEventListener('DOMContentLoaded', function() {
    const $searchField = document.querySelector("[data-search-field]");
    const $searchBtn = document.querySelector("[data-search-btn]");

    var someElement = document.getElementById('someElementId');
    $searchBtn.addEventListener("click", function () {
        const searchQuery = $searchField.value.trim().toLowerCase();
        if (searchQuery) {
            window.location.href = `Recipe?search=${encodeURIComponent(searchQuery)}`;
        }
    });

    $searchField.addEventListener("keydown", e => {
        if (e.key === "Enter") {
            $searchBtn.click();
        }
    });
});


// script.js
function saveRecipe(recipeId) {
    console.log(recipeId);
    $.ajax({
        url: '/save-recipe/' + recipeId + '/',
        type: 'GET',
        success: function(response) {
            // Update the button or perform any other UI updates
        },
        error: function(error) {
            console.log(error);
        }
    });
}




