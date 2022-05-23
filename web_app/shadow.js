class ShadowComponent extends HTMLElement {
    async connectedCallback() {
        this.shadow = this.attachShadow({mode: 'open'});
        this.shadow.innerHTML = await fetch(import.meta.url.replace(".js", ".html")).then(result => result.text());

        requestAnimationFrame(() => {
            this.shadowRoot.querySelector("#edtFirstName").onchange =  event => this.dataset.firstname = event.target.value;
            this.shadowRoot.querySelector("#edtLastName").onchange = event => this.dataset.lastname = event.target.value;
            this.dataset.ready = "true";
        })
    }

    async disconnectedCallback() {
        this.shadowRoot.querySelector("#edtFirstName").onchange =  null;
        this.shadowRoot.querySelector("#edtLastName").onchange = null;
        this.shadow = null;
    }
}

customElements.define("shadow-component", ShadowComponent);