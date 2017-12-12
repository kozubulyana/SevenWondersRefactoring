CREATE PROCEDURE [dbo].[GetAirport]
	@id BIGINT
AS
	SELECT * FROM Airports
	WHERE Id = @id
RETURN 0
