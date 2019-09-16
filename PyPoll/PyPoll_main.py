# %%
#connect to modules
import os
import csv

#build variables
candidates = []
num_votes = 0
vote_counts = [] 
election_data = ['1']

#loop
for files in election_data:
#open data file
    election_dataCSV = os.path.join('election_data.csv')
    with open(election_dataCSV) as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        line = next(csvReader,None)

        for line in csvReader:

#vote totals
            num_votes = num_votes + 1
            candidate = line[2]
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1
            else:
                candidates.append(candidate)
                vote_counts.append(1)

#calculation variables
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

#vote %
    for count in range(len(candidates)):
        vote_percentage = (vote_counts[count]/num_votes*100)
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]

    percentages = [round(i,2) for i in percentages]

#terminal results
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {num_votes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]:.3f}% ({vote_counts[count]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")

#file results
    output_file = election_dataCSV[0:-4]
    write_election_dataCSV = f"pypoll_results.txt"
    filewriter = open(write_election_dataCSV, mode = 'w')
    filewriter.write("Election Results\n")
    filewriter.write("--------------------------\n")
    filewriter.write(f"Total Votes: {num_votes}\n")
    for count in range(len(candidates)):
        filewriter.write(f"{candidates[count]}: {percentages[count]:.3f}% ({vote_counts[count]})\n")
    filewriter.write("---------------------------\n")
    filewriter.write(f"Winner: {winner}\n")
    filewriter.write("---------------------------\n")
    filewriter.close()

# %%
