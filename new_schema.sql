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
    compentency_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    date_created TEXT

);

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER PRIMARY KEY,
    compentency_id,    
    name_of_assessment TEXT NOT NULL,
    date_created TEXT,

    FOREIGN KEY (compentency_id)
            REFERENCES COMPENTENCIES (compentency_id)
);

CREATE TABLE IF NOT EXISTS Assessment_Results (
    assessment_result_id INTEGER PRIMARY KEY,
    user_id,
    assessment_id,
    score TEXT,
    date_taken TEXT,
    manager TEXT NOT NULL,
    
    FOREIGN KEY (user_id)
            REFERENCES Users (user_id),
    FOREIGN KEY (assessment_id)
            REFERENCES Assessments (assessment_id)


);