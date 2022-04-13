const target = document.getElementById("target");

document.getElementById("btnSetAttribute").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.setAttribute("data-active", "true");
        document.getElementById("btnSetStyle").removeAttribute("disabled");
    }, 1000);
})

document.getElementById("btnSetStyle").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.style.padding = "1rem";
        document.getElementById("btnSetText").removeAttribute("disabled");
    }, 1000);
})

document.getElementById("btnSetText").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.textContent = "Test"
        document.getElementById("btnSetProperty").removeAttribute("disabled");
    }, 1000);
})

document.getElementById("btnSetProperty").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.myProperty = "Test"
    }, 1000);
})
