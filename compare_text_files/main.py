# https://www.reddit.com/r/learnpython/comments/je0kd3/compare_two_text_files_and_save_matching_values/

import csv

class FA():
    def __init__(self, x, y, yerr):
        self.x = x
        self.y = y
        self.yerr = yerr

    def tolerates(self, val):
        return -self.yerr <= (self.x - val) <= self.yerr

class FB():
    def __init__(self, x_n):
        self.x_n = x_n

class FC():
    def __init__(self, x_n, y, yerr):
        self.x_n = x_n
        self.y = y
        self.yerr = yerr

a_list = []
b_list = []
c_list = []

# Read FA.csv file contents and store in a_list
with open("FA.csv") as fa_file:
    reader = csv.DictReader(fa_file)
    for row in reader:
        x = float(row["x"])
        y = float(row["y"])
        yerr = float(row["yerr"])
        a_list.append(FA(x, y, yerr))

# Read FB.csv file contents and store in b_list
with open("FB.csv") as fb_file:
    reader = csv.DictReader(fb_file)
    for row in reader:
        x_n = float(row["x_n"])
        b_list.append(FB(x_n))

# Find matches within error tolerance range and store in c_list
for b in b_list:
    for a in a_list:
        if a.tolerates(b.x_n):
            c_list.append(FC(b.x_n, a.y, a.yerr))

# Write output to OUT.csv
with open('OUT.csv', "w", newline='') as out_file:
    writer = csv.DictWriter(out_file, fieldnames = ["x_n", "y", "yerr"])
    writer.writeheader()
    for c in c_list:
        row = {}
        row["x_n"]  = "%g" % c.x_n
        row["y"]    = "%g" % c.y
        row["yerr"] = "%g" % c.yerr
        writer.writerow(row)