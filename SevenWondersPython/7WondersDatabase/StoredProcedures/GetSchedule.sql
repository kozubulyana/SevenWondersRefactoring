CREATE PROCEDURE [dbo].[GetSchedule]
	@id BIGINT
AS 
	SELECT Schedules.Id,
		Flights.Id as FlightId,
		Flights.Price as FlightPrice,
		Flights.Number as FlightNumber,
		Airplanes.Company as FlightAirplaneCompany,
		Airplanes.Model as FlightAirplaneModel,
		departureAirports.Name as FlightDepartureAirport,
		arrivalAirports.Name as FlightArrivalAirport,
		Schedules.DepartureTime,
		Schedules.ArrivalTime
	FROM Schedules
	JOIN Flights ON Schedules.FlightId = Flights.Id
	JOIN Airplanes ON Flights.AirplaneId = Airplanes.Id
	JOIN Airports as departureAirports ON Flights.DepartureAirportId = departureAirports.Id
	JOIN Airports as arrivalAirports ON Flights.ArrivalAirportId = arrivalAirports.Id
	WHERE Schedules.Id = @id
RETURN 0 