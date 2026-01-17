# ================================
# Weather Data Analysis – May(from 14)
# ================================
# This script performs exploratory data analysis on
# hourly weather data for the month of May.
# Focus areas:
# - Hourly temperature variation
# - Day vs night temperature comparison
# - Daily average temperature
# - Weather condition frequency
# - Humidity trends in summer
# ================================

# -------- Import required libraries --------
import pandas as pd
import matplotlib.pyplot as plt

# -------- Step 1: Load the dataset with error handling --------
try:
    df = pd.read_csv(
        r'C:\Users\ssand\Desktop\datascience\Tasks\task 4\Book1.csv'
    )
    print("Dataset loaded successfully")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

# -------- Step 2: Basic dataset inspection --------
print("\nDataset Information:")
print(df.info())

# -------- Step 3: Convert date/time column to datetime --------
df["date/time"] = pd.to_datetime(df["date/time"])

# -------- Step 4: Check for missing values and duplicates --------
print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:", df.duplicated().sum())

# -------- Step 5: Extract useful time-based features --------
df["hour"] = df["date/time"].dt.hour
df["day"] = df["date/time"].dt.date

# -------- Step 6: Basic statistical analysis --------
avg_temp = df["temp_c"].mean()
max_temp = df["temp_c"].max()
min_temp = df["temp_c"].min()
avg_humidity = df["rel_hum%"].mean()

print("\nBasic Analysis Results:")
print("Average temperature in May:", round(avg_temp, 2), "°C")
print("Maximum temperature in May:", max_temp, "°C")
print("Minimum temperature in May:", min_temp, "°C")
print("Average relative humidity in May:", round(avg_humidity, 2), "%")

# =========================================================
# VISUALIZATION SECTION
# =========================================================

# -------- Graph 1: Hourly Temperature Variation --------
hourly_avg_temp = df.groupby("hour")["temp_c"].mean()

plt.figure()
plt.plot(hourly_avg_temp)
plt.xlabel("Hour of the Day")
plt.ylabel("Average Temperature (°C)")
plt.title("Hourly Temperature Variation in May")
plt.show()

# -------- Graph 2: Day vs Night Temperature Comparison --------
# Day: 6 AM – 6 PM, Night: remaining hours
df["day_night"] = df["hour"].apply(
    lambda x: "Day" if 6 <= x < 18 else "Night"
)

day_night_temp = df.groupby("day_night")["temp_c"].mean()

plt.figure()
plt.bar(day_night_temp.index, day_night_temp.values)
plt.xlabel("Time Period")
plt.ylabel("Average Temperature (°C)")
plt.title("Day vs Night Temperature in May")
plt.show()

# -------- Graph 3: Daily Average Temperature --------
daily_avg_temp = df.groupby("day")["temp_c"].mean()

plt.figure()
plt.plot(daily_avg_temp)
plt.xlabel("Day")
plt.ylabel("Average Temperature (°C)")
plt.title("Daily Average Temperature in May")
plt.show()

# -------- Graph 4: Weather Condition Frequency --------
weather_counts = df["weather"].value_counts()

plt.figure()
plt.bar(weather_counts.index, weather_counts.values)
plt.xlabel("Weather Condition")
plt.ylabel("Frequency")
plt.title("Weather Condition Frequency in May")
plt.xticks(rotation=45)
plt.show()

# -------- Graph 5: Humidity Trend in Summer --------
daily_avg_humidity = df.groupby("day")["rel_hum%"].mean()

plt.figure()
plt.plot(daily_avg_humidity)
plt.xlabel("Day")
plt.ylabel("Average Relative Humidity (%)")
plt.title("Daily Average Humidity Trend in May")
plt.show()

# -------- End of Script --------
print("\nWeather data analysis for May completed successfully.")
