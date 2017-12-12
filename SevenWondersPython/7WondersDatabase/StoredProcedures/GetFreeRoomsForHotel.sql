CREATE PROCEDURE [dbo].[GetFreeRoomsForHotel]
	@hotelId BIGINT,
	@departureDate Date,
	@arrivalDate Date,
	@people INT
AS	
	SELECT allRooms.Id,
		RoomTypes.Name as RoomType,
		allRooms.MaxPeople,
		allRooms.Price,
		allRooms.WindowView
	FROM Rooms as allRooms
	JOIN RoomTypes on allRooms.RoomTypeId=RoomTypes.Id
	WHERE IsDeleted = 0 AND
		 allRooms.MaxPeople >= @people AND
		 allRooms.HotelId = @hotelId AND
		 NOT EXISTS (SELECT *
                   FROM Reservations
				   JOIN Tours ON Reservations.Id=Tours.ReservationId
                   WHERE Tours.IsDeleted = 0 AND
						Reservations.IsDeleted = 0 AND
						RoomId = allRooms.Id AND
						NOT(@departureDate >= ReturnDate) AND NOT (@arrivalDate <= LeaveDate))
	ORDER BY allRooms.Price
RETURN 0