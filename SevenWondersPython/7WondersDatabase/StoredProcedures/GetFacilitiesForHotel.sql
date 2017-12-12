CREATE PROCEDURE [dbo].[GetFacilitiesForHotel]
	@hotelId BIGINT
AS	
	SELECT Facilities.Name
	FROM Facilities
	JOIN FacilityHotels ON Facilities.Id = FacilityHotels.Facility_Id
	JOIN Hotels ON FacilityHotels.Hotel_Id = Hotels.Id
	WHERE Hotel_Id = @hotelId
RETURN 0
