CREATE PROCEDURE [dbo].[AddTour]
	@creationDate DATETIME,
	@totalPrice DECIMAL,
	@reservationId BIGINT,
	@customerId BIGINT
AS 
	INSERT INTO Tours(CreationDate, TotalPrice, ReservationId, CustomerId, TourStateId, IsDeleted)
		VALUES (@creationDate, @totalPrice, @reservationId, @customerId, 1, 0)
RETURN 0 