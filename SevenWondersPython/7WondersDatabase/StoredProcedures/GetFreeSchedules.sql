CREATE PROCEDURE [dbo].[GetFreeSchedules]
	@cityDepartureId BIGINT,
	@cityArrivalId BIGINT,
	@people INT,
	@date Date
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
	WHERE Schedules.IsDeleted = 0 AND 
		Flights.IsDeleted = 0 AND
		departureAirports.IsDeleted = 0 AND
		arrivalAirports.IsDeleted = 0 AND
		departureAirports.CityId = @cityDepartureId AND
		arrivalAirports.CityId = @cityArrivalId AND
		Schedules.DayOfWeek +1 IN (SELECT DATEPART(dw, @date)) AND
		Airplanes.SeatsAmount > @people
	ORDER BY Flights.Price
RETURN 0 