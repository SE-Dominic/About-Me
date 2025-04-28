/*
These fetch functons are making an HTML request for the html pages
used in the templates folder. Then it returns a promise which we access using the
response keyword. using the response we .text() that information to get the text within the page
which we then change the html of the main.html file to the contents of our requested data.
*/
function loadSocialsTemplate() {
    fetch("templates/socialsTemplate.html")
        .then(Response =>Response.text())
        .then(html => {
            document.getElementById("main-page-content").innerHTML = html;
        })
        .catch(error => {
            console.error("Error loading specified template.", error);
        });
}

function loadProjectsTemplate() {
    fetch("templates/projectsTemplate.html")
        .then(Response => Response.text())
        .then (html => {
            document.getElementById("main-page-content").innerHTML = html;
        })
        .catch(error => {
            console.log("Error loading specified template.", error);
        });
}

function loadContactTemplate() {
    fetch("templates/contactTemplate.html")
        .then(Response => Response.text())
        .then (html => {
            document.getElementById("main-page-content").innerHTML = html;
        })
        .catch(error => {
            console.log("Error loading specified template.", error);
        });
}
