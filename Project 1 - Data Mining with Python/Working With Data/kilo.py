import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics 
def print_csv(thing):
	print("called method")
	with pd.option_context('display.max_rows', len(thing)):
		print(thing.to_string())

sfcrime_original = pd.read_csv("Data/SF-police-data-2016.csv")
sfdistricts_original = pd.read_csv("Data/SF_Police_Districts.csv", index_col='PdDistrict')
#print_csv(sfcrime_original)
print(sfcrime_original.keys())
# sfcrime_by_district = sfcrime_original.groupby("PdDistrict").aggregate('count')
#print(sfcrime_by_district)
crime_by_district = pd.crosstab(index=sfcrime_original["PdDistrict"],
                            columns=sfcrime_original["Category"])
crime_by_day = pd.crosstab(index=sfcrime_original["DayOfWeek"],
                            columns=sfcrime_original["Category"])
day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
crime_by_day.index = day_list
crime_by_district["Total"] = crime_by_district.apply(sum, axis=1)
# print(crime_crosstab["Total"])
crime_total_by_district = crime_by_district.drop(['ARSON', 'ASSAULT', 'BAD CHECKS', 'BRIBERY', 'BURGLARY',
       'DISORDERLY CONDUCT', 'DRIVING UNDER THE INFLUENCE', 'DRUG/NARCOTIC',
       'DRUNKENNESS', 'EMBEZZLEMENT', 'EXTORTION', 'FAMILY OFFENSES',
       'FORGERY/COUNTERFEITING', 'FRAUD', 'GAMBLING', 'KIDNAPPING',
       'LARCENY/THEFT', 'LIQUOR LAWS', 'LOITERING', 'MISSING PERSON',
       'NON-CRIMINAL', 'OTHER OFFENSES', 'PORNOGRAPHY/OBSCENE MAT',
       'PROSTITUTION', 'RECOVERED VEHICLE', 'ROBBERY', 'RUNAWAY',
       'SECONDARY CODES', 'SEX OFFENSES, FORCIBLE',
       'SEX OFFENSES, NON FORCIBLE', 'STOLEN PROPERTY', 'SUICIDE',
       'SUSPICIOUS OCC', 'TREA', 'TRESPASS', 'VANDALISM', 'VEHICLE THEFT',
       'WARRANTS', 'WEAPON LAWS'] ,axis=1)
print(crime_by_day)
outlier_dictionary = {}
# print(crime_by_day.keys())
for i in crime_by_day.keys():

	#print(crime_by_day[i].tolist())
	total = crime_by_day[i].sum(axis=0)
	mean = statistics.mean(crime_by_day[i].tolist())
	seventy_fifth_percentile = crime_by_day[i].quantile(.75)
	twenty_fifth_percentile = crime_by_day[i].quantile(.25)
	standard_deviation = statistics.stdev(crime_by_day[i].tolist())
	iqr = seventy_fifth_percentile - twenty_fifth_percentile
	# print(i, total)
	# print("Mean:", mean)
	# print("StDev:", standard_deviation)
	for j in range(len(crime_by_day[i].tolist())):
		toAdd = False
		if crime_by_day[i].tolist()[j] > 1.5*iqr + seventy_fifth_percentile:
			print(day_list[j], "is an high outlier for", i)
			outlier_dictionary[i] = (j, "high")
			toAdd = True
		if crime_by_day[i].tolist()[j] < twenty_fifth_percentile - 1.5*iqr:
			print(day_list[j], "is an low outlier for", i)
			outlier_dictionary[i] = (j, "low")
			toAdd = True
		if toAdd:
			crime_by_day.plot.bar(y=i)
			plt.title("Ammount of "+ str(i)+  " Crime Vs Day Of Week")
	plt.show()
	# f, (ax1, ax2) = plt.subplots(len(outlier_dictionary), sharex=False)
	# for i in outlier_dictionary:
	# 	crime_by_day.plot.bar(y=i[1][0])
	# plt.show()
# ax1.bar(den_delays_annual.index,den_delays_annual['Delayed'])
# ax2.bar(den_delays_annual.index,den_delays_annual['Percent Delayed'])








