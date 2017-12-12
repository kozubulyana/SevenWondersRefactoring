CREATE PROCEDURE [dbo].[IsCityNameValid]
	@id BIGINT,
	@name NVARCHAR(MAX),
	@countryId BIGINT
AS	
	IF EXISTS (SELECT * FROM Cities WHERE Id <> @id AND Name = @name AND CountryId = @countryId AND IsDeleted = 0)
		SELECT 'False';
	ELSE
		SELECT 'True';
RETURN 0;