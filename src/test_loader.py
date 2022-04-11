import sys
import os
import json


class TestLoader:
    def __init__(self):
        self.files = []
        self.load_file()
        self.load_folder()
        self.next_index = 0

    def load_file(self):
        if "--file" in sys.argv:
            index = sys.argv.index("--file")
            file = sys.argv[index + 1]

            if os.path.isabs(file):
                self.files.append(file)
            else:
                file = os.path.join(os.path.dirname(__file__), file)
                self.files.append(os.path.realpath(file))

    def load_folder(self):
        if "--folder" in sys.argv:
            index = sys.argv.index("--folder")
            folder = sys.argv[index + 1]

            if os.path.isabs(folder):
                files = os.listdir(folder)
                self.files.append(files)
            else:
                folder = os.path.join(os.path.dirname(__file__), folder)
                folder = os.path.realpath(folder)
                files = os.listdir(folder)

                for file in files:
                    self.files.append(os.path.join(folder, file))

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
