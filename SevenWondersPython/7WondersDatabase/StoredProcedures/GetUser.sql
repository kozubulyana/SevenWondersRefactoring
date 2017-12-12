CREATE PROCEDURE [dbo].[GetUser]
	@email NVARCHAR(MAX),
	@hashedPassword NVARCHAR(MAX)
AS
	SELECT Id, RoleId FROM Users WHERE Email = @email AND Password = @hashedPassword
RETURN 0