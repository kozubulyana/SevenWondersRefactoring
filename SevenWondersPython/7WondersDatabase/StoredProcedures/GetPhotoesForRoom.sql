CREATE PROCEDURE [dbo].[GetPhotoesForRoom]
	@roomId BIGINT
AS	
	SELECT Id, photoLink
	FROM RoomsPhotoes
	WHERE RoomId = @roomId
RETURN 0