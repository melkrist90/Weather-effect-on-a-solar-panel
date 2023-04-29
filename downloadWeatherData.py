from weatherDataFunctions import mergeWithWeatherData

blindern = 'SN18700' # Weather station ID

# One function call for each month (remember to remove or specify the folder names)
# 1. quarter
mergeWithWeatherData("productionData\\01january2020-production.csv", "weatherData\\01january2020-weather.csv", blindern)
mergeWithWeatherData("productionData\\02february2020-production.csv", "weatherData\\02february2020-weather.csv", blindern)
mergeWithWeatherData("productionData\\03march2020-production.csv", "weatherData\\03march2020-weather.csv", blindern)

# 2. quarter
mergeWithWeatherData("productionData\\04april2020-production.csv", "weatherData\\04april2020-weather.csv", blindern)
mergeWithWeatherData("productionData\\05may2020-production.csv", "weatherData\\05may2020-weather.csv", blindern)
mergeWithWeatherData("productionData\\06june2020-production.csv", "weatherData\\06june2020-weather.csv", blindern)

# 3. quarter
mergeWithWeatherData("productionData\\07july2020-production.csv", "weatherData\\07july2020-weather.csv", blindern)
mergeWithWeatherData("productionData\\08august2020-production.csv", "weatherData\\08august2020-weather.csv", blindern)
mergeWithWeatherData("productionData\\09september2020-production.csv", "weatherData\\09september2020-weather.csv", blindern)

# 4. quarter
mergeWithWeatherData("productionData\\10october2020-production.csv", "weatherData\\10october2020-weather.csv", blindern)
mergeWithWeatherData("productionData\\11november2020-production.csv", "weatherData\\11november2020-weather.csv", blindern)
mergeWithWeatherData("productionData\\12december2020-production.csv", "weatherData\\12december2020-weather.csv", blindern)
