# -*- coding: utf-8 -*-
"""
Created on Wed May 28 23:03:14 2025

@author: DELL
"""
import os 
os.chdir(r"D:\Data Analytics\Google - Data Analytics\8 Google Data Analytics Capstone Complete a Case Study\Dataset")
# import the necessary Libraries
import pandas as pd 


# Load both sheets
sheet1 = pd.read_csv("Divvy_Trips_2019_Q1/Divvy_Trips_2019_Q1.csv")

sheet2 = pd.read_csv("Divvy_Trips_2020_Q1/Divvy_Trips_2020_Q1.csv")


# Rename columns in sheet1 to match sheet2
sheet1 = sheet1.rename(columns={
    'trip_id': 'ride_id',
    'start_time': 'started_at',
    'end_time': 'ended_at',
    'from_station_name': 'start_station_name',
    'from_station_id': 'start_station_id',
    'to_station_name': 'end_station_name',
    'to_station_id': 'end_station_id',
    'usertype': 'member_casual',
    'WEEKDAY': 'day_of_week'
})

# Optional: Drop or fill missing columns to align both
sheet1['rideable_type'] = 'unknown'
sheet1['start_lat'] = None
sheet1['start_lng'] = None
sheet1['end_lat'] = None
sheet1['end_lng'] = None

# Make sure columns match
common_columns = list(set(sheet1.columns).intersection(set(sheet2.columns)))
sheet1 = sheet1[common_columns]
sheet2 = sheet2[common_columns]

# Combine
full_data = pd.concat([sheet1, sheet2], ignore_index=True)

# Save merged data
full_data.to_csv("202X_full_year_data.csv", index=False)
