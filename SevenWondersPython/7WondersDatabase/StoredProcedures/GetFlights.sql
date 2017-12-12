CREATE PROCEDURE [dbo].[GetFlights]
AS
	SELECT Flights.Id,
		Flights.Number,
		departureAirports.Id as DepartureAirportId,
		departureAirports.Code as DepartureAirportCode,
		departureAirports.Name as DepartureAirportName,
		departureCities.Name as DepartureAirportCityName,
		departureCountries.Name as DepartureAirportCountryName ,
		arrivalAirports.Id as ArrivalAirportId,
		arrivalAirports.Code as ArrivalAirportCode,
		arrivalAirports.Name as ArrivalAirportName,
		arrivalCities.Name as ArrivalAirportCityName,
		arrivalCountries.Name as ArrivalAirportCountryName,
		Flights.Price as Price,
		Airplanes.Id as AirplaneId,
		Airplanes.SeatsAmount as AirplaneSeatsAmount,
		Airplanes.Company as AirplaneCompany,
		Airplanes.Model as AirplaneModel
	FROM Flights
	JOIN Airplanes ON Flights.AirplaneId = Airplanes.Id
	JOIN Airports as departureAirports ON Flights.DepartureAirportId = departureAirports.Id
	JOIN Cities as departureCities ON departureAirports.CityId = departureCities.Id
	JOIN Countries as departureCountries ON departureCities.CountryId = departureCountries.Id
	JOIN Airports as arrivalAirports ON Flights.ArrivalAirportId = arrivalAirports.Id
	JOIN Cities as arrivalCities ON arrivalAirports.CityId = arrivalCities.Id
	JOIN Countries as arrivalCountries ON arrivalCities.CountryId = arrivalCountries.Id
	WHERE Flights.IsDeleted = 0 AND
		 departureAirports.IsDeleted = 0  AND
		 departureCities.IsDeleted = 0  AND
		 departureCountries.IsDeleted = 0  AND
		 arrivalAirports.IsDeleted = 0 AND
		 arrivalCities.IsDeleted = 0 AND
		 arrivalCountries.IsDeleted = 0 
	ORDER BY Flights.Number
RETURN 0
