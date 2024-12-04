document.getElementById("registrationForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });

    const messageElement = document.getElementById("message");

    try {
        const response = await fetch("http://127.0.0.1:8000/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(jsonData),
        });

        const result = await response.json();

        if (response.ok) {
            messageElement.textContent = result.message;
            messageElement.className = "success";
            e.target.reset();
        } else {
            messageElement.textContent = result.error;
            messageElement.className = "error";
        }
    } catch (error) {
        messageElement.textContent = "An error occurred. Please try again later.";
        messageElement.className = "error";
    }
});
