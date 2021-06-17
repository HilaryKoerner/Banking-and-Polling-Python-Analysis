# Banking and Polling Python Analysis

Using Python, I analyzed two data sets (budgetary data and polling data from CSV files). 

The first challenge is to analyze budget data. The csv file is just two columns of data (date, Profit & Loss). In this exercise I did the following:

1. Counted how many months of data were included in the data set. This was done by putting the dates into their own list and finding the length. 
2. Found the total sum of the profit and loss. This was achieved by putting the profit and loss data into a list and calculating the sum.  
3. Calculated the rate of change. I iterated through the csv file and found the difference of each month compared to the previous month. I put these amounts into a dictionary with the corresponding dates. To find the rate of change, I took the sum of the difference and divided that by total months less one month
4. I calculated the greatest increase by finding the max value of my dictionary. I did this for the greatest decrease as well. I pulled the months that corresponded to these amounts
5. I compiled the findings into an easy-to-read python print out and exported the findings to a text file 
  
The second challenge was to analyze election results. This csv file had three columns (voter ID, county, vote cast by ID). In this exercise I did the following:
1. Found the total number of votes cast. I did list by pulling the votes IDs into one list and finding the length. 
2. I calculated the votes each candidate received and found the percentage of votes. I did this by using the candidates' names and if statements. I found the percentage by dividing the candidate vote total by the total number of votes. 
3. I determined the winner by using if/and statements. If a candidate had more votes than the other three candidates, they were determined the winner. 
4. I compiled the findings into an easy-to-read python print out and exported the findings to a text file. 
  
