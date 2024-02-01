-- Answer-1
SELECT 
	Shippers.ShipperID,Shippers.ShipperName,Shippers.Phone,count(Orders.OrderID) as Count_of_Orders
FROM 
       Shippers INNER JOIN Orders on Shippers.ShipperID=Orders.ShipperID 
GROUP BY 
         Shippers.ShipperID,Shippers.ShipperName,Shippers.Phone
HAVING 
          count(Orders.OrderID)>0;

--Answer-2
SELECT 
	Shippers.ShipperID,Shippers.ShipperName,Shippers.Phone,count(Orders.OrderID) as Count_of_Orders
FROM 
	Shippers INNER JOIN Orders on Shippers.ShipperID=Orders.ShipperID 
GROUP BY 
	Shippers.ShipperID,Shippers.ShipperName,Shippers.Phone
HAVING 
	count(Orders.OrderID)=0;


--Answer-3
SELECT 
    Customers.CustomerID,
    Customers.CustomerName,
    Orders.OrderID,
    Orders.OrderDate
FROM 
    Customers, Orders
WHERE 
    Customers.CustomerID = Orders.CustomerID
    AND Orders.ShipperID IS NULL
    AND Orders.ShipperID NOT IN (SELECT ShipperID FROM Shippers);
