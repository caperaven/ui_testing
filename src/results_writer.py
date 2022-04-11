from datetime import datetime
import json
import os


def save_results(results, folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

    now = datetime.now()
    file = os.path.realpath(os.path.join(folder, "{}_{}_{}_{}_{}_{}.json".format(now.year, now.month, now.day, now.hour, now.minute, now.second)))

    outfile = open(file, "w")
    json.dump(results, outfile, indent=4)
    outfile.close()
