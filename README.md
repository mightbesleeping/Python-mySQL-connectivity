# Python-mySQL-connectivity
basic train management system based on mysql database connected with simplicity of python

Train Management System

This Python program provides a user-friendly interface to manage train data in a MySQL database named student (you can easily modify this to your desired database name). It offers the following functionalities:

List Trains: Displays a table of train information, including train number, name, formatted arrival time (HH:MM), and platform number (if available).
Add Train: Guides users through adding a new train record to the database, prompting for train number (mandatory), name (optional), arrival time (HH:MM format, optional), arrival date (YYYY-MM-DD format, optional), and platform number (optional). Input validation ensures that the mandatory train number is provided and not empty.
Show Train Details: Allows users to search for a specific train by its number. If found, it displays all available details about that train.
Delete Train: Enables users to remove a train record from the database by entering its number. Confirmation is requested before deletion.
Key Features:

User-friendly menu-driven interface for easy navigation.
Input validation to ensure data integrity.
Clear error messages to guide users.
Option to manage arrival time and date (can be customized as needed).
