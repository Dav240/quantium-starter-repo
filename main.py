import csv

csvFiles = ["data/daily_sales_data_0.csv","data/daily_sales_data_1.csv","data/daily_sales_data_2.csv"]

def priceToFloat(price):
    return float(price.replace("$", ""))

with open("output.csv", mode="w", newline="") as outputFile:
    writer = csv.writer(outputFile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["sales", "date", "region"])
    for filePath in csvFiles:
        with open(filePath, newline="") as csvFile:
            reader = csv.reader(csvFile, delimiter=",", quotechar='"')
            for row in reader:
                if row[0] == "pink morsel":
                    price = priceToFloat(row[1])
                    quantity = int(row[2])
                    writer.writerow([price*quantity, row[3], row[4]])

