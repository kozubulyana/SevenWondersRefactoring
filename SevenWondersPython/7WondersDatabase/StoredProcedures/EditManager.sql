--CREATE FUNCTION dbo.SplitInts
--(
--   @List      VARCHAR(MAX),
--   @Delimiter VARCHAR(255)
--)
--RETURNS TABLE
--AS
--  RETURN ( SELECT Item = CONVERT(INT, Item) FROM
--      ( SELECT Item = x.i.value('(./text())[1]', 'varchar(max)')
--        FROM ( SELECT [XML] = CONVERT(XML, '<i>'
--        + REPLACE(@List, @Delimiter, '</i><i>') + '</i>').query('.')
--          ) AS a CROSS APPLY [XML].nodes('i') AS x(i) ) AS y
--      WHERE Item IS NOT NULL
--  );
--GO

--CREATE FUNCTION [dbo].SplitString(@input AS Varchar(4000) )
--RETURNS
--      @Result TABLE(Value BIGINT)
--AS
--BEGIN
--      DECLARE @str VARCHAR(20)
--      DECLARE @ind Int
--      IF(@input is not null)
--      BEGIN
--            SET @ind = CharIndex(',',@input)
--            WHILE @ind > 0
--            BEGIN
--                  SET @str = SUBSTRING(@input,1,@ind-1)
--                  SET @input = SUBSTRING(@input,@ind+1,LEN(@input)-@ind)
--                  INSERT INTO @Result values (@str)
--                  SET @ind = CharIndex(',',@input)
--            END
--            SET @str = @input
--            INSERT INTO @Result values (@str)
--      END
--      RETURN
--END

CREATE PROCEDURE [dbo].[EditManager]
	@id BIGINT,
	@firstName NVARCHAR(MAX),
	@lastName NVARCHAR(MAX),
	@dateOfBirth DATETIME,
	@phoneNumber NVARCHAR(MAX),
	@email NVARCHAR(MAX),
	@password NVARCHAR(MAX),
	@countriesList NVARCHAR(MAX)

AS
	BEGIN TRANSACTION
		DECLARE @countries TABLE (Id INT)
		INSERT INTO @countries(Id) (SELECT * FROM dbo.SplitString(@countriesList))
		DECLARE @currentEmail NVARCHAR(MAX)
		SET @currentEmail = (SELECT Email FROM Managers WHERE Id = @id)
		BEGIN TRY
			UPDATE Managers
			SET FirstName = @firstName,
				LastName = @lastName,
				PhoneNumber = @phoneNumber,
				DateOfBirth = @dateOfBirth,
				Email = @email
			WHERE Id = @id

			UPDATE Users
			SET Email = @email,
				Password = @password
			WHERE Email = @currentEmail

			DECLARE @countriesCount BIGINT
			SET @countriesCount = (SELECT COUNT(Id) FROM @countries)
			WHILE (@countriesCount > 0)
			BEGIN
				UPDATE Countries
				SET ManagerId = @id
				WHERE Id = (SELECT TOP 1 Id FROM @countries)
				DELETE FROM @countries WHERE Id = (SELECT TOP 1 Id FROM @countries)
				SET @countriesCount = @countriesCount - 1
			END
			COMMIT
			SELECT 0 AS Result
		END TRY
		BEGIN CATCH
			SELECT ERROR_MESSAGE() AS Result
			ROLLBACK
		END CATCH
RETURN 0
