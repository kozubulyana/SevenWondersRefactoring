CREATE PROCEDURE [dbo].[GetCountriesForManager]
	@id BIGINT 
AS
	SELECT * FROM Countries WHERE ManagerId = @id
RETURN 0
