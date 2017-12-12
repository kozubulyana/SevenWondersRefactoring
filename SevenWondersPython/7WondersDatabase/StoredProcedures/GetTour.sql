CREATE PROCEDURE [dbo].[GetTour]
	@id BIGINT
AS
	SELECT Tours.Id, 
		Reservations.LeaveDate,
		Reservations.ReturnDate,
		Reservations.LeaveScheduleId,
		Reservations.ReturnScheduleId,
		CityDeparture.Name as DepartureCity,
		CountryDeparture.Name as DepartureCountry,
		CityArrival.Name as ArrivalCity,
		CountryArrival.Name as ArrivalCountry
	FROM Tours
	JOIN Reservations ON Tours.ReservationId=Reservations.Id	
	JOIN Rooms ON Reservations.RoomId=Rooms.Id
	JOIN Hotels ON Rooms.HotelId=Hotels.Id
	JOIN Cities as CityArrival on CityArrival.Id=Hotels.CityId
	JOIN Countries as CountryArrival on CityArrival.CountryId=CountryArrival.Id
	JOIN Schedules ON Reservations.LeaveScheduleId=Schedules.Id
	JOIN Flights ON Schedules.FlightId=Flights.Id
	JOIN Airports as DepartureAirport ON DepartureAirport.Id=Flights.DepartureAirportId
	JOIN Cities as CityDeparture on CityDeparture.Id=DepartureAirport.CityId
	JOIN Countries as CountryDeparture on CityDeparture.CountryId=CountryDeparture.Id
	WHERE Tours.Id = @id
RETURN 0