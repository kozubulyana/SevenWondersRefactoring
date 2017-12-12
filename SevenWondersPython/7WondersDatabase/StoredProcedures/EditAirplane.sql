CREATE PROCEDURE [dbo].[EditAirplane]
	@id BIGINT,
	@model NVARCHAR(MAX),
	@company NVARCHAR(MAX),
	@seatsAmount INT
AS	
	UPDATE Airplanes
	SET Model = @model,
		Company = @company,
		SeatsAmount = @seatsAmount
	WHERE Id = @id;
RETURN 0