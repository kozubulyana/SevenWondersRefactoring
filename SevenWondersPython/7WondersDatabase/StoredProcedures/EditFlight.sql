CREATE PROCEDURE [dbo].[EditFlight]
	@id BIGINT,
	@number NVARCHAR(MAX),
	@price DECIMAL,
	@departureAirportId BIGINT,
	@arrivalAirportId BIGINT
AS	
	UPDATE Flights
	SET Number = @number,
		Price = @price,
		DepartureAirportId = @departureAirportId,
		ArrivalAirportId = @arrivalAirportId
	WHERE Id = @id;	
RETURN 0
