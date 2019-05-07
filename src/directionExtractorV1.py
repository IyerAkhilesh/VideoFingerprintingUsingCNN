import re
from numpy.ma import array
from os import listdir
from os.path import isfile, join
import csv
import netifaces


def direction_finder(source_mac_address, destination_mac_address):
    # These strings have a "\n" appended to the end of them
    source_mac_address = source_mac_address.strip()
    destination_mac_address = destination_mac_address.strip()

    # this_pc = netifaces.ifaddresses(netifaces.interfaces()[7])[netifaces.AF_LINK][0]["addr"]
    this_pc_1 = "8a:6d:7b:cb:b7:4b"
    this_pc_2 = "78:0c:b8:f2:4d:bf"
    # print(this_pc)
    if this_pc_1 in source_mac_address or this_pc_2 in source_mac_address:
        # print("S", source_mac_address)
        return 1
    elif this_pc_1 in destination_mac_address or this_pc_2 in destination_mac_address:
        # print("D", destination_mac_address)
        return -1
    else:
        # print("S and D", source_mac_address, destination_mac_address)
        return 0


files = array([file for file in listdir("D:\\DatasetAndCSV\\NewCSVCaptures\\") if
               isfile(join("D:\\DatasetAndCSV\\NewCSVCaptures\\", file))])
for file_counter in range(0, len(files)):
    with open("D:\\DatasetAndCSV\\NewCSVCaptures\\" + files[file_counter]) as file_name:
        # print(file_name)
        # readlines gives a list of rows of file
        lines = file_name.read().split("\n")
        line_array = []
        for line in lines:
            line = line.replace("\x00", "")
            if line.strip().split(",") is not []:
                line_array.append(line.strip().split(","))

        with open("D:\\DatasetAndCSV\\New_CSV_files\\" + files[file_counter][0: files[file_counter].index(".")] + ".csv", "w+") as csv_file:

            csv_writer = csv.writer(csv_file)
            row = ["Direction"]
            # print(row)
            print("Starting writing into file "+files[file_counter]+".csv")
            csv_writer.writerow(row)

            for row_counter in range(0, len(line_array)):
                if len(line_array[row_counter]) != 1:
                    row = [direction_finder(str(line_array[row_counter][0]), str(line_array[row_counter][1]))]
                    csv_writer.writerow(row)
            print("Writing into file "+files[file_counter]+".csv finished!")
