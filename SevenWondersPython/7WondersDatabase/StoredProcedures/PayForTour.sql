CREATE PROCEDURE [dbo].[PayForTour]
	@id BIGINT
AS
	UPDATE [dbo].[Tours] SET TourStateId = 2
	WHERE Id = @id

	UPDATE [dbo].[Customers] SET TotalPayment += (SELECT TotalPrice FROM Tours WHERE Id = @id)
	WHERE Id = (SELECT CustomerId FROM Tours WHERE Id = @id)
RETURN 0

