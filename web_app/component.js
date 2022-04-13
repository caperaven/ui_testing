class CustomComponent extends HTMLElement {
    async connectedCallback() {
        this.innerHTML = await fetch(import.meta.url.replace(".js", ".html")).then(result => result.text());

        requestAnimationFrame(() => {
            setTimeout(() => {
                this.isReady = true;
                this.dispatchEvent(new CustomEvent("isReady"));
            }, 1)
        })
    }
}

customElements.define("custom-component", CustomComponent);