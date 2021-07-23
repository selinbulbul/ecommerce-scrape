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