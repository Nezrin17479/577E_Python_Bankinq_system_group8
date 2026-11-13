Python_Bankinq_system_group8.git
Team Members & Responsibilities:
    Member A: Nəzrin Kərimova:
        Role: Authentication and Security Manager.
        Implemented Features:
            1.Developed secure user authentication with SHA-256 password hashing.
            2.Implemented failed login attempt tracking per user account.
            3.Created a persistent 60-second countdown timer (lockout_until) that survives application restarts.
            4.Implemented permanent account/card blocking after 6 total failed attempts.
            5.Added secure change_password functionality with strict validation (minimum 8 characters, uppercase, lowercase, digit,    old-vs-new password check, and double confirmation).
            6.Integrated persistent storage logic using users.json to preserve security states and last_login timestamps across restarts.
    Member B:Mehdi Məhərrəmli:
        Role:Account Management and Banking Operations.
        Implemented Features:
            1.Developed core banking operations including balance checking, fund deposits, and cash withdrawals.
            2.Implemented secure money transfer logic between different user accounts with proper validation checks.
            3.Ensured that all financial transactions update the persistent users.json data file accurately in real-time.
            4.Handled business logic exceptions related to insufficient funds and invalid transaction amounts.
    Member C:Akif Teymurov:
        Role:User Interface, Menu Navigation, and Transaction History.
        Implemented Features:
            1.Designed and structured the interactive terminal-based menu system for seamless user navigation.
            2.Implemented transaction history tracking and detailed activity logging for user actions.
            3.Coordinated the integration of independent modules (Authentication, Operations, and Data Storage).
            4.Conducted system testing, general error handling, and managed the overall program execution flow.
    

