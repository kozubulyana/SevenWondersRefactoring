CREATE PROCEDURE [dbo].[GetEquipmentsForRoom]
	@roomId INT
AS	
	SELECT Equipments.Name
	FROM Equipments
	JOIN EquipmentRooms ON Equipments.Id = EquipmentRooms.Equipment_Id
	JOIN Rooms ON EquipmentRooms.Room_Id = Rooms.Id
	WHERE Room_Id = @roomId
RETURN 0