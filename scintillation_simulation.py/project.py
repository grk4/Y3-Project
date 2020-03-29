import csv

data_list = []


def read_data():
    with open("Sine 40kHz 20Vp2p 2 mic Scintillation near speaker test result.csv") as f:
        CSVreader = csv.reader(f)
        start_line = 8
        count = 0
        for row in CSVreader:
            if count >= start_line:
                data_list.append(row)
            count += 1


if __name__ == "__main__":
    read_data()
    print(data_list[4][1])
