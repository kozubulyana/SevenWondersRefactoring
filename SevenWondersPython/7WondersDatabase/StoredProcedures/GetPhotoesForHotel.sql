CREATE PROCEDURE [dbo].[GetPhotoesForHotel]
	@hotelId BIGINT
AS	
	SELECT Id, PhotoLink
	FROM HotelsPhotoes
	WHERE HotelId = @hotelId AND IsDeleted = 0
RETURN 0