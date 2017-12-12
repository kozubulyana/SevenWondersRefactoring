
CREATE PROCEDURE [dbo].[AddManager]
	@id BIGINT,
	@firstName NVARCHAR(MAX),
	@lastName NVARCHAR(MAX),
	@dateOfBirth DATETIME,
	@phoneNumber NVARCHAR(MAX),
	@email NVARCHAR(MAX),
	@password NVARCHAR(MAX),
	@countriesList NVARCHAR(MAX)
AS
	
	IF EXISTS (SELECT Id FROM Managers WHERE Id = @id)
		BEGIN
		EXEC [dbo].[EditManager] @id, @firstName, @lastName, @dateOfBirth, @phoneNumber, @email, @password, @countriesList
		END
	ELSE
		BEGIN
		BEGIN TRANSACTION
		DECLARE @countries TABLE (Id INT)
		INSERT INTO @countries(Id) (SELECT * FROM dbo.SplitString(@countriesList))
		DECLARE @currentEmail NVARCHAR(MAX)
		SET @currentEmail = (SELECT Email FROM Managers WHERE Id = @id)
		BEGIN TRY
			INSERT INTO Managers([FirstName], [LastName], [PhoneNumber], [DateOfBirth], [Email], [IsDeleted]) VALUES(@firstName, @lastName, @phoneNumber, @dateOfBirth, @email, 0)
			DECLARE @managerRole BIGINT
			SET @managerRole = 3
			INSERT INTO Users([Email], [Password], [RoleId]) VALUES (@email, @password, @managerRole)


			DECLARE @countriesCount BIGINT
			SET @countriesCount = (SELECT COUNT(Id) FROM @countries)
			WHILE (@countriesCount > 0)
			BEGIN
				UPDATE Countries
				SET ManagerId = (SELECT MAX(Id) FROM Managers)
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
		END
RETURN 0