CREATE PROCEDURE [dbo].[GetCustomerByEmail]
	@email NVARCHAR(MAX)
AS
	SELECT * FROM Customers WHERE Email = @email 
RETURN 0