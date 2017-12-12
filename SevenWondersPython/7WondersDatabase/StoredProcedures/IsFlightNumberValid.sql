CREATE PROCEDURE [dbo].[IsFlightNumberValid]
	@id BIGINT,
	@number NVARCHAR(MAX)
AS	
	IF EXISTS (SELECT * FROM Flights WHERE Id <> @id AND Number = @number AND IsDeleted=0)
		SELECT 'False';
	ELSE
		SELECT 'True';
RETURN 0;