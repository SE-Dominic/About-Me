document.getElementById("contact-form").contactForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    try {
        const response = await fetch("http://127.0.0.1:8000/contact", {
            method: "POST",
            body: FormData(event.target),
        });
        if (!response.ok) { //not 200
            alert("[ERROR] RESPONSE ERROR: ", response.statusText);
            return;
        }
        let jsonData = await response.json();
        console.log(jsonData);
        window.location.href="/docs/index.html";
        return;
    } catch(error) {
        console.error("[ERROR]: Error fetching api\n", error);
        return;
    }
})
