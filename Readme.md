Python_Bankinq_system_group8.git
Team Members & Responsibilities:
    Member A: Nəzrin Kərimova
    Role: Authentication and Security Manager.
    Implemented Features:
        1.Developed secure user authentication with SHA-256 password hashing.
        2.Implemented failed login attempt tracking per user account.
        3.Created a persistent 60-second countdown timer (lockout_until) that survives application restarts.
        4.Implemented permanent account/card blocking after 6 total failed attempts.
        5.Added secure change_password functionality with strict validation (minimum 8 characters, uppercase, lowercase, digit,    old-vs-new password check, and double confirmation).
        6.Integrated persistent storage logic using users.json to preserve security states and last_login timestamps across restarts.

