CREATE PROCEDURE [dbo].[GetCountry]
	@id BIGINT
AS
	SELECT * FROM Countries
	WHERE Id = @id
RETURN 0
