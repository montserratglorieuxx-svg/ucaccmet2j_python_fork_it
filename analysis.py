import json
with open('precipitation.json') as file:
    data = json.load(file)

seattle=[]
for measurement in data: 
    if measurement["station"]=="GHCND:US1WAKG0038":
        seattle.append(measurement)


total_monthly_precipitation = {}
for measurement in seattle:
    split_date=measurement["date"].split("-")
    measurement["date"]=split_date[1]

    month = measurement['date']
    if month not in total_monthly_precipitation:
        total_monthly_precipitation[month] = 0
    total_monthly_precipitation[month] += measurement['value']

    measurement["date"]=split_date

print(total_monthly_precipitation)

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(total_monthly_precipitation, file, indent=4) 


total_yearly_precipitation = {}
for measurement in seattle:
    measurement["date"]=split_date[0]

    year = measurement['date']
    if year not in total_yearly_precipitation:
        total_yearly_precipitation[year] = 0
    total_yearly_precipitation[year] += measurement['value']

    measurement["date"]=split_date

print(total_yearly_precipitation)


# x=0
# total_yearly_precipitation = {}
# for month in total_monthly_precipitation:
#     x=x+month['value']