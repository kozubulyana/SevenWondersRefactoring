CREATE PROCEDURE [dbo].[ChangeManagerStatus]
	@id BIGINT
AS
	DECLARE @deleted BIT;
	SET @deleted = (SELECT IsDeleted FROM [dbo].[Managers] WHERE Id = @id)
		UPDATE [dbo].[Managers] SET IsDeleted = ABS(@deleted - 1) WHERE Id = @id
RETURN 0
