import csv
from datetime import datetime

path = "C:\\Users\\HARSHA\\Downloads\\GSMData.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)
print(header)

data = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

print(data[0])


#compute and store daily stock returns

returns_path = "C:\\Users\HARSHA\\Downloads\google_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(['Date', "Return"])

for i in range(len(data) - 1):
    todays_day = data[i]
    todays_date = todays_day[0]
    todays_price = todays_day[-1]
    yesterday_row = data[i+1]
    yesterday_price = yesterday_row[-1]

    daily_return = (todays_price - yesterday_price) / yesterday_price

    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])

