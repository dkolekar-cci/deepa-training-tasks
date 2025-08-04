CREATE TABLE `college_db`.`users` (
  `user_id` INT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `age` INT NULL CHECK(age>=16 AND age<=30),
  `department` VARCHAR(50) NULL,
  `email` VARCHAR(100) NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE);