CREATE PROCEDURE [dbo].[GetToursForManager]
	@managerId BIGINT
AS
	SELECT Tours.Id, 
		TourStates.Name as TourState,
		Customers.FirstName AS CustomerFirstName,
		Customers.LastName AS CustomerLastName,
		Customers.Email AS CustomerEmail,
		Customers.PhoneNumber AS CustomerPhoneNumber,
		Tours.CreationDate AS OrderDate,
		Tours.TotalPrice AS Price,
		Reservations.LeaveDate,
		Reservations.ReturnDate,
		DepartureAirport.Code as DepartureAirportCode,
		CityDeparture.Name as DepartureAirportCity,
		CountryDeparture.Name as DepartureAirportCountry,
		ArrivalAirport.Code as ArrivalAirportCode,
		CityArrival.Name as ArrivalAirportCity,
		CountryArrival.Name as ArrivalAirportCountry,
		Hotels.Id AS HotelId,
		Hotels.Name AS HotelName
	FROM Tours
	JOIN Reservations ON Tours.ReservationId=Reservations.Id
	JOIN Rooms ON Reservations.RoomId=Rooms.Id
	JOIN Hotels ON Rooms.HotelId=Hotels.Id
	JOIN Cities as CityArrival on CityArrival.Id=Hotels.CityId
	JOIN Countries as CountryArrival on CityArrival.CountryId=CountryArrival.Id
	JOIN Customers ON Tours.CustomerId=Customers.Id
	JOIN TourStates ON Tours.TourStateId=TourStates.Id
	JOIN Schedules ON Reservations.LeaveScheduleId=Schedules.Id
	JOIN Flights ON Schedules.FlightId=Flights.Id
	JOIN Airports as DepartureAirport ON DepartureAirport.Id=Flights.DepartureAirportId
	JOIN Airports as ArrivalAirport ON ArrivalAirport.Id=Flights.ArrivalAirportId
	JOIN Cities as CityDeparture on CityDeparture.Id=DepartureAirport.CityId
	JOIN Countries as CountryDeparture on CityDeparture.CountryId=CountryDeparture.Id
	WHERE CountryArrival.ManagerId = @managerId AND Tours.IsDeleted = 0 AND Reservations.IsDeleted = 0
	ORDER  BY Tours.CreationDate DESC
RETURN 0