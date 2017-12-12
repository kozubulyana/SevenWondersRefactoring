CREATE PROCEDURE [dbo].[GetRoom]
	@roomId BIGINT
AS 
	SELECT Rooms.Id, 
		Rooms.Price, 	
		Hotels.FoodPrice
	FROM Rooms
	JOIN Hotels ON Rooms.HotelId = Hotels.Id
	WHERE Rooms.Id = @roomId 
RETURN 0 