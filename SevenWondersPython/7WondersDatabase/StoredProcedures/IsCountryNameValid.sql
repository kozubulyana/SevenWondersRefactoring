CREATE PROCEDURE [dbo].[IsCountryNameValid]
	@id BIGINT,
	@name NVARCHAR(MAX)
AS	
	IF EXISTS (SELECT * FROM Countries WHERE Id <> @id AND Name = @name AND IsDeleted=0)
		SELECT 'False';
	ELSE
		SELECT 'True';
RETURN 0;