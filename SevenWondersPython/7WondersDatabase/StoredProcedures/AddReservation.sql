CREATE PROCEDURE [dbo].[AddReservation]
	@roomId BIGINT,
	@personAmount INT,
	@leaveScheduleId BIGINT,
	@returnScheduleId BIGINT,
	@leaveDate DATE,
	@returnDate DATE,
	@withoutFood BIT
AS 
	INSERT INTO Reservations(PersonAmount, LeaveDate, ReturnDate, RoomId, LeaveScheduleId, ReturnScheduleId, IsDeleted, WithoutFood)
		VALUES (@personAmount, @leaveDate, @returnDate, @roomId, @leaveScheduleId, @returnScheduleId, 0, @withoutFood);
	SELECT @@IDENTITY
RETURN 0