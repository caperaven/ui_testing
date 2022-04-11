class TestLogger:
    def __init__(self, test_count):
        self.test_count = test_count
        self.progress = 0

    def step(self, test_id):
        self.progress += 1

        print("Test {progress}/{count}: {id}".format(
            progress=self.progress,
            count=self.test_count,
            id=test_id
        ))
