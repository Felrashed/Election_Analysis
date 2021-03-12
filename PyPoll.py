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

#Initialize a total vote counter
total_votes = 0

#candidate options and candidate votes
#delcare a new list
candidate_options = []
#declare empty dictionary
candidate_votes = {}

#Track Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        
        #Add to the total vote count
        total_votes += 1
        
        #get the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate add it to the list
        if candidate_name not in candidate_options:
            # add it to the list of candidates
            candidate_options.append(candidate_name)
            
            #begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0
 
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
    #determine the percentage of votes for each candidate by looping through the counts
    # iterate through the candidate list 
for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #calculate the percentage of cotes
    vote_percentage = float(votes) / float(total_votes) * 100
    #print the candidate name and percentage of votes
    print(f"{candidate_name} :  {vote_percentage:.1f} ({votes:,})\n") 

    #Determine winning vote count and candidate
    #determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        #if true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
            
        winning_percentage = vote_percentage
            
        #set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

#print the winning candidates' results to the terminal
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)


#To do: print out the winning candidate, vote count and percentage to terminal
#votes to the terminal.
#print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


#print the candidate vote dictionary
#print(candidate_votes)

#Print the candidate list.
#print(candidate_options)

#3. Print the total votes
#print(total_votes)


   



#Using the open() function with the "w" mode we will write the data to the file
outfile = open(file_to_save, "w")
#write some data to the file.
outfile.write("Counties in the Election\n")
outfile.write("-------------------------\n")
outfile.write("Arapahoe\nDenver\nJefferson")

#Close the file
outfile.close()
