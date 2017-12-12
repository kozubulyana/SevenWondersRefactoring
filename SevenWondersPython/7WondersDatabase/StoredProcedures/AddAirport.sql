CREATE PROCEDURE [dbo].[AddAirport]
	@id BIGINT,
	@name NVARCHAR(MAX),
	@code NVARCHAR(3),
	@cityId BIGINT
AS	
	IF EXISTS (SELECT * FROM Airports WHERE Id = @id)
		UPDATE Airports
		SET Name = @name, Code=@code, CityId = @cityId
		WHERE Id = @id;
	ELSE
		INSERT INTO Airports(Name, Code, CityId, IsDeleted)
		VALUES (@name, @code, @cityId, 0);	
RETURN 0