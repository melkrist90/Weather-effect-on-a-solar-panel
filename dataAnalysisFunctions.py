import pandas as pd
import csv
import sys

# Global variables for quarterly or yearly results
global_days = 0

global_sum_prod, global_sum_temp, global_sum_sun, global_sum_prec = None, None, None, None
global_avr_prod, global_avr_temp, global_avr_sun, global_avr_prec = None, None, None, None

global_max_prod = {"title": "max production", "date": None, "production": sys.float_info.min, "temperature": None, "sun hours": None, "precipitation": None}
global_min_prod = {"title": "min production", "date": None, "production": sys.float_info.max, "temperature": None, "sun hours": None, "precipitation": None}

global_max_temp = {"title": "max temperature", "date": None, "production": None, "temperature": sys.float_info.min, "sun hours": None, "precipitation": None}
global_min_temp = {"title": "min temperature","date": None, "production": None, "temperature": sys.float_info.max, "sun hours": None, "precipitation": None}

global_max_sun = {"title": "max sun hours", "date": None, "production": None, "temperature": None, "sun hours": sys.float_info.min, "precipitation": None}
global_min_sun = {"title": "min sun hours", "date": None, "production": None, "temperature": None, "sun hours": sys.float_info.max, "precipitation": None}

global_max_prec = {"title": "max precipitation", "date": None, "production": None, "temperature": None, "sun hours": None, "precipitation": sys.float_info.min}
global_min_prec = {"title": "min precipitation", "date": None, "production": None, "temperature": None, "sun hours": None, "precipitation": sys.float_info.max}

global_max_min_list = [global_max_prod, global_min_prod, global_max_temp, global_min_temp, global_max_sun, global_min_sun, global_max_prec, global_min_prec]

global_max_list = [global_max_prod, global_max_temp, global_max_sun,  global_max_prec]
global_min_list = [global_min_prod, global_min_temp, global_min_sun, global_min_prec]



# Analyze each file
def analyzeFile(input_filename, output_filename, month):
    print("***", month, "***")

    with open(input_filename) as ifile:
        reader = csv.reader(ifile, delimiter=';')

        # Local variables (spelled out)
        # Highest/lowest
        max_prod = {"title": "max production", "date": None, "production": sys.float_info.min, "temperature": None, "sun hours": None, "precipitation": None}
        min_prod = {"title": "min production", "date": None, "production": sys.float_info.max, "temperature": None, "sun hours": None, "precipitation": None}

        max_temp = {"title": "max temperature", "date": None, "production": None, "temperature": sys.float_info.min, "sun hours": None, "precipitation": None}
        min_temp = {"title": "min temperature","date": None, "production": None, "temperature": sys.float_info.max, "sun hours": None, "precipitation": None}

        max_sun = {"title": "max sun hours", "date": None, "production": None, "temperature": None, "sun hours": sys.float_info.min, "precipitation": None}
        min_sun = {"title": "min sun hours", "date": None, "production": None, "temperature": None, "sun hours": sys.float_info.max, "precipitation": None}

        max_prec = {"title": "max precipitation", "date": None, "production": None, "temperature": None, "sun hours": None, "precipitation": sys.float_info.min}
        min_prec = {"title": "min precipitation", "date": None, "production": None, "temperature": None, "sun hours": None, "precipitation": sys.float_info.max}

        # Sums
        days = -1 # In case the file has skipped a day
        sum_prod, sum_temp, sum_sun, sum_prec = None, None, None, None

        # Iterating the lines of the file
        for row in reader:

            if days > -1: # Control: Passed the header

                # Extracting data from each line
                try:
                    time, temp, sun, prec = row[0], float(row[2]), float(row[3]), float(row[4])

                    if row[1] != " ":
                        kWh = float(row[1])
                    else:
                        kWh = 0.0

                except:
                    print("Error: Could not find", row)
                    print("Please check source file", input_filename)

                # Local sum
                if days > 0: # Control: Assigne av value to the local sum variables
                    sum_prod += kWh
                    sum_temp += temp
                    sum_sun += sun
                    sum_prec += prec

                else:
                    sum_prod, sum_temp, sum_sun, sum_prec = kWh, temp, sun, prec

                days += 1

                # Beneath the thoughts behind the local variables are spelled out
                # Highest/lowest production
                if kWh > max_prod.get("production"):
                    max_prod.update({"date": time, "production": kWh, "temperature": temp, "sun hours": sun, "precipitation": prec})

                if kWh < min_prod.get("production"):
                    min_prod.update({"date": time, "production": kWh, "temperature": temp, "sun hours": sun, "precipitation": prec})

                # Highest/lowest temperature
                if temp > max_temp.get("temperature"):
                    max_temp.update({"date": time, "production": kWh, "temperature": temp, "sun hours": sun, "precipitation": prec})

                if temp < min_temp.get("temperature"):
                    min_temp.update({"date": time, "production": kWh, "temperature": temp, "sun hours": sun, "precipitation": prec})

                # Highest/lowest number of sun hours
                if sun > max_sun.get("sun hours"):
                    max_sun.update({"date": time, "production": kWh, "temperature": temp, "sun hours": sun, "precipitation": prec})

                if sun < min_sun.get("sun hours"):
                    min_sun.update({"date": time, "production": kWh, "temperature": temp, "sun hours": sun, "precipitation": prec})

                # Highest/lowest precipitation
                if prec > max_prec.get("precipitation"):
                    max_prec.update({"date": time, "production": kWh, "temperature": temp, "sun hours": sun, "precipitation": prec})

                if prec < min_prec.get("precipitation"):
                    min_prec.update({"date": time, "production": kWh, "temperature": temp, "sun hours": sun, "precipitation": prec})

            else:
                days += 1

        global global_days, global_sum_prod, global_sum_temp, global_sum_sun, global_sum_prec

        # Update global sum varibles
        if global_days > 0:
            global_sum_prod += sum_prod
            global_sum_temp += sum_temp
            global_sum_sun += sum_sun
            global_sum_prec += sum_prec
        else:
            global_sum_prod, global_sum_temp, global_sum_sun, global_sum_prec = sum_prod, sum_temp, sum_sun, sum_prec

        global_days += days


        # Results
        max_min_list = [max_prod, min_prod, max_temp, min_temp, max_sun, min_sun, max_prec, min_prec]
        sum_prod, sum_temp, sum_sun, sum_prec = round(sum_prod, 3), round(sum_temp, 3), round(sum_sun, 3), round(sum_prec, 3)
        avr_prod, avr_temp, avr_sun, avr_prec = round(sum_prod/days, 3), round(sum_temp/days, 3), round(sum_sun/days, 3), round(sum_prec/days, 3)

        print("")

        # Printing sums
        print("SUM")
        print("Total production (kWh):", sum_prod)
        print("Total sun hours:", sum_sun)
        print("Total precipitation (mm):", sum_prec)
        print("\n")

        # Printing averages
        print("AVERAGE PER DAY")
        print("Average production (kWh):", avr_prod)
        print("Average temperature (C):", avr_temp)
        print("Average sun hours:", avr_sun)
        print("Average precipitation (mm):", avr_prec)
        print("\n")


        # Printing highest/lowest results
        print("HIGHEST AND LOWEST RESULTS")
        c = [] # Coloumns
        i = [] # Index (row)
        counter = 1; # Row counter

        for result in max_min_list:
            c.append([result["title"], result["date"], result["production"], result["temperature"], result["sun hours"], result["precipitation"]])
            i.append(str(counter))
            counter += 1

        local_max_min_table = pd.DataFrame(c, columns = ['type', '         date', '   production (kWh)', '   temperature (C)', '   sun hours', '   precipitation (mm)'], index=[i])
        print(local_max_min_table)
        print("\n")

        # Printing highest/lowest production relative to highest/lowest temperature, sun hours and precipitation
        print("MATCHING RESULTS")
        match = False

        for dict in max_min_list[2:]:
            if dict["date"] == max_prod["date"]:
                print(dict["date"] + ":", max_prod["title"], "(", max_prod["production"], ") and", dict["title"], "(", dict[dict["title"].removeprefix(dict["title"][0:4])], ")")
                match = True

            if dict["date"] == min_prod["date"]:
                print(dict["date"] + ":", min_prod["title"], "(", min_prod["production"], ") and", dict["title"], "(", dict[dict["title"].removeprefix(dict["title"][0:4])], ")")
                match = True

        if match == False:
            print("None")

        print("")

        # Writing to file and updating global dictionaries while iterating
        with open(output_filename, "x", newline='') as ofile:
            writer = csv.writer(ofile, delimiter=';', dialect='excel', doublequote=False)

            # Writing sums
            writer.writerow(["Sum production (kWh)", "Sum sun hours", "Sum precipitation (mm)"])
            writer.writerow([sum_prod, sum_sun, sum_prec])
            writer.writerow("")


            # Writing averages
            writer.writerow(["Average production (kWh)", "Average temperature (Celsius)", "Average sun hours", "Average precipitation (mm)"])
            writer.writerow([avr_prod, avr_temp, avr_sun, avr_prec])
            writer.writerow("")

            # Writing highest/lowest results at the beginning of each iteration
            writer.writerow(["Type", "Time", "Production (kWh)", "Temperature (Celsius)", "Sun hours", "Precipitation (mm)"])

            for local_element in max_min_list:
                writer.writerow([local_element["title"], local_element["date"], local_element["production"], local_element["temperature"], local_element["sun hours"], local_element["precipitation"]])

                # Updating global dictionaries (this time with a complicated, but fun and potentially more generic, alternative to the if-else sentences)
                key = local_element["title"].removeprefix(local_element["title"][0:4])

                if "max" in local_element["title"]:
                    for global_element in global_max_list:
                        if key == global_element["title"].removeprefix(global_element["title"][0:4]): # Removes "max"
                            if local_element[key] > global_element[key]:
                                global_element.update({"date": local_element["date"], "production": local_element["production"], "temperature": local_element["temperature"], "sun hours": local_element["sun hours"], "precipitation": local_element["precipitation"]})
                else:
                    for global_element in global_min_list:
                        if key == global_element["title"].removeprefix(global_element["title"][0:4]): # Removes "min"
                            if local_element[key] < global_element[key]:
                                global_element.update({"date": local_element["date"], "production": local_element["production"], "temperature": local_element["temperature"], "sun hours": local_element["sun hours"], "precipitation": local_element["precipitation"]})


        print("")

        # Printing updtated global dictionaries
        print("UPDATED OVERALL STATS")
        global_c = [] # Coloumns
        global_i = [] # Index (row)
        global_counter = 1; # Row counter

        for instance in global_max_min_list:
            global_c.append([instance["title"], instance["date"], instance["production"], instance["temperature"], instance["sun hours"], instance["precipitation"]])
            global_i.append(str(global_counter))
            global_counter += 1

        global_max_min_table = pd.DataFrame(global_c, columns = ['type', '         date', '   production (kWh)', '   temperature (C)', '   sun hours', '   precipitation (mm)'], index=[global_i])
        print(global_max_min_table)

        print("\n" + "\n")

# Writing the global stats to file
def saveGlobalStats(output_filename):
    global global_sum_prod, global_sum_temp, global_sum_sun, global_sum_prec
    global global_avr_prod, global_avr_temp, global_avr_sun, global_avr_prec

    # Calculate averages with three decimals
    global_avr_prod, global_avr_temp, global_avr_sun, global_avr_prec = round(global_sum_prod/global_days, 3), round(global_sum_temp/global_days, 3), round(global_sum_sun/global_days, 3), round(global_sum_prec/global_days, 3)

    # Round sums to three decimals
    global_sum_prod, global_sum_temp, global_sum_sun, global_sum_prec = round(global_sum_prod, 3), round(global_sum_temp, 3), round(global_sum_sun, 3), round(global_sum_prec, 3)

    # Write to file
    with open(output_filename, "x", newline='') as ofile:
        writer = csv.writer(ofile, delimiter=';', dialect='excel', doublequote=False)

        print("*** OVERALL STATS ***")
        print("")

        # Writing sums
        writer.writerow(["Sum production (kWh)", "Sum sun hours", "Sum precipitation (mm)"])
        writer.writerow([global_sum_prod, global_sum_sun, global_sum_prec])
        writer.writerow("")

        # Printing sums
        print("SUM")
        print("Total production (kWh):", global_sum_prod)
        print("Total sun hours:", global_sum_sun)
        print("Total precipitation (mm):", global_sum_prec)
        print("\n")


        # Writing averages
        writer.writerow(["Average production (kWh)", "Average temperature (Celsius)", "Average sun hours", "Average precipitation (mm)"])
        writer.writerow([global_avr_prod, global_avr_temp, global_avr_sun, global_avr_prec])
        writer.writerow("")

        # Printing averages
        print("AVERAGE PER DAY")
        print("Average production (kWh):", global_avr_prod)
        print("Average temperature (C):", global_avr_temp)
        print("Average sun hours:", global_avr_sun)
        print("Average precipitation (mm):", global_avr_prec)
        print("\n")

        # Writing and printing highest/lowest results
        print("HIGHEST AND LOWEST RESULTS")
        c = [] # Coloumns
        i = [] # Index (row)
        counter = 1; # Row counter

        for global_element in global_max_min_list:
            writer.writerow([global_element["title"], global_element["date"], global_element["production"], global_element["temperature"], global_element["sun hours"], global_element["precipitation"]])
            c.append([global_element["title"], global_element["date"], global_element["production"], global_element["temperature"], global_element["sun hours"], global_element["precipitation"]])
            i.append(str(counter))
            counter += 1

        global_max_min_table = pd.DataFrame(c, columns = ['type', '         date', '   production (kWh)', '   temperature (C)', '   sun hours', '   precipitation (mm)'], index=[i])
        print(global_max_min_table)
        print("\n")

        # Printing highest/lowest production relative to highest/lowest temperature, sun hours and precipitation
        print("MATCHING RESULTS")
        match = False

        for dict in global_max_min_list[2:]:
            if dict["date"] == global_max_prod["date"]:
                print(dict["date"] + ":", global_max_prod["title"], "(", global_max_prod["production"], ") and", dict["title"], "(", dict[dict["title"].removeprefix(dict["title"][0:4])], ")")
                match = True

            if dict["date"] == global_min_prod["date"]:
                print(dict["date"] + ":", global_min_prod["title"], "(", global_min_prod["production"], ") and", dict["title"], "(", dict[dict["title"].removeprefix(dict["title"][0:4])], ")")
                match = True

        if match == False:
            print("None")
