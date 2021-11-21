# Election Analysis
- Seth and Tom were audited on the results of the election. Instead of counting them by hand again, they sent their voting data over in a .csv file to be electronically counted. I wrote a program that read their .csv file in python and wrote a script to count up the total votes for each candidate and for each county, calculated the overall percentage for each candidate/county. I also wrote my analysis to a second text document to be sent over for the audit using the same code.  


## Overview of Election Audit
1. 369,711 votes were cast in this Congressional Election
   - Jefferson county had 38,850 votes, 10.5% of the total turnout for the election.
   - Arapahoe county had 24,801 votes, 6.7% of the total turnout.
   - Denver county had 306,055 votes, 82.8% of the total turnout.
     - Denver County had the highest number of votes.


2. There were three candidates running for Congress
   - Raymon Anthony Doane received 11,606 votes, a total of 3.1% of the total turnout.
   - Charles Casper Stockham received 85,213 votes, a total of 32.0% of the total turnout.
   - Diana DeGette received 272,892 votes, a total of 73.8% of the total turnout.
     - Diana DeGette won the election with 73.8% of the votes.


## Election-Audit Summary
- The script is set up primarily using lists and dictionaries that run through the data and only populate for unique entries. All of the values used for counting/calculating in the code are read straight from the .csv, so adding more candidates or counties in the next election file will not break the code. The code runs through 369,712 rows in a fraction of a second, meaning that this code can handle a much larger data file.
- This script can easily be modified as well. By adding in an extra for loop, you can calculate the total number of votes and percentage that a candidate received from each county. 
- It can also be modified just by manually adding in the number of eligible voters from the state's census data at the top of the script and adding in a line to divide the census data by the total votes in the state to find the percentage of people in the state who actually voted, for example:
```
Census_Eligible_Voters = 1000000
total_votes = 0 
...
open(file_to_save, "w") as txt_file:
All_Voters_Percent = (float(total_votes) / float(Census_Eligble_Voters) * 100)
election_results = (
     f"\nElection Results\n"
     f"Percent of eligible voters {All_Voters_Percent:,.1f}\n
```
