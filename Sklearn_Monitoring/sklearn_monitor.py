# "Scikit-Learn Monitoring Data"
from sklearn import linear_model
from sklearn.cluster import SpectralClustering
import json
import pandas as pnd
from math import isnan
import numpy as np

# Import dataset
by_monitor_data = pnd.read_csv("C:\\Users\\justi\\Downloads\\annual_conc_by_monitor_2024\\annual_conc_by_monitor_2024.csv")

# New dataset dictionary
by_monitor_data2 = {}

# For-loop to edit monitor data
for item in np.arange(0, len(by_monitor_data["Parameter Name"])):
    # Nested try-excepts (there could be functions in place later)
    try:
        try:
            by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]]["Longitude"].append(by_monitor_data["Longitude"][item])
        except:
            by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]]["Longitude"].append(0)
        try:
            by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]]["Latitude"].append(by_monitor_data["Latitude"][item])
        except:
            by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]]["Latitude"].append(0)
        try:
            by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]]["Arithmetic Mean"].append(by_monitor_data["Arithmetic Mean"][item])
        except:
            by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]]["Arithmetic Mean"].append(0)
    except:
        try:
            try:
                by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]].update({"Longitude" : [by_monitor_data["Longitude"][item]]})
            except:
                by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]].update({"Longitude" : [0]})
            try:
                by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]].update({"Latitude" : [by_monitor_data["Latitude"][item]]})
            except:
                by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]].update({"Latitude" : [0]})
            try:
                by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]].update({"Arithmetic Mean" : [by_monitor_data["Arithmetic Mean"][item]]})
            except:
                by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]][by_monitor_data["Sample Duration"][item]].update({"Arithmetic Mean" : [0]})
        except:
            try:
                try:
                    by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]].update({by_monitor_data["Sample Duration"][item] : {"Longitude" : [by_monitor_data["Longitude"][item]]}})
                except:
                    by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]].update({by_monitor_data["Sample Duration"][item] : {"Longitude" : [0]}})
                try:
                    by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]].update({by_monitor_data["Sample Duration"][item] : {"Latitude" : [by_monitor_data["Latitude"][item]]}})
                except:
                    by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]].update({by_monitor_data["Sample Duration"][item] : {"Latitude" : [0]}})
                try:
                    by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]].update({by_monitor_data["Sample Duration"][item] : {"Arithmetic Mean" : [by_monitor_data["Arithmetic Mean"][item]]}})
                except:
                    by_monitor_data2[by_monitor_data["Units of Measure"][item]][by_monitor_data["Parameter Name"][item]].update({by_monitor_data["Sample Duration"][item] : {"Arithmetic Mean" : [0]}})
            except:
                try:
                    try:
                        by_monitor_data2[by_monitor_data["Units of Measure"][item]].update({by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Longitude" : [by_monitor_data["Longitude"][item]]}}})
                    except:
                        by_monitor_data2[by_monitor_data["Units of Measure"][item]].update({by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Longitude" : [0]}}})
                    try:
                        by_monitor_data2[by_monitor_data["Units of Measure"][item]].update({by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Latitude" : [by_monitor_data["Latitude"][item]]}}})
                    except:
                        by_monitor_data2[by_monitor_data["Units of Measure"][item]].update({by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Latitude" : [0]}}})
                    try:
                        by_monitor_data2[by_monitor_data["Units of Measure"][item]].update({by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Arithmetic Mean" : [by_monitor_data["Arithmetic Mean"][item]]}}})
                    except:
                        by_monitor_data2[by_monitor_data["Units of Measure"][item]].update({by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Arithmetic Mean" : [0]}}})
                except:
                    try:
                        by_monitor_data2.update({by_monitor_data["Units of Measure"][item] : {by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Longitude" : [by_monitor_data["Longitude"][item]]}}}})
                    except:
                        by_monitor_data2.update({by_monitor_data["Units of Measure"][item] : {by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Longitude" : [0]}}}})
                    try:
                        by_monitor_data2.update({by_monitor_data["Units of Measure"][item] : {by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Latitude" : [by_monitor_data["Latitude"][item]]}}}})
                    except:
                        by_monitor_data2.update({by_monitor_data["Units of Measure"][item] : {by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Latitude" : [0]}}}})
                    try:
                        by_monitor_data2.update({by_monitor_data["Units of Measure"][item] : {by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Arithmetic Mean" : [by_monitor_data["Arithmetic Mean"][item]]}}}})
                    except:
                        by_monitor_data2.update({by_monitor_data["Units of Measure"][item] : {by_monitor_data["Parameter Name"][item] : {by_monitor_data["Sample Duration"][item] : {"Arithmetic Mean" : [0]}}}})

xp = []
Yp = []

# Specific to Parts per Million under the Ozone hour with 1 Hour of Sample Duration
skl_monit_ppm_ozone_hour = by_monitor_data2["Parts per million"]["Ozone"]["1 HOUR"]
# For-loop converts data to X and Y for Scikit-Learn format
for item in np.arange(0, len(skl_monit_ppm_ozone_hour)):
    # Item added with Longitude and Latitude
    long = skl_monit_ppm_ozone_hour["Longitude"][item]
    lat = skl_monit_ppm_ozone_hour["Latitude"][item]
    arit_mean = skl_monit_ppm_ozone_hour["Arithmetic Mean"][item]
    # Skip the row if a value is NaN: if not, append
    if isnan(long) or isnan(lat) or isnan(arit_mean):
        pass
    else:
        # Initial list nested to X list
        xp.append([])
        # Append Longitude, and Latitude to the specific nested list
        xp[item].append(long)
        xp[item].append(lat)
        # Append Arithmetic Mean to resulting value lists
        Yp.append(arit_mean)


xp8 = []
Yp8 = []
# Selecting PPM Ozone data for 8 hour runs, beginning time as average of hour
skl_monit_ppm_ozone_8hr = by_monitor_data2["Parts per million"]["Ozone"]["8-HR RUN AVG BEGIN HOUR"]

# For-loop: Every data point in the length
for item in np.arange(0, len(skl_monit_ppm_ozone_8hr)):
    long = skl_monit_ppm_ozone_8hr["Longitude"][item]
    lat = skl_monit_ppm_ozone_8hr["Latitude"][item]
    arit_mean = skl_monit_ppm_ozone_8hr["Arithmetic Mean"][item]
    if isnan(long) or isnan(lat) or isnan(arit_mean):
        pass
    else:
        # Append an empty list to matrix
        xp8.append([])
        # Longitude added to that empty list first
        xp8[item].append(long)
        # Then Latitude
        xp8[item].append(lat)
        # Arithmetic Mean added (with any value that's NaN converted to 0)
        Yp8.append(arit_mean)
        



# Linear Regression object
reg = linear_model.LinearRegression()
# Fit
reg.fit(xp, Yp)

# Printed coefficient and intercept
print(reg.coef_)
print(reg.intercept_)
# Spectral Clustering 
sc = SpectralClustering(3)

print(sc.fit_predict(xp))


# Convert to JSON file
by_monitor_json = json.dumps(by_monitor_data2)


# Convert to dataFrame and then to CSV
df = pnd.DataFrame([by_monitor_json])
df.to_csv("monitoring_output.csv")
