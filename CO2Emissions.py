# ---------------------------------------------------------------------------------------------
# Questions:
# 1. What were the top 5 countries in the set that produced the most CO2 from 1960-2019?
# 1A: In order, The United States, China, Russia, the Middle East & North Africa, and India were
#     the top producers of CO2; this makes sense given their size, population and economic power 
#
# 2. Which country in the top 5 had the greatest increase %-wise in carbon emissions from 2009-2019?
# 2A: India had the greatest overall increase within the decade, while the US had the lowest increase.
#     This is very insteresting and could be looked into further
#
# 3. 
#
# ---------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np

dataFrame = pd.read_csv("co2_emissions_kt_by_country.csv", usecols=[
                        "country_name", "year", "value"])
# print(dataFrame.head(25))
# print(dataFrame.sort_values("value").tail(10))
without_world = dataFrame[
    (dataFrame.country_name != "World")
    & (dataFrame.country_name != "East Asia & Pacific (excluding high income)")
    & (dataFrame.country_name != "IDA & IBRD total")
    & (dataFrame.country_name != "IBRD only")
    & (dataFrame.country_name != "Middle income")
    & (dataFrame.country_name != "Low & middle income")
    & (dataFrame.country_name != "High income")
    & (dataFrame.country_name != "Latin America & Caribbean (excluding high income)")
    & (dataFrame.country_name != "Low income")
    & (dataFrame.country_name != "Lower middle income")
    & (dataFrame.country_name != "Middle East & North Africa (excluding high income)")
    & (dataFrame.country_name != "Sub-Saharan Africa (excluding high income)")
    & (dataFrame.country_name != "Europe & Central Asia (IDA & IBRD countries)")
    & (dataFrame.country_name != "Latin America & the Caribbean (IDA & IBRD countries)")
    & (dataFrame.country_name != "Middle East & North Africa (IDA & IBRD countries)")
    & (dataFrame.country_name != "South Asia (IDA & IBRD)")
    & (dataFrame.country_name != "Sub-Saharan Africa (IDA & IBRD countries)")
    & (dataFrame.country_name != "Upper middle income")
    & (dataFrame.country_name != "Late-demographic dividend")
    & (dataFrame.country_name != "East Asia & Pacific")
    & (dataFrame.country_name != "OECD members")
    & (dataFrame.country_name != "Post-demographic dividend")
    & (dataFrame.country_name != "East Asia & Pacific (IDA & IBRD countries)")
    & (dataFrame.country_name != "Europe & Central Asia")
    & (dataFrame.country_name != "Early-demographic dividend")
    & (dataFrame.country_name != "Europe & Central Asia (excluding high income)")
    & (dataFrame.country_name != "North America")
    & (dataFrame.country_name != "European Union")
    & (dataFrame.country_name != "Euro area")
    & (dataFrame.country_name != "South Asia")
    & (dataFrame.country_name != "China") # Remove to see top 60
    & (dataFrame.country_name != "United States") # Remove to see top 120
    & (dataFrame.country_name != "Russian Federation")
    & (dataFrame.country_name != "Middle East & North Africa")
    & (dataFrame.country_name != "India")
    # and dataFrame.country_name != ""
    # and dataFrame.country_name != ""
    # and dataFrame.country_name != ""
]
print(without_world.sort_values("value", ascending=False).head(30))

# without_world.plot()

top5 = []

only_china = dataFrame[dataFrame.country_name == "China"]
china_sum = only_china["value"].sum()
top5.append(float(china_sum))
print(f"Sum of China's Emissions from 1960-2019: {china_sum}")

only_us = dataFrame[dataFrame.country_name == "United States"]
us_sum = only_us["value"].sum()
top5.append(float(us_sum))
print(f"Sum of the United State's Emissions from 1960-2019: {us_sum}")

only_rus = dataFrame[dataFrame.country_name == "Russian Federation"]
rus_sum = only_rus["value"].sum()
top5.append(float(rus_sum))
print(f"Sum of Russia's Emissions from 1960-2019: {rus_sum}")

only_middle_east = dataFrame[dataFrame.country_name == "Middle East & North Africa"]
middle_east_sum = only_middle_east["value"].sum()
top5.append(float(middle_east_sum))
print(f"Sum of the Middle East and North Africa's Emissions from 1960-2019: {middle_east_sum}")

only_india = dataFrame[dataFrame.country_name == "India"]
india_sum = only_india["value"].sum()
top5.append(float(india_sum))
print(f"Sum of India's Emissions from 1960-2019: {india_sum}")

china_percent = dataFrame[(dataFrame.country_name == "China") & (dataFrame.year >= 2009) & (dataFrame.year <= 2019)]
# print(china_percent.sort_values("value", ascending=False).head(10))
print()
print("China Percentages:")
print(china_percent["value"].pct_change())
# sum = 0.338301

# print(only_china.pct_change())
US_percent = dataFrame[(dataFrame.country_name == "United States") & (dataFrame.year >= 2009) & (dataFrame.year <= 2019)]
# print(china_percent.sort_values("value", ascending=False).head(10))
print()
print("US Percentages:")
print(US_percent["value"].pct_change())
# sum = -0.063206


Russia_percent = dataFrame[(dataFrame.country_name == "Russian Federation") & (dataFrame.year >= 2009) & (dataFrame.year <= 2019)]
# print(china_percent.sort_values("value", ascending=False).head(10))
print()
print("Russia Percentages:")
print(Russia_percent["value"].pct_change())
# sum = 0.100829

MEast_percent = dataFrame[(dataFrame.country_name == "Middle East & North Africa") & (dataFrame.year >= 2009) & (dataFrame.year <= 2019)]
# print(china_percent.sort_values("value", ascending=False).head(10))
print()
print("Middle East Percentages:")
print(MEast_percent["value"].pct_change())
# sum = 0.231168

India_percent = dataFrame[(dataFrame.country_name == "India") & (dataFrame.year >= 2009) & (dataFrame.year <= 2019)]
# print(china_percent.sort_values("value", ascending=False).head(10))
print()
print("India Percentages:")
print(India_percent["value"].pct_change())
# sum = 0.465342

china_percent.plot(title="China's Emission Percentage, 2009-2019", x="year")
US_percent.plot(title="United States's Emission Percentage, 2009-2019", x="year")
Russia_percent.plot(title="Russia's Emission Percentage, 2009-2019", x="year")
MEast_percent.plot(title="Middle East's Emission Percentage, 2009-2019", x="year")
India_percent.plot(title="India's Emission Percentage, 2009-2019", x="year")