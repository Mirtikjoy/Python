items = [" Report.csv", " data.csv", " summary.CSV", " analysis.TXT", " results.csv"]

new_items = []

for item in items:
    item = item.strip().lower().replace(".txt", ".csv ")
    new_items.append(item)

print("Items:", ", ".join(new_items))