items = [" Report.csv", " data.csv", " summary.CSV", " analysis.TXT", " results.csv"]

for item in items:
    item = item.strip().lower().replace(".txt", ".csv ")
    print("Items:-",item, end=" ")

