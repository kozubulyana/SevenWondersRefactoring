CREATE PROCEDURE [dbo].[AddAirplane]
	@model NVARCHAR(MAX),
	@company NVARCHAR(MAX),
	@seatsAmount INT
AS	
	INSERT INTO Airplanes(Model, Company, SeatsAmount, IsDeleted)
	OUTPUT Inserted.Id
	VALUES (@model, @company, @seatsAmount, 0);	
RETURN 0
