CREATE PROCEDURE [dbo].[DeleteCity]
	@id BIGINT
AS
	UPDATE [dbo].[Cities] SET IsDeleted = 1 WHERE Id = @id
RETURN 0
