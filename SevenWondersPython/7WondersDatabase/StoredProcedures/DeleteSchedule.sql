CREATE PROCEDURE [dbo].[DeleteSchedule]
	@id BIGINT
AS
	UPDATE Schedules
	SET IsDeleted = 1
	WHERE Id = @id
RETURN 0