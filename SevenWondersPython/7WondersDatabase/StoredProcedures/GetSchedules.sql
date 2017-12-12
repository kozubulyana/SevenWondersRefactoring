CREATE PROCEDURE [dbo].[GetSchedules]
	@flightId BIGINT
AS 
	SELECT Schedules.Id,
		Schedules.DayOfWeek,
		Schedules.DepartureTime,
		Schedules.ArrivalTime
	FROM Schedules
	JOIN Flights ON Schedules.FlightId = Flights.Id
	WHERE Schedules.FlightId = @flightId AND Schedules.IsDeleted = 0
	ORDER BY Schedules.DayOfWeek 
RETURN 0 