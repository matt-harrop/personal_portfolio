const floatingNavBar = document.querySelector("#floatingNavBar");

const bioDiv = document.querySelector("#about");
const experienceDiv = document.querySelector("#experience");
const projectsDiv = document.querySelector("#projects");
const contactDiv = document.querySelector("#contact");

const bioNavButton = document.querySelector("#bioNavButton");
const projectsNavButton = document.querySelector("#projectsNavButton");
const contactNavButton = document.querySelector("#contactNavButton");
const experienceNavButton = document.querySelector("#experienceNavButton");

const projectImageOverlays = document.querySelectorAll(".project-image > .overlay");

const contactForm = document.querySelector('#contactForm')
const formSubmitButton = document.querySelector('#contactFormSubmitButton')

const projects = loadJson('#project-json-data');

let previousBioDivY = bioDiv.getBoundingClientRect().y;
const navBarTopBuffer = 20;

console.log(bioDiv.getBoundingClientRect().y);

document.addEventListener('scroll', function(e) {

    //Right here, need to check if the navbar is at the top of the viewport and then make it stick there if it is
    //by changing the position to relative(?) with a buffer from the top.
    if (previousBioDivY > navBarTopBuffer && bioDiv.getBoundingClientRect().y <= navBarTopBuffer) {
        floatingNavBar.classList.add('floating-nav-bar');
    } else if (previousBioDivY < navBarTopBuffer && bioDiv.getBoundingClientRect().y >= navBarTopBuffer) {
        floatingNavBar.classList.remove('floating-nav-bar');
    }
    previousBioDivY = bioDiv.getBoundingClientRect().y;


    //Highlight the navbar button for the section currently in focus
    updateHighlightedNavButton();

});

for (const element of projectImageOverlays) {
    element.addEventListener('mouseover', function(e) {
        for (const child of element.children) {
            child.hidden = false;
        }
    });
    element.addEventListener('mouseleave', function(e) {
        for (const child of element.children) {
            child.hidden = true;
        }
    });
    //Make each image overlay a link (if it has a good URL?):
    element.addEventListener('click', function(e) {
        // location.href =
    })
}

function loadJson(selector) {
  return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

function updateHighlightedNavButton() {

    const midPoint = window.innerHeight / 2;

    if (experienceDiv.getBoundingClientRect().y > midPoint) {
        bioNavButton.classList.add('nav-button-highlighted');
    } else {
        bioNavButton.classList.remove('nav-button-highlighted');
    }
    if (experienceDiv.getBoundingClientRect().y < midPoint && projectsDiv.getBoundingClientRect().y > midPoint) {
        experienceNavButton.classList.add('nav-button-highlighted');
    } else {
        experienceNavButton.classList.remove('nav-button-highlighted');
    }
    if (projectsDiv.getBoundingClientRect().y < midPoint && contactDiv.getBoundingClientRect().y > midPoint) {
        projectsNavButton.classList.add('nav-button-highlighted');
    } else {
        projectsNavButton.classList.remove('nav-button-highlighted');
    }
    if (contactDiv.getBoundingClientRect().y < midPoint) {
        contactNavButton.classList.add('nav-button-highlighted');
    } else {
        contactNavButton.classList.remove('nav-button-highlighted');
    }
}

contactForm.addEventListener('submit', function(e) {
    formSubmitButton.setAttribute('value', 'Sending...');
    const formData = new FormData(contactForm);
    console.log(formData.values())
    e.preventDefault();

    axios.post('save_message', formData)
        .then((res) => {
            contactForm.hidden = true;
            document.querySelector('.alert-success').hidden = false;
        })
        .catch((error) => {
            console.log(error)
            contactForm.hidden = true;
            document.querySelector('.alert-danger').hidden = false;
        })
    }
)
