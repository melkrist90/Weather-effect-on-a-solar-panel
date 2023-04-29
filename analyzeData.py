from dataAnalysisFunctions import analyzeFile, saveGlobalStats

# One function call for each month (remember to remove or specify the folder names)
# 1. quarter
analyzeFile("weatherData\\01january2020-weather.csv", "stats\\01january2020-stats.csv", "JANUARY")
analyzeFile("weatherData\\02february2020-weather.csv", "stats\\02february2020-stats.csv", "FEBRUARY")
analyzeFile("weatherData\\03march2020-weather.csv", "stats\\03march2020-stats.csv", "MARCH")

# 2. quarter
analyzeFile("weatherData\\04april2020-weather.csv", "stats\\04april2020-stats.csv", "APRIL")
analyzeFile("weatherData\\05may2020-weather.csv", "stats\\05may2020-stats.csv", "MAY")
analyzeFile("weatherData\\06june2020-weather.csv", "stats\\06june2020-stats.csv", "JUNE")

# 3. quarter
analyzeFile("weatherData\\07july2020-weather.csv", "stats\\07july2020-stats.csv", "JULY")
analyzeFile("weatherData\\08august2020-weather.csv", "stats\\08august2020-stats.csv", "AUGUST")
analyzeFile("weatherData\\09september2020-weather.csv", "stats\\09september2020-stats.csv", "SEPTEMBER")

# 4. quarter
analyzeFile("weatherData\\10october2020-weather.csv", "stats\\10october2020-stats.csv", "OCTOBER")
analyzeFile("weatherData\\11november2020-weather.csv", "stats\\11november2020-stats.csv", "NOVEMBER")
analyzeFile("weatherData\\12december2020-weather.csv", "stats\\12december2020-stats.csv", "DECEMBER")

# Yearly stats
saveGlobalStats("stats\\year2020-stats.csv")
