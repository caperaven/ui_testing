class CustomComponent extends HTMLElement {
    async connectedCallback() {
        this.innerHTML = await fetch(import.meta.url.replace(".js", ".html")).then(result => result.text());

        requestAnimationFrame(() => {
            this.isReady = true;
            this.dispatchEvent(new CustomEvent("isReady"));
        })
    }
}

customElements.define("custom-component", CustomComponent);