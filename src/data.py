data = {
    "scripts": {
        "is_ready": "document.querySelector('{}').addEventListener('isReady', (e) => e.target.dataset.ready = true)",
        "idle-false": "document.body.setAttribute('idle', false)",
        "idle-true": "crsbinding.idleTaskManager.add(() => document.body.setAttribute('idle', true))"
    }
}
