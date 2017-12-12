CREATE PROCEDURE [dbo].[GetCustomer]
	@id BIGINT
AS 
	SELECT Id,
		FirstName,
		LastName,
		DateOfBirth,
		PhoneNumber,
		Email,
		Discount
	FROM Customers
	WHERE Id = @id
RETURN 0 