CREATE PROCEDURE [dbo].[AddSchedule]
	@flightId BIGINT,
	@dayOfWeek INT,
	@departureTime Time,
	@arrivalTime Time
AS	
		INSERT INTO Schedules(DayOfWeek, DepartureTime, ArrivalTime, FlightId, IsDeleted)
		VALUES (@dayOfWeek, @departureTime, @arrivalTime, @flightId, 0);	
RETURN 0

