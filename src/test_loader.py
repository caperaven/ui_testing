import sys
import os
import json


class TestLoader:
    def __init__(self):
        self.files = []
        self.load_file()
        self.load_folder()
        self.next_index = 0

        filtered = filter(lambda file: "skip." not in file, self.files)
        self.files = list(filtered)

    """
    get file from cmd, if exists, add to tests files to execute
    """

    def load_file(self):
        if "--file" in sys.argv:
            index = sys.argv.index("--file")
            file = sys.argv[index + 1]

            if os.path.isabs(file):
                self.files.append(file)
            else:
                file = os.path.join(os.getcwd(), file)
                self.files.append(os.path.realpath(file))

    """
    for a given folder, if defined, get the files tests files to execute    
    """

    def load_folder(self):
        if "--folder" in sys.argv:
            index = sys.argv.index("--folder")
            folder = sys.argv[index + 1]

            for root, dirnames, filenames in os.walk(folder):
                folder = os.path.realpath(root)
                for filename in filenames:
                    file = os.path.join(folder, filename)
                    self.files.append(file)

    """
    call this function to load the next test.json file as JSON and pass back the JSON object
    if you are at the end and there is nothing more to execute, return None
    """

    def next_test(self):
        if self.next_index > len(self.files) - 1:
            return None
        else:
            file = self.files[self.next_index]
            self.next_index += 1

            file = open(file)
            data = json.load(file)
            file.close()
            return data

    """
    what is the current test.json file being executed
    """

    def current_test_file(self):
        return self.files[self.next_index - 1]