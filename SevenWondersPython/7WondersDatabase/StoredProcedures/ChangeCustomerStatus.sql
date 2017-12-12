CREATE PROCEDURE [dbo].[ChangeCustomerStatus]
	@id BIGINT
AS
	DECLARE @deleted BIT;
	SET @deleted = (SELECT IsDeleted FROM [dbo].[Customers] WHERE Id = @id)
		UPDATE [dbo].[Customers] SET IsDeleted = ABS(@deleted - 1) WHERE Id = @id
RETURN 0
