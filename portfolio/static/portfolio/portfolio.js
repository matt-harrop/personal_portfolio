const floatingNavBar = document.querySelector("#floatingNavBar");
const bioDiv = document.querySelector("#about");
let previousBioDivY = bioDiv.getBoundingClientRect().y;
const navBarTopBuffer = 20;

console.log(bioDiv.getBoundingClientRect().y);

document.addEventListener('scroll', function(e) {
    //Right here, need to check if the navbar is at the top of the viewport and then make it stick there if it is
    //by changing the position to relative(?) with a buffer from the top.

    if (previousBioDivY > navBarTopBuffer && bioDiv.getBoundingClientRect().y <= navBarTopBuffer) {
        // alert('Just scrolled past the top of the Bio Div (from above)!');
        floatingNavBar.classList.add('floating-nav-bar');
    } else if (previousBioDivY < navBarTopBuffer && bioDiv.getBoundingClientRect().y >= navBarTopBuffer) {
        // alert('Just scrolled past the top of the Bio Div! (from below)');
        floatingNavBar.classList.remove('floating-nav-bar');
    }

    previousBioDivY = bioDiv.getBoundingClientRect().y;
});

