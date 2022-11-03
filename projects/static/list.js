const forms = document.querySelectorAll(".is_completed")
for (let form of forms) {
    const checkbox = form.querySelector("input[type=checkbox]")
    checkbox.addEventListener("click", (event) => {
        form.submit()
    })
}