import json

with open('precipitation.json') as file:
    data = json.load(file)

city_list=[]
state_list=[]
code_list=[]

with open("stations.csv", 'r') as file:
  file.readline()
  for row in file: 
    split_row=row.split(",")
    city_list.append(split_row[0])
    state_list.append(split_row[1])
    code_list.append(split_row[2])


for code in code_list:
    city=[]
    for measurement in data: 
        if measurement["station"]==code:
            city.append(measurement)
    #print(city)
    

    total_monthly_precipitation = {}
    for measurement in city:
        split_date=measurement["date"].split("-")
        measurement["date"]=split_date[1]

        month = measurement['date']
        if month not in total_monthly_precipitation:
            total_monthly_precipitation[month] = 0
        total_monthly_precipitation[month] += measurement['value']

        measurement["date"]=split_date

    print(total_monthly_precipitation)

    # with open('results.json', 'w', encoding='utf-8') as file:
    #     json.dump(total_monthly_precipitation, file, indent=4) 


    total_yearly_precipitation = {}
    for measurement in city:
        measurement["date"]=split_date[0]

        year = measurement['date']
        if year not in total_yearly_precipitation:
            total_yearly_precipitation[year] = 0
        total_yearly_precipitation[year] += measurement['value']

        measurement["date"]=split_date

    print(total_yearly_precipitation)

    relative_monthly_precipitation = {}
    for month in total_monthly_precipitation:
        relative=(total_monthly_precipitation[month]*(100/total_yearly_precipitation["2010"]))
        relative_monthly_precipitation[month]=relative

    print(relative_monthly_precipitation)

    # with open('relative_results.json', 'w', encoding='utf-8') as file:
    #     json.dump(relative_monthly_precipitation, file, indent=4) 
    
    
    
    city=[]
    city_list=[]
    state_list=[]
    code_list=[]


# seattle=[]
# for measurement in data: 
#     if measurement["station"]=="GHCND:US1WAKG0038":
#         seattle.append(measurement)


# total_monthly_precipitation = {}
# for measurement in seattle:
#     split_date=measurement["date"].split("-")
#     measurement["date"]=split_date[1]

#     month = measurement['date']
#     if month not in total_monthly_precipitation:
#         total_monthly_precipitation[month] = 0
#     total_monthly_precipitation[month] += measurement['value']

#     measurement["date"]=split_date

# print(total_monthly_precipitation)

# with open('results.json', 'w', encoding='utf-8') as file:
#     json.dump(total_monthly_precipitation, file, indent=4) 


# total_yearly_precipitation = {}
# for measurement in seattle:
#     measurement["date"]=split_date[0]

#     year = measurement['date']
#     if year not in total_yearly_precipitation:
#         total_yearly_precipitation[year] = 0
#     total_yearly_precipitation[year] += measurement['value']

#     measurement["date"]=split_date

# print(total_yearly_precipitation)

# relative_monthly_precipitation = {}
# for month in total_monthly_precipitation:
#     relative=(total_monthly_precipitation[month]*(100/total_yearly_precipitation["2010"]))
#     relative_monthly_precipitation[month]=relative

# print(relative_monthly_precipitation)

# with open('relative_results.json', 'w', encoding='utf-8') as file:
#     json.dump(relative_monthly_precipitation, file, indent=4) 


# ############################################
    
# Cincinnati=[]
# for measurement in data: 
#     if measurement["station"]=="GHCND:USW00093814":
#         Cincinnati.append(measurement)


# total_monthly_precipitation = {}
# for measurement in Cincinnati:
#     split_date=measurement["date"].split("-")
#     measurement["date"]=split_date[1]

#     month = measurement['date']
#     if month not in total_monthly_precipitation:
#         total_monthly_precipitation[month] = 0
#     total_monthly_precipitation[month] += measurement['value']

#     measurement["date"]=split_date

# print(total_monthly_precipitation)

# with open('results.json', 'w', encoding='utf-8') as file:
#     json.dump(total_monthly_precipitation, file, indent=4) 


# total_yearly_precipitation = {}
# for measurement in seattle:
#     measurement["date"]=split_date[0]

#     year = measurement['date']
#     if year not in total_yearly_precipitation:
#         total_yearly_precipitation[year] = 0
#     total_yearly_precipitation[year] += measurement['value']

#     measurement["date"]=split_date

# print(total_yearly_precipitation)

# relative_monthly_precipitation = {}
# for month in total_monthly_precipitation:
#     relative=(total_monthly_precipitation[month]*(100/total_yearly_precipitation["2010"]))
#     relative_monthly_precipitation[month]=relative

# print(relative_monthly_precipitation)

# with open('relative_results.json', 'w', encoding='utf-8') as file:
#     json.dump(relative_monthly_precipitation, file, indent=4) 

# ##################################################

# Maui=[]
# for measurement in data: 
#     if measurement["station"]=="stations.csv":
#         Maui.append(measurement)


# total_monthly_precipitation = {}
# for measurement in Maui:
#     split_date=measurement["date"].split("-")
#     measurement["date"]=split_date[1]

#     month = measurement['date']
#     if month not in total_monthly_precipitation:
#         total_monthly_precipitation[month] = 0
#     total_monthly_precipitation[month] += measurement['value']

#     measurement["date"]=split_date

# print(total_monthly_precipitation)

# with open('results.json', 'w', encoding='utf-8') as file:
#     json.dump(total_monthly_precipitation, file, indent=4) 


# total_yearly_precipitation = {}
# for measurement in seattle:
#     measurement["date"]=split_date[0]

#     year = measurement['date']
#     if year not in total_yearly_precipitation:
#         total_yearly_precipitation[year] = 0
#     total_yearly_precipitation[year] += measurement['value']

#     measurement["date"]=split_date

# print(total_yearly_precipitation)

# relative_monthly_precipitation = {}
# for month in total_monthly_precipitation:
#     relative=(total_monthly_precipitation[month]*(100/total_yearly_precipitation["2010"]))
#     relative_monthly_precipitation[month]=relative

# print(relative_monthly_precipitation)

# with open('relative_results.json', 'w', encoding='utf-8') as file:
#     json.dump(relative_monthly_precipitation, file, indent=4) 

# ####################################################

# San_Diego=[]
# for measurement in data: 
#     if measurement["station"]=="stations.csv":
#         San_Diego.append(measurement)


# total_monthly_precipitation = {}
# for measurement in San_Diego:
#     split_date=measurement["date"].split("-")
#     measurement["date"]=split_date[1]

#     month = measurement['date']
#     if month not in total_monthly_precipitation:
#         total_monthly_precipitation[month] = 0
#     total_monthly_precipitation[month] += measurement['value']

#     measurement["date"]=split_date

# print(total_monthly_precipitation)

# with open('results.json', 'w', encoding='utf-8') as file:
#     json.dump(total_monthly_precipitation, file, indent=4) 


# total_yearly_precipitation = {}
# for measurement in seattle:
#     measurement["date"]=split_date[0]

#     year = measurement['date']
#     if year not in total_yearly_precipitation:
#         total_yearly_precipitation[year] = 0
#     total_yearly_precipitation[year] += measurement['value']

#     measurement["date"]=split_date

# print(total_yearly_precipitation)

# relative_monthly_precipitation = {}
# for month in total_monthly_precipitation:
#     relative=(total_monthly_precipitation[month]*(100/total_yearly_precipitation["2010"]))
#     relative_monthly_precipitation[month]=relative

# print(relative_monthly_precipitation)

# with open('relative_results.json', 'w', encoding='utf-8') as file:
#     json.dump(relative_monthly_precipitation, file, indent=4) 

    
# #calculate relative_monthly_precipitation
# for month in total_monthly_precipitation:

#     *(total_yearly_precipitation[]/100)
