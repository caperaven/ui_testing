# ui_testing

This project is for internal need but if you can get some use out of it, you are welcome to participate.  
The purpose of this project is to automate testing using a JSON test file that defines test steps.  
Once the tests are done, generate a results document.

It uses selenium web driver and assumes you have it installed and in the environment paths.

See the [tests folder](https://github.com/caperaven/ui_testing/tree/master/tests) for examples.

## Requirements

You will need the web driver for the browser installed and the path to that driver added to your environment variables PATH.  
For Chrome download your driver based on your chrome version here. 
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

Check your Chrome version by opening this URL in chrome.
[chrome://settings/help](chrome://settings/help)

If you have added your drivers to the path, make sure you restart your terminals and IDE before use.

## Running tests

Run the ui_testing.exe with the following parameters

You can either run a single test or run all the tests in the defined folder.  
For --file and --folder the next parameter needs to be the file or folder to use

1. --file ./tests/paging-toolbar.json 
2. --folder ./tests
3. --debug
4. --root https://127.0.0.1:8080

Use --debug if you want to have the dev tools automatically open when running tests.
use --root followed by the root URL if you want to return to a neutral page after each test.

