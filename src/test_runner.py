class TestRunner:
    def __init__(self, logger):
        self.logger = logger

    def __del__(self):
        self.logger = None

    def run_test(self, json, results):
        self.logger.step(json["id"])
        return