# Product Sales 

analyse these sales informations and find out key insights from user behaviour. 

dataset** contains the sales history (almost half a million records) for the period of almost an year for certain product categories.

The dataset does not have proper 'Unit price' as it was corrupted and I would request your help to fix it with the help of products datasets.

KPI : 'Revenue by product category' 

    DSLR cameras
    Smartphones
    Processors
    Monitors
    Mouse
    Keyboards

To modify and include the missing informations in sales table, you have to use SQL Joins and ensure the number of record counts after each operation.

To SUM UP, you should recieve the below 7 datasets:

    sales.csv
    dslr.csv
    smartphone.csv
    processor.csv
    monitor.csv
    mouse.csv
    keyboard.csv

sales. csv : The sales data have below infomations:

InvoiceNo: A 8-digit integral number uniquely assigned to each transaction. If this code starts with letter 'C', it indicates a cancellation.

StockCode: A 5-digit integral number uniquely assigned to each distinct product.

Description: Product (item) name as mentioned on Amazon website.

Quantity: The quantities of each product (item) per transaction.

InvoiceDate: the day and time when each transaction was generated.

UnitPrice: Product price per unit in USD.

CustomerID: a 5-digit integral number uniquely assigned to each customer.

Country: the name of the country where each customer resides.

QUESTIONS: 

•	What are the top 5 items generating the maximum revenue.
•	How is the customer buying pattern.
(I would be interested to know weekly, monthly, daily etc.)
•	There might be various factors that might play a role. In my last assignment, I used to observe people place a lot of orders in the lunch time. So, this kind of information would add values to our analysis.
•	Is there any specific days when the sales have been unusually high / low and what could be the possible reasons? (This is a very generic question and most of the time you have to make an educated guess with a supporting data)
•	What do you think about the customers? Are they individuals or wholesalers?
Can you grab any other information on this.
•	Highest number of orders and highest money spent: Can you explore a bit on this.. like which countries / customers.
A plot detailing number of orders countrywise and another plot depicting amount of money spent country wise would do the job.
•	Top 5 countries generating the max revenue. (Can you create a map of them - this is optional and good to have)
•	How about excluding the host country ('Germany in this case) to do the same analysis.
•	Quarterly revenue ( How about creating a plotly express animation)
•	What are the best-selling and the second best-selling products in every category? (Revenue wise).(Hint: explore SQL Window function)
•	New Customer registrations per month for the year 2019.You can consider MIN("InvoiceDate") as the registration date.
•	Can you create a plot showing the growth rate of new customers for the same period (2019).
•	What are the other KPIs you can think of. (Ex- Average revenue per customer for each month in the year 2019)
