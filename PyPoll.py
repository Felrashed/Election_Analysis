#The data we need to retreive:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of cotes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file.
### with open(file_to_load) as election_data:

    # To do: Perform Analysis
 ###   print(election_data)

#add our dependencies
import csv
import os
#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To Do: read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    print(headers)

   



#Using the open() function with the "w" mode we will write the data to the file
outfile = open(file_to_save, "w")
#write some data to the file.
outfile.write("Counties in the Election\n")
outfile.write("-------------------------\n")
outfile.write("Arapahoe\nDenver\nJefferson")

#Close the file
outfile.close()
