class CustomComponent extends HTMLElement {
    async connectedCallback() {
        this.innerHTML = await fetch(import.meta.url.replace(".js", ".html")).then(result => result.text());

        requestAnimationFrame(() => {
            setTimeout(() => {
                this.dataset.ready = "true";
                this.dataset.loaded = "true";
                this.isReady = true;
                this.dispatchEvent(new CustomEvent("isReady"));
            }, 1)
        })

        this.clickHandler = this.click.bind(this);
        this.dblClickHandler = this.dblClick.bind(this);
        this.contextClickHandler = this.contextClick.bind(this);

        this.addEventListener("click", this.clickHandler);
        this.addEventListener("dblclick", this.dblClickHandler);
        this.addEventListener("contextmenu", this.contextClickHandler);
    }

    async disconnectedCallback() {
        this.removeEventListener("click", this.clickHandler);
        this.removeEventListener("dblclick", this.dblClickHandler);
        this.removeEventListener("contextmenu", this.contextClickHandler);

        this.clickHandler = null;
        this.dblClickHandler = null;
        this.contextClickHandler = null;
    }

    click(event) {
        this.querySelector("h2").textContent = "click";
        event.preventDefault();
    }

    dblClick(event) {
        this.querySelector("h2").textContent = "dbl click";
        event.preventDefault();
    }

    contextClick(event) {
        this.querySelector("h2").textContent = "context click";
        event.preventDefault();
    }
}

customElements.define("custom-component", CustomComponent);