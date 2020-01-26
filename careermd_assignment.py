# import neccessary libraries
import requests # to send a get request
import xmltodict # to parse the XML input to convert to dictionary 
import json # to output as json format

# download XML file from the feed
url = "https://www.crosscountrysearch.com/careermd" # assign object for the url
response=requests.get(url) # call server to get the url
with open("careermd.xml", "wb") as file: # create the file and get all the contents of the request
    file.write(response.content)

# convert to JSON file
with open('careermd.xml', 'r') as f: # read careermd.xml file in local
    xmlstring=f.read() # assign the string into an object
jsonstring=json.dumps(xmltodict.parse(xmlstring), indent=4) # parse the xml with xmltodict and format as json
with open("careermd.json", "w") as f: # write careermd.json file to local
    f.write(jsonstring)


# I also wanted to explore converting the feed to a dataframe in order to transform and see statistical summary.

# read careermd.xml and parse to dictionary
with open("careermd.xml") as fd: # read and parse to dictionary (so do not format yet)
    careermddict=xmltodict.parse(fd.read())
careermddict.keys()

# look at values in key JOBS
careermddict["JOBS"].values()

# as we see the nested dictionary, access and create a new dictionary for converting to dataframe
careermddata=careermddict["JOBS"]["JOB"]

# normalize and convert to dataframe
import pandas as pd
from pandas.io.json import json_normalize # import json_normalize for converting to dataframe
df=json_normalize(careermddata) # normalize and create a dataframe as df
df.head() # look at the first five observation

# look at missing values
df.isnull().sum()

# Look at data types
df.dtypes

# summary of the dataframe
df.info()

# value counts of j1_visa status (which has missing values)
df["j1_visa_status"].value_counts()

# statistical summary
df.describe()




