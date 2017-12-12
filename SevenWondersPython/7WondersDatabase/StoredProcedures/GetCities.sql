CREATE PROCEDURE [dbo].[GetCities]
		@countryId INT = NULL,
		@cityId INT = NULL
AS
	IF @countryId IS NOT NULL
		IF @cityId IS NOT NULL
			SELECT Cities.Id, Cities.Name, Cities.CountryId, Countries.Name as CountryName
			FROM Cities
			JOIN Countries ON Cities.CountryId=Countries.Id
			WHERE Cities.IsDeleted = 0 AND Countries.IsDeleted = 0 AND Countries.Id=@countryId AND Cities.Id=@cityId
			ORDER BY Name
		ELSE 
			SELECT Cities.Id, Cities.Name, Cities.CountryId, Countries.Name as CountryName
			FROM Cities
			JOIN Countries ON Cities.CountryId=Countries.Id
			WHERE Cities.IsDeleted = 0 AND Countries.IsDeleted = 0 AND Countries.Id=@countryId 
			ORDER BY Name
	ELSE
		SELECT Cities.Id, Cities.Name, Cities.CountryId, Countries.Name as CountryName
		FROM Cities
		JOIN Countries ON Cities.CountryId=Countries.Id
		WHERE Cities.IsDeleted = 0 AND Countries.IsDeleted = 0
		ORDER BY CountryName, Name
RETURN 0