# **PyPoll: Auditing & Validating Election Outcomes with Python**

![](https://github.com/Felrashed/Election_Analysis/blob/main/Resources/Header_Gif.gif)

## **Resources**
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.38., and Excel
- Sweat and Tears 

## **Election Audit: Overview & Purpose**
The Colorado Board of Elections has contracted our firm, Rocky Mountain Data Partners LLC., with automating the process for auditing Congressional election outcomes using **Python.** While this process is traditionally done through excel, the CBE believes that if accomplished, the pilot program's method could become the standard across all elections in the state. The audit of Congressional election results is to include the following:
- Calculate the total number of votes cast.
- A complete list of candidates who received votes.
- Calculate the total number of votes each candidate received.
- Calculate the percentage of votes each candidate won.
- Determine the winner of the election based on popular vote.

In addition to the initial analysis conducted, a secondary audit at the county level was requested as well. The audit has been expanded to include the following county-level requirements:
- The voter turnout for each county.
- The percentage of votes from each county out of the total vote count.
- The county with the highest turnout.

**Initializing Lists and Dictionaries**             |  **Identify Winner and Output Candidate Results**
:-----------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:
![](https://github.com/Felrashed/Election_Analysis/blob/main/Resources/Code_initial_framework.PNG)  |  ![](https://github.com/Felrashed/Election_Analysis/blob/main/Resources/code_winner.PNG)

## **Election-Audit Results**
- **Total Votes:** The total number of votes cast in the election was **369,711 Votes**

- **County-Level Voting Data**
    - **Jefferson County:** **38,855** votes representing **10.5%** of the total votes cast
    - **Denver County:** **306,055** votes representing **82.8%** of the total votes cast
    - **Arapahoe County:** **24,801** votes representing **6.7%** of the total votes cast
    - **Largest County Turnout:** **Denver** with **82.8%** of the total votes cast

- **Candidate Voting Data**
 
    - **List of Candidates Who Received Votes:**
        -   **Charles Casper Stockham**
        -   **Diana DeGette**
        -   **Raymon Anthony Doane**
    - **Final Candidate Vote Counts:**
        -   **Charles Casper Stockham** received **23.0%** of the vote with **85,213** votes.
        -   **Diana DeGette** received **73.8%** of the vote with **272,892** votes.
        -   **Raymon Anthony Doane** received **3.1%** of the vote with **11,606** votes.
    - The **Winner** of the election was:
        -   **Diana DeGette,** who received **272,892** votes accounting for **73.8%** of the vote.

**Results: Terminal Output**             |  **Validated TXT Output File**
:-------------------------:|:-------------------------:
![](https://github.com/Felrashed/Election_Analysis/blob/main/Resources/Output_Terminal.PNG)  |  ![](https://github.com/Felrashed/Election_Analysis/blob/main/Resources/Output_txt_file.PNG)

## **Election-Audit Summary**
The pilot program has proven that the **P**ython-**A**utomated **E**lection **A**udit **T**ool **(PEAT)** was a complete success. PEAT was able to analyze and calculate all the voting data accurately, efficiently, and at a granular level. As designed, the tool can be applied to other elections since it is already formatted to intake any name, prevent duplicates, and maintain a running count of candidates, counties, and votes themselves, This means PEAT can be applied to Congressional, Senatorial, State Gubernatorial, and Gubernatorial election audits and still maintain its data inegrity. Should the Colorado Board of Elections opt to extend Rocky Mountain Data Partners' contract, it would be our reccomendation to include the following: 
1. The CBE should include in future data sets, information relating to the **type** of ballot cast:
    - Since Colorado collects ballots via mail, punchard, and Direct Recording Electronic (DRE) machines, it would be worthwhile to include this data in the analaysis to calculate the share of votes cast by each method. This would ensure that the CBE maintains situational awareness in voting trends to correctly apply resources where needed, has a record of the number of ballots cast by each method as a comparative metric for ensuring election integrity, and allows for potential analysis of voter choice as it relates to chosen methon. 
2. The CBE should also allow for **variance and historical trend** analysis to inspire confidence in the integrity of elections:
    - With historical trends, demographic data for each county and voting district, and current voting outcome data, analaysis can be performed to show variance and/or accuracy among, but not limited to, the following data points:
        - Number of ballots cast vs. Number of Registered Voters
        - Share of overall votes cast for each party in a particular race relative to previous elections
        - Share of votes cast by category (Mail-In, Punch Card, DRE) vs. Previous Election 

**Example Code: Unique Candidate Identification**             |  **Example Code: Geographic Identification**
:-------------------------:|:-------------------------:
![](https://github.com/Felrashed/Election_Analysis/blob/main/Resources/code_example.PNG)  |  ![](https://github.com/Felrashed/Election_Analysis/blob/main/Resources/code_county.PNG)

**PyPoll: A Visual Example Of The Working Code**             |  
:-----------------------------------------------------------------------------------------:|
![](https://github.com/Felrashed/Election_Analysis/blob/main/Resources/Full_Example_Gif.gif)  |