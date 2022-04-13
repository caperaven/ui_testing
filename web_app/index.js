const target = document.getElementById("target");

document.getElementById("btnSetAttribute").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.setAttribute("data-active", "true");
        document.getElementById("btnSetStyle").removeAttribute("disabled");
    }, 1);
})

document.getElementById("btnSetStyle").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.style.background = "gray";
        document.getElementById("btnSetText").removeAttribute("disabled");
    }, 1);
})

document.getElementById("btnSetText").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.textContent = "Test"
        document.getElementById("btnSetProperty").removeAttribute("disabled");
    }, 1);
})

document.getElementById("btnSetProperty").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.myProperty = "Test"
    }, 1);
})
