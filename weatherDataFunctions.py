import csv
import requests
import pandas as pd
import json

# Collect observations of mean temperature, sun hours and precipitation on a particular date
def tempSunAndRain(date, station):
    client_id = '' # Create a user at frost.met.no/howto.html

    # Endpoint
    endpoint = 'https://frost.met.no/observations/v0.jsonld' # Norwegian Meteorological Institute

    # Search parameters (mean temperature, sun hours and precipitation)
    parameters = {
        'sources': station,
        'elements': 'mean(air_temperature P1D), sum(duration_of_sunshine P1D), sum(precipitation_amount P1D)',
        'referencetime': date,
        }

    # HTTP GET request
    result = requests.get(endpoint, parameters, auth=(client_id,''))

    # Result in JSON
    json = result.json()

    # Extract values (of highest quality)
    temp = json["data"][0]["observations"][0]["value"] # Mean temperature
    sun = json["data"][0]["observations"][2]["value"] # Sun hours
    prec = json["data"][0]["observations"][4]["value"] # Precipitation

    # Confirming that the request was successful by printing the result to the terminal
    print(date, temp, sun, prec)

    return [temp, sun, prec]


# Writing date and production data to the output file along with results from the calling of the above tempSunAndRain function
def mergeWithWeatherData(input_filename, output_filename, nearest_station):

    # Creating and opening the output file
    with open(output_filename, "x", newline='') as ofile:
        writer = csv.writer(ofile, delimiter=';', dialect='excel', doublequote=False)

        # Opening the input file containing the production data
        with open(input_filename, "r", newline='') as ifile:
            reader = csv.reader(ifile, delimiter=';')
            line = 1

            # Interating thorugh the lines of the inpurt file
            for row in reader:
                if line > 1: # Control: Passed the header
                    try:
                        # The strings from the first and third column in the input file is added to the output
                        date = row[0]
                        kWh = row[2]
                        output = [date, kWh]

                        # The date from the input file is used to call the above tempSunAndRain function
                        observations = tempSunAndRain(date, nearest_station)

                        # Results of the call is added to the output
                        for element in observations:
                            output.append(element)

                        # Writing the line to the output file
                        writer.writerow(output)

                    except:
                        print("Error: Could not find", row)
                        print("Please check source file", input_filename)

                else:
                    # Adding a suitable header to the first line of the output file
                    header_row = ['Time', 'kWh', 'Temperature (Celsius)', 'Sun hours', 'Precipitation (mm)']
                    writer.writerow(header_row)
                    line += 1
