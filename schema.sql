CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    email UNIQUE NOT NULL,
    phone TEXT,
    password TEXT NOT NULL,
    user_type TEXT NOT NULL,
    hire_date TEXT,
    date_created TEXT,
    active INT DEFAULT 1
     
);

CREATE TABLE IF NOT EXISTS COMPENTENCIES (
    user_id,
    name TEXT NOT NULL,
    date_created TEXT,
    
    FOREIGN KEY (user_id)
            REFERENCES Users (user_id)

);

CREATE TABLE IF NOT EXISTS Assessments (
    user_id,    
    name_of_assessment TEXT NOT NULL,
    date_created TEXT,
    FOREIGN KEY (user_id)
            REFERENCES Users (user_id)
);

CREATE TABLE IF NOT EXISTS Assessment_Results (
    user_id,
    name_of_assessment,
    score TEXT,
    date_taken TEXT,
    manager TEXT NOT NULL,
    
    FOREIGN KEY (user_id)
            REFERENCES Users (user_id),
FOREIGN KEY (name_of_assessment)
            REFERENCES Assessments (name_of_assessment)


);