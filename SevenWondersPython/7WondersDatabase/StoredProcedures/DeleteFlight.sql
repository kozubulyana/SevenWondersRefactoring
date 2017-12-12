CREATE PROCEDURE [dbo].[DeleteFlight]
	@id BIGINT
AS
	UPDATE Flights
	SET IsDeleted = 1
	WHERE Id = @id
RETURN 0