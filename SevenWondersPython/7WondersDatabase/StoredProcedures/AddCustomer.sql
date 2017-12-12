CREATE PROCEDURE [dbo].[AddCustomer]
	@firstName NVARCHAR(MAX),
	@lastName NVARCHAR(MAX),
	@dateOfBirth DATETIME,
	@phoneNumber NVARCHAR(MAX),
	@email NVARCHAR(MAX),
	@password NVARCHAR(MAX)
	AS
	BEGIN
		INSERT INTO Users(Email, Password, RoleId)
		VALUES (@email, @password, 1);

		INSERT INTO Customers(FirstName, LastName, PhoneNumber, DateOfBirth, IsDeleted, CityId, Email, TotalPayment, Discount)
		VALUES (@firstName, @lastName, @phoneNumber, @dateOfBirth, 0 , null, @email, 0, 0);
	END
RETURN 0