CREATE PROCEDURE [dbo].[EditSchedule]
	@id BIGINT,
	@dayOfWeek INT,
	@departureTime Time,
	@arrivalTime Time
AS	
	UPDATE Schedules
	SET DayOfWeek = @dayOfWeek,
		DepartureTime = @departureTime,
		ArrivalTime = @arrivalTime,
		IsDeleted = 0
	WHERE Id = @id;	
RETURN 0