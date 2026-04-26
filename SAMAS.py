import pandas as pd
import numpy as np
import csv
import os
import matplotlib.pyplot as plt

class FarmRecord:
    def __init__(self, date, crop, moisture, temp, rainfall, fertilizer):
        self.date = date
        self.crop = crop
        self.moisture = moisture
        self.temp = temp
        self.rainfall = rainfall
        self.fertilizer = fertilizer
    def to_list(self):
        return [self.date, self.crop, self.moisture,
                self.temp, self.rainfall, self.fertilizer]
records = []
def add_record():
    try:
        date = input("Enter date: ")
        crop = input("Enter crop: ")
        moisture = float(input("Enter moisture: "))
        temp = float(input("Enter temperature: "))
        rainfall = float(input("Enter rainfall: "))
        fertilizer = input("Enter fertilizer: ")

        rec = FarmRecord(date, crop, moisture, temp, rainfall, fertilizer)
        records.append(rec)
        print("Record Added")
    except ValueError:
        print("Invalid input Enter numeric values properly")
def view_records():
    if not records:
        print("No records available")
        return
    print("\nRECORDS")
    for r in records:
        print(r.to_list())
def save_file():
    try:
        with open("farm_data.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Crop", "Moisture", "Temp", "Rainfall", "Fertilizer"])

            for r in records:
                writer.writerow(r.to_list())
        print("Data Saved")
    except Exception as e:
        print("Error saving file:", e)
def load_file():
    if not os.path.exists("farm_data.csv"):
        print("No previous file found")
        return

    try:
        with open("farm_data.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                rec = FarmRecord(
                    row[0], row[1],
                    float(row[2]), float(row[3]),
                    float(row[4]), row[5]
                )
                records.append(rec)

        print("Data Loaded")

    except Exception as e:
        print("Error loading file:", e)

def analysis():
    if not records:
        print("No data available")
        return

    data = [r.to_list() for r in records]
    df = pd.DataFrame(data, columns=["Date", "Crop", "Moisture", "Temp", "Rainfall", "Fertilizer"])

    print("\nDATA TABLE")
    print(df)

    print("\nANALYSIS")
    print("Average Moisture:", np.mean(df["Moisture"]))
    print("Max Temperature:", np.max(df["Temp"]))
    print("Total Rainfall:", np.sum(df["Rainfall"]))

    low = df[df["Moisture"] < 30]
    if not low.empty:
        print("\nLow Moisture Days")
        print(low)

    plt.figure()
    plt.plot(df["Date"], df["Moisture"], marker='o')
    plt.title("Moisture Levels Over Time")
    plt.xlabel("Date")
    plt.ylabel("Moisture")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.bar(df["Date"], df["Rainfall"])
    plt.title("Rainfall Distribution")
    plt.xlabel("Date")
    plt.ylabel("Rainfall")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    crop_counts = df["Crop"].value_counts()

    plt.figure()
    plt.pie(crop_counts, labels=crop_counts.index, autopct='%1.1f%%')
    plt.title("Crop Distribution")
    plt.tight_layout()
    plt.show()

def search():
    name = input("Enter crop name: ").lower()
    found = False

    for r in records:
        if name in r.crop.lower():
            print(r.to_list())
            found = True

    if not found:
        print("No record found")

def main():
    load_file()

    while True:
        print("\nSAMAS SYSTEM")
        print("1 Add Record")
        print("2 View Records")
        print("3 Save Data")
        print("4 Analysis")
        print("5 Search")
        print("6 Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                add_record()
            elif choice == 2:
                view_records()
            elif choice == 3:
                save_file()
            elif choice == 4:
                analysis()
            elif choice == 5:
                search()
            elif choice == 6:
                save_file()
                print("Exiting")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Enter a number only")

main()
