-- Create the TASKS database
CREATE DATABASE TASKStest;

-- Switch to the TASKS database
USE TASKStest;

-- Create the Monday table
CREATE TABLE Monday
(
  TaskID INT
  AUTO_INCREMENT PRIMARY KEY
  , TaskTitle TEXT
  , TaskDescription TEXT
  , Completed BOOLEAN
);

  -- Insert sample data into the Monday table
  INSERT INTO
  Monday
    (TaskTitle, TaskDescription, Completed)
  VALUES
    ('Project Setup', 'Create GitHub repository and set up development environment', TRUE),
    ('Project Planning', 'Jump on a team call to meet peers', TRUE),
    ('Task Assignment', 'Divide assignment into smaller tasks and assign team members', TRUE),
    ('Coding and Implementation', 'Write code to address requirements', FALSE),
    ('Documentation', 'Write README files, code comments, and spell-check', FALSE),
    ('Post-work Discussion', 'Reflect on the work done and go through the list of requirements to make sure all points have been addressed', FALSE),
    ('Celebrate Success', 'Celebrate once instructor reviews and grades the assignment', FALSE);

  SELECT *
  FROM Monday;