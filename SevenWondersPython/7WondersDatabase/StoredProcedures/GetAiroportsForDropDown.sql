CREATE PROCEDURE [dbo].[GetAiroportsForDropDown]
AS
	SELECT Airports.Id, 
		Airports.Name as Text
	FROM Airports
	JOIN Cities ON Airports.CityId = Cities.Id
	JOIN Countries ON Cities.CountryId = Countries.Id
	WHERE Airports.IsDeleted = 0 AND
		Cities.IsDeleted = 0 AND 
		Countries.IsDeleted = 0		
RETURN 0