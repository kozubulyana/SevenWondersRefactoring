CREATE PROCEDURE [dbo].[GetManager]
	@id BIGINT
AS
	SELECT * FROM Managers
	WHERE Id = @id
RETURN 0
