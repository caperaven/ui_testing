# Command line arguments
# ------ Files --------------
# --file c:\\tests\\test.json.json
# --file ./../tests/test.json.json
# ------ Folders --------------
# --folder c:\\tests
# --folder ./../tests

from src.test_loader import TestLoader
from src.test_runner import TestRunner
from src.test_logger import TestLogger
from src.results_writer import save_results, set_results_folder
import tempfile

import os

folder = tempfile.gettempdir()
set_results_folder(folder)

# Test loader is responsible for:
# 1. discovering
# 2. loading
# 3. dishing
# of test.json files based on commandline arguments
test_loader = TestLoader()

# Test logger prints the current test.json progress based on the number of tests running
test_logger = TestLogger(len(test_loader.files))

# Test runner executes json intent and populate the results file
test_runner = TestRunner(test_logger)

# this will hold the test.json results
results = {}

# loop through the tests and execute them
while True:
    json = test_loader.next_test()
    if json is None:
        break

    file = test_loader.current_test_file()
    test_runner.run_test(json, results, file)

save_results(results)

# clean up memory by disposing of instances
del test_runner
del test_logger
del test_loader

