CREATE PROCEDURE [dbo].[AddCountry]
	@id BIGINT,
	@name NVARCHAR(MAX)
AS	
	IF EXISTS (SELECT * FROM Countries WHERE Id = @id)
		UPDATE Countries
		SET Name= @name
		WHERE Id=@id;
	ELSE
		INSERT INTO Countries (Name, ManagerId, IsDeleted)
		VALUES (@name,NULL, 0);	
RETURN 0
