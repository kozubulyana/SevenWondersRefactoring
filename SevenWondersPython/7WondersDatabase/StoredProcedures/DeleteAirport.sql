CREATE PROCEDURE [dbo].[DeleteAirport]
	@id BIGINT
AS
	UPDATE [dbo].[Airports] SET IsDeleted = 1 WHERE Id = @id
RETURN 0
