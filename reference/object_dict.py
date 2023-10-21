import scipy.io
import csv


def load_reference():
    colors = scipy.io.loadmat('data/color150.mat')['colors']
    names = {}
    with open(r'data/object150_info.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            names[int(row[0])] = row[5].split(";")[0]
    return names, colors


names, colors = load_reference()
