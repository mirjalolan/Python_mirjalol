

import sqlite3 as sql
import pandas as pd
conn = sql.connect('homeworks\\chinook.db')


# Customer Purchases Analysis:
# Find the total amount spent by each customer on purchases (considering invoices).
# Identify the top 5 customers with the highest total purchase amounts.
# Display the customer ID, name, and the total amount spent for the top 5 customers.
query = '''
SELECT
    c.CustomerID,
    CONCAT(c.FirstName, ' ', c.LastName) as FullName,
    sum(i.Total) as TotalSpent
FROM invoices as i
INNER JOIN customers as c
on i.CustomerID = c.CustomerID
GROUP BY c.CustomerID
ORDER BY TotalSpent DESC
LIMIT 5
'''
result = pd.read_sql_query(query, conn)
print(result)


# Album vs. Individual Track Purchases:
# Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
# A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
# Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).
query = '''
WITH CustomerAlbumPurchases AS (
    SELECT 
        i.CustomerId,
        t.AlbumId,
        COUNT(DISTINCT ii.TrackId) AS PurchasedTracks,
        (SELECT COUNT(*) FROM tracks WHERE AlbumId = t.AlbumId) AS TotalTracks
    FROM invoices i
    JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
    JOIN tracks t ON ii.TrackId = t.TrackId
    GROUP BY i.CustomerId, t.AlbumId
),
CustomerPreference AS (
    SELECT 
        CustomerId,
        CASE 
            WHEN MAX(CASE WHEN PurchasedTracks = TotalTracks THEN 1 ELSE 0 END) = 1
            THEN 'Full Album'
            ELSE 'Individual Tracks'
        END AS Preference
    FROM CustomerAlbumPurchases
    GROUP BY CustomerId
)
SELECT 
    Preference,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customers) AS PercentageOfCustomers
FROM CustomerPreference
GROUP BY Preference;
'''
result = pd.read_sql_query(query, conn)
print(result)
