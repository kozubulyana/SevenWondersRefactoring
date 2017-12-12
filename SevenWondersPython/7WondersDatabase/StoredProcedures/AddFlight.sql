CREATE PROCEDURE [dbo].[AddFlight]
	@number NVARCHAR(MAX),
	@price DECIMAL,
	@airplaneId BIGINT,
	@departureAirportId BIGINT,
	@arrivalAirportId BIGINT

AS	
	INSERT INTO Flights(Number, Price, AirplaneId, DepartureAirportId, ArrivalAirportId, IsDeleted)
	VALUES (@number, @price, @airplaneId, @departureAirportId, @arrivalAirportId, 0);	
RETURN 0