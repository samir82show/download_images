import requests
import argparse
import os

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--imagename", required=True, help="name of the images")
    ap.add_argument("-f", "--file", required=True, help="The file contains the images urls")
    ap.add_argument("-d", "--targetdir", required=True, help="The dir will contain the images")
    args = vars(ap.parse_args())

    fd = open(args["file"], "r")
    num_lines = sum(1 for line in open(args["file"]))
    j = 0
    for i in fd:
        j += 1
        print(j, " out of ", num_lines)
        try:
            f = open(os.path.join(args["targetdir"], args["imagename"]) + str(j) + ".jpg",'wb')
            f.write(requests.get(i).content)
            f.close()
        except:
            print(i + " is not accessible")
    print ("finished: " + j)