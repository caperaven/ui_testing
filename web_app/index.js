const target = document.getElementById("target");
const DELAY = 0;


document.getElementById("btnSetAttribute").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.setAttribute("data-active", "true");
        document.getElementById("btnSetStyle").removeAttribute("disabled");
    }, DELAY);
})

document.getElementById("btnSetStyle").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.style.padding = "1rem";
        document.getElementById("btnSetText").removeAttribute("disabled");
    }, DELAY);
})

document.getElementById("btnSetText").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.textContent = "Test"
        document.getElementById("btnSetProperty").removeAttribute("disabled");
    }, DELAY);
})

document.getElementById("btnSetProperty").addEventListener("click", () => {
    const timeout = setTimeout(() => {
        clearTimeout(timeout);
        target.myProperty = "Test"
        document.getElementById("btnSetClass").removeAttribute("disabled");
    }, DELAY);
})

document.getElementById("btnSetClass").addEventListener("click", () => {
    target.classList.add("test");
})

document.getElementById("btnSetClass").addEventListener("click", () => {
    target.classList.add("test");
})

document.getElementById("btnNewTab").addEventListener("click", (event) => {
    window.open('/new-tab.html', '_blank');
})

document.getElementById("btnNewWindow").addEventListener("click", () => {
    window.open('/new-tab.html', '_blank', "width=200,height=100");
})