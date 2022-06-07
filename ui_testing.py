# Command line arguments
# ------ Files --------------
# --file c:\\tests\\test.json.json
# --file ./../tests/test.json.json
# ------ Folders --------------
# --folder c:\\tests
# --folder ./../tests

# Additional flags
# --auto-open = open test folder when tests are done

from src.data import state
from src.test_loader import TestLoader
from src.test_runner import TestRunner
from src.test_logger import TestLogger
from src.test_scraper import TestScraper
from src.results_writer import save_results, set_results_folder
import sys
import tempfile
import subprocess

import os

folder = tempfile.gettempdir()
set_results_folder(folder)

# Test loader is responsible for:
# 1. discovering
# 2. loading
# 3. dishing
# of test.json files based on commandline arguments
test_loader = TestLoader()
test_scraper = TestScraper()

# Test logger prints the current test.json progress based on the number of tests running
test_logger = TestLogger(len(test_loader.files))

# Test runner executes json intent and populate the results file
test_runner = TestRunner(test_logger, test_scraper)

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

if "--auto-open" in sys.argv:
    path = state["folder"]
    subprocess.Popen(r'explorer /open,"{}"'.format(path))
    pass

# clean up memory by disposing of instances
del test_runner
del test_logger
del test_loader

