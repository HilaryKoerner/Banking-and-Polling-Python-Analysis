# Banking and Polling Python Analysis

Using Python, I analyzed two data sets (budgetary data and polling data from CSV files). 

The first challenge is to analyze budget data. The csv file is just two columns of data (date, Profit & Loss). In this exercise I did the following:

1. Counted how many months of data were included in the data set. This was done by putting the dates into their own list and finding the length.
 
![pybankcount](https://user-images.githubusercontent.com/74504885/122773775-3efdfb80-d26e-11eb-92df-0f2eb1d724dc.PNG)

2. Found the total sum of the profit and loss. This was achieved by putting the profit and loss data into a list and calculating the sum.  
3. Calculated the rate of change. I iterated through the csv file and found the difference of each month compared to the previous month. I put these amounts into a dictionary with the corresponding dates. To find the rate of change, I took the sum of the difference and divided that by total months less one month
4. I calculated the greatest increase by finding the max value of my dictionary. I did this for the greatest decrease as well. I pulled the months that corresponded to these amounts

![pybankmonths](https://user-images.githubusercontent.com/74504885/122773875-550bbc00-d26e-11eb-9879-3626fb4fe40e.PNG)

5. I compiled the findings into an easy-to-read python print out and exported the findings to a text file 

![pybank](https://user-images.githubusercontent.com/74504885/122773281-d6af1a00-d26d-11eb-91c7-13b118614aab.PNG)

  
The second challenge was to analyze election results. This csv file had three columns (voter ID, county, vote cast by ID). In this exercise I did the following:
1. Found the total number of votes cast. I did list by pulling the votes IDs into one list and finding the length. 

![pypollvotecount](https://user-images.githubusercontent.com/74504885/122774173-9734fd80-d26e-11eb-9828-eac996a3ac8c.PNG)

2. I calculated the votes each candidate received and found the percentage of votes. I did this by using the candidates' names and if statements. I found the percentage by dividing the candidate vote total by the total number of votes. 
3. I determined the winner by using if/and statements. If a candidate had more votes than the other three candidates, they were determined the winner. 

![pypollwinner](https://user-images.githubusercontent.com/74504885/122774238-a2882900-d26e-11eb-87fd-16036b9bf816.PNG)


4. I compiled the findings into an easy-to-read python print out and exported the findings to a text file. 

![pypoll](https://user-images.githubusercontent.com/74504885/122773298-dc0c6480-d26d-11eb-8f25-89b840106729.PNG)

  
