CREATE PROCEDURE [dbo].[AddCity]
	@id BIGINT,
	@name NVARCHAR(MAX),
	@countryId BIGINT
AS	
	IF EXISTS (SELECT * FROM Cities WHERE Id = @id)
		UPDATE Cities
		SET Name = @name, CountryId = @countryId
		WHERE Id = @id;
	ELSE
		INSERT INTO Cities(Name, CountryId, IsDeleted)
		VALUES (@name, @countryId, 0);	
RETURN 0