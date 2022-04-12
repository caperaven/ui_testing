class CustomComponent extends HTMLElement {
    async connectedCallback() {
        this.innerHTML = await fetch(import.meta.url.replace(".js", ".html")).then(result => result.text());

        requestAnimationFrame(() => {
            //this.isReady = true;

            setTimeout(() => {
                this.dispatchEvent(new CustomEvent("isReady"));
            }, 15000)
        })
    }
}

customElements.define("custom-component", CustomComponent);