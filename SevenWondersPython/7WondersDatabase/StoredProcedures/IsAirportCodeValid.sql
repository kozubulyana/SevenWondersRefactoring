CREATE PROCEDURE [dbo].[IsAirportCodeValid]
	@id BIGINT,
	@code NVARCHAR(3)
AS	
	IF EXISTS (SELECT * FROM Airports WHERE Id <> @id AND Code = @code AND IsDeleted = 0)
		SELECT 'False';
	ELSE
		SELECT 'True';
RETURN 0;