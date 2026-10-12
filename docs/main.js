const contactForm = document.getElementById("contact-form");

contactForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(contactForm);
    try {
        const response = await fetch("http://127.0.0.1:8000/contact", {
            method: "POST",
            body: FormData(contactForm),
        });
        if (!response.ok) { //not 200
            alert("[ERROR] RESPONSE ERROR: ", response.error);
            return;
        }
        alert("Contact api connection successful", response.status);
        console.log(pack);
    } catch(error) {
        console.error("[ERROR]: Error fetching api.");
        return;
    }
})