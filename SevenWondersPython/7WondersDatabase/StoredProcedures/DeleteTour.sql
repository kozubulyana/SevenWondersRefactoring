CREATE PROCEDURE [dbo].[DeleteTour]
	@id BIGINT
AS
	UPDATE [dbo].[Tours] SET IsDeleted = 1 WHERE Id = @id
RETURN 0
