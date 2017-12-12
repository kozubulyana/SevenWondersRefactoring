CREATE PROCEDURE [dbo].[GetManagerByEmail]
	@email NVARCHAR(MAX)
AS
	SELECT * FROM Managers WHERE Email = @email
RETURN 0