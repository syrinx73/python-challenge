{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "--------------------------\n",
      "Total Votes: 3521001\n",
      "Khan: 63.000% (2218231)\n",
      "Correy: 20.000% (704200)\n",
      "Li: 14.000% (492940)\n",
      "O'Tooley: 3.000% (105630)\n",
      "---------------------------\n",
      "Winner: Khan\n",
      "---------------------------\n"
     ]
    }
   ],
   "source": [
    "#connect to modules\n",
    "import os\n",
    "import csv\n",
    "\n",
    "#build variables\n",
    "candidates = []\n",
    "num_votes = 0\n",
    "vote_counts = [] \n",
    "election_data = ['1']\n",
    "\n",
    "#loop\n",
    "for files in election_data:\n",
    "#open data file\n",
    "    election_dataCSV = os.path.join('election_data.csv')\n",
    "    with open(election_dataCSV) as csvFile:\n",
    "\n",
    "        csvReader = csv.reader(csvFile, delimiter=',')\n",
    "\n",
    "        line = next(csvReader,None)\n",
    "\n",
    "        for line in csvReader:\n",
    "\n",
    "#vote totals\n",
    "            num_votes = num_votes + 1\n",
    "            candidate = line[2]\n",
    "            if candidate in candidates:\n",
    "                candidate_index = candidates.index(candidate)\n",
    "                vote_counts[candidate_index] = vote_counts[candidate_index] + 1\n",
    "            else:\n",
    "                candidates.append(candidate)\n",
    "                vote_counts.append(1)\n",
    "\n",
    "#calculation variables\n",
    "    percentages = []\n",
    "    max_votes = vote_counts[0]\n",
    "    max_index = 0\n",
    "\n",
    "#vote %\n",
    "    for count in range(len(candidates)):\n",
    "        vote_percentage = (vote_counts[count]/num_votes*100)\n",
    "        percentages.append(vote_percentage)\n",
    "        if vote_counts[count] > max_votes:\n",
    "            max_votes = vote_counts[count]\n",
    "            print(max_votes)\n",
    "            max_index = count\n",
    "    winner = candidates[max_index]\n",
    "\n",
    "    percentages = [round(i,2) for i in percentages]\n",
    "\n",
    "#terminal results\n",
    "    print(\"Election Results\")\n",
    "    print(\"--------------------------\")\n",
    "    print(f\"Total Votes: {num_votes}\")\n",
    "    for count in range(len(candidates)):\n",
    "        print(f\"{candidates[count]}: {percentages[count]:.3f}% ({vote_counts[count]})\")\n",
    "    print(\"---------------------------\")\n",
    "    print(f\"Winner: {winner}\")\n",
    "    print(\"---------------------------\")\n",
    "\n",
    "#file results\n",
    "    output_file = election_dataCSV[0:-4]\n",
    "    write_election_dataCSV = f\"pypoll_results.txt\"\n",
    "    filewriter = open(write_election_dataCSV, mode = 'w')\n",
    "    filewriter.write(\"Election Results\\n\")\n",
    "    filewriter.write(\"--------------------------\\n\")\n",
    "    filewriter.write(f\"Total Votes: {num_votes}\\n\")\n",
    "    for count in range(len(candidates)):\n",
    "        filewriter.write(f\"{candidates[count]}: {percentages[count]:.3f}% ({vote_counts[count]})\\n\")\n",
    "    filewriter.write(\"---------------------------\\n\")\n",
    "    filewriter.write(f\"Winner: {winner}\\n\")\n",
    "    filewriter.write(\"---------------------------\\n\")\n",
    "    filewriter.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
