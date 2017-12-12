CREATE PROCEDURE [dbo].[GetAirports]
AS
	SELECT Airports.Id, Airports.Name, Airports.Code, Airports.CityId, Cities.Name as CityName
	FROM Airports
	JOIN Cities ON Airports.CityId=Cities.Id
	JOIN Countries ON Cities.CountryId = Countries.Id
	WHERE Cities.IsDeleted = 0 AND Airports.IsDeleted = 0 AND Countries.IsDeleted = 0
	ORDER BY Name
RETURN 0