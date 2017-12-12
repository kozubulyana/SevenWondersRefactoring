CREATE PROCEDURE [dbo].[DeleteCountry]
	@id BIGINT
AS
	UPDATE Countries
	SET IsDeleted = 1
	WHERE Id = @id
RETURN 0