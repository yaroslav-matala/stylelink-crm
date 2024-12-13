# Stylelink - Simple Client Manager

![Am I Responsive Design](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/amiresponsive.png)

### Overview

This project is a client management web application built with Django. It allows users to add, view, update, and delete client information in a secure and organized manner. The app includes a dashboard where users can manage their clients, search through records, and paginate results. The project is designed to be intuitive and user-friendly, with a focus on accessibility and responsive design. It incorporates authentication, ensuring that only authorized users can access their own data.

The app will be deployed on Heroku, making it accessible to users from anywhere. Future updates include the addition of a walkthrough guide for new users, as well as additional features to improve usability.

### Site User and Goal

- **Target Users**:  
  The primary users of this site are individuals or businesses that need to manage client information, such as small business owners, consultants, and freelancers. The system is designed to be simple enough for non-technical users while providing powerful features for managing client records.

- **Goal**:  
  The goal of this project is to provide a straightforward, secure, and efficient way for users to manage their clients' information. It aims to streamline the process of adding, updating, and deleting client records while ensuring data privacy and security. Additionally, the application will evolve to include a user-friendly walkthrough guide to assist users in navigating the platform with ease.

## Table of Contents
1. [User Experience Design](#user-experience-design)
2. [Features](#features)
3. [Database planning](#database-planning)
4. [Agile Development](#agile-development)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Future Features](#future-features)
8. [Technology Stack](#technology-stack)
9. [Credits](#credits)

---

## User Experience Design

### User Stories
#### As a user:
- I want to register/login securely, so my data is protected.
- I want to add new clients to the system quickly, so I can manage my contacts efficiently.
- I want to search for clients by name, so I can find specific information easily.
- I want to view my clients in a clean, intuitive layout for quick navigation.

### Wireframes
Wireframes were created using **Balsamiq** to visualize the initial design and layout for mobile, tablet, and desktop views.

![Stylelink Homepage Wireframe](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/Stylelink-Homepage.png)
![Stylelink Dahsboard Wireframe](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/Stylelink-Dashboard.png)

---

## Features

### Core Features
1. **Authentication System**  
   - Users can register, log in, and log out securely.
2. **Client Management**  
   - Add, edit, and delete client records.
3. **Responsive Design**  
   - Fully functional across all screen sizes, built using Bootstrap's Superhero theme from Bootswatch.
4. **Dashboard** 
   - The dashboard displays a list of clients with pagination, search functionality, and client details such as name, phone, location, and associated user.
5. **Search Functionality**  
   - Search for clients by name for quick access.
6. **Pagination**  
   - Ensures smooth navigation even with large data sets.
7. **Theme Switcher** 
   - Users can toggle between light and dark themes on the dashboard for a more personalized and comfortable viewing experience.

### Screenshots
#### Dashboard Page
![Dashboard Screenshot](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/dashboard.png)

#### Add Client Page
![Add Client Screenshot](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/add-client.png)  

---

## Database Planning

The application uses a relational database to store client information. The database is built using **PostgreSQL** and consists of the following tables:

# Entity Relationship Diagram (ERD)
![Entity Relationship Diagram](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/stylelink-erd.png)

## User Table
| Field         | Type      | Description                       |
|---------------|-----------|-----------------------------------|
| `id`          | Primary Key (PK) | Auto-generated unique identifier |
| `username`    | String    | Username of the user              |
| `password`    | String    | Password for the user             |
| `email`       | String    | Email of the user                 |
| `date_joined` | DateTime | Date the user registered          |

## Client Table
| Field         | Type      | Description                              |
|---------------|-----------|------------------------------------------|
| `id`          | Primary Key (PK) | Auto-generated unique identifier        |
| `user`        | Foreign Key (FK) | References `User` table (One-to-Many)    |
| `name`        | String    | Name of the client                       |
| `phone`       | String    | Phone number of the client (optional)    |
| `email`       | String    | Email of the client (optional)           |
| `location`    | String    | Location of the client (optional)        |
| `formula`     | Text      | Formula stored here (optional)           |
| `notes`       | Text      | Additional notes or comments (optional)  |
| `price`       | Decimal   | Price associated with client (optional)  |
| `created_at`  | DateTime  | Date the client was created              |
| `updated_at`  | DateTime  | Date the client was last updated         |

## Relationship:
- **One-to-Many**: A `User` can have many `Clients`, but each `Client` is associated with exactly one `User`.

#### Database Relationships

- **User-Client Relationship**: The `Client` model has a foreign key linking to the `User` model. This ensures that clients are associated with specific users, and users can only access and manage their own client data.
  
#### Indexing

- **Client Name Index**: An index is applied to the `name` field for faster search and filtering of client names in the dashboard.

#### Data Integrity

- **Validation**: The application performs validation checks to ensure data integrity, such as ensuring that all required fields (name, phone, etc.) are provided when creating or updating client records.
- **Cascade Deletion**: When a user is deleted from the system, all related client records will also be deleted to maintain referential integrity.

#### Database Migration

Django’s built-in migration system will be used to create and manage the database schema. This allows for easy version control of the database and ensures that changes to the models are automatically reflected in the database structure.

---

## Agile Development

### Project Board
The development process followed Agile methodologies. The [Project Board](https://github.com/users/yaroslav-matala/projects/5) on GitHub was used to track tasks, progress, and deliverables.  

---

## Testing

### Manual Testing
#### Features Tested:
- Authentication: Successful registration, login, and logout flows.
- Client Management: Adding, editing, and deleting clients works as expected.
- Search Functionality: Accurate results for valid searches and appropriate feedback for no results.
- Responsive Design: Tested on Chrome DevTools, mobile devices, and desktop screens.

#### HOME PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure the home page loads correctly without errors.    | Pass   |
| Verify that unauthenticated users see the correct UI.   | Pass   |
| Confirm redirection to the dashboard for logged-in users. | Pass   |

#### DASHBOARD PAGE

| Test Description                                         | Result |
|----------------------------------------------------------|--------|
| Ensure the dashboard page loads correctly for logged-in users. | Pass   |
| Verify pagination works as expected.                    | Pass   |
| Test search functionality filters results accurately.   | Pass   |
| Confirm unauthorized access redirects to the login page. | Pass   |

#### ADD CLIENT PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure the add client form renders correctly.           | Pass   |
| Verify a valid form submission saves the client.        | Pass   |
| Test that unauthorized users are redirected to the login page. | Pass   |
| Check form validation works for invalid input.          | Pass   |

#### UPDATE CLIENT PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure the update client form loads with prefilled data. | Pass   |
| Verify updates are saved correctly.                     | Pass   |
| Test that unauthorized users cannot access this page.   | Pass   |
| Confirm error handling for invalid client IDs.          | Pass   |

#### VIEW CLIENT PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure client details are displayed accurately.         | Pass   |
| Test that unauthorized users cannot access this page.   | Pass   |
| Verify error handling for non-existent client IDs.      | Pass   |

#### DELETE CLIENT FUNCTIONALITY

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure a client is deleted successfully upon confirmation. | Pass   |
| Verify unauthorized users cannot delete clients.        | Pass   |
| Confirm proper redirection to the dashboard after deletion. | Pass   |

#### LOGIN PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure the login page renders correctly.                | Pass   |
| Verify valid user credentials successfully log in the user. | Pass   |
| Test invalid credentials display an error message.      | Pass   |
| Confirm authenticated users are redirected to the dashboard. | Pass   |

#### REGISTRATION PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure the registration form renders correctly.         | Pass   |
| Verify valid form submissions create a new user account. | Pass   |
| Test invalid inputs display appropriate error messages. | Pass   |
| Confirm new users can log in immediately after registration. | Pass   |

#### LOGOUT FUNCTIONALITY

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure users are logged out successfully.               | Pass   |
| Verify logged-out users are redirected to the home page. | Pass   |
| Test that logged-out users cannot access restricted pages. | Pass   |

#### SECURITY

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Verify all pages requiring authentication redirect unauthorized users to the login page. | Pass   |
| Ensure sensitive actions (e.g., adding, updating, or deleting clients) are protected. | Pass   |
| Test error handling for unexpected inputs or actions.   | Pass   |
| Confirm no sensitive information is exposed to unauthorized users. | Pass   |

## Screenshots
#### Successful Client Addition
![Test Add Client Screenshot](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/client-added-successfully.png)  

#### Mobile Responsiveness
![Responsive Test Screenshot](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/dashboard-responsive.png)  

---

## Deployment

### Steps for Deployment
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stylelink.git
   ```

2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

3.	Run migrations:
  ```bash
  python manage.py migrate
  ```

4. Start the development server:
  ```bash
  python manage.py runserver
  ```
5. Access the app locally at http://127.0.0.1:8000

For live deployment, the project is hosted on **Heroku** at: [Live Site.](https://stylelink-7c53adcbe9a8.herokuapp.com/)

---

## Future Features

- **Help Button with Walkthrough Guide**  
  A "Help" button will be added to the dashboard page. When clicked, it will activate a step-by-step walkthrough guide on the screen to help users navigate through the features of the app. This guide will highlight key areas of the dashboard, such as adding clients, searching, and pagination, providing useful instructions for new users and those needing assistance.

---

## Technology Stack

This project utilizes the following technologies:

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **HTML5**: The latest version of the HTML standard for structuring web content.
- **CSS3**: The latest version of the CSS standard for styling web pages.
- **JavaScript**: A programming language used to make web pages interactive.
- **Bootstrap**: A popular front-end framework for building responsive, mobile-first websites. This project uses the **Bootswatch Superhero** theme.
- **PostgreSQL**: A powerful, open-source relational database management system used to store client data.
- **Heroku**: A platform-as-a-service (PaaS) that is used to deploy and run the web application.
- **Git**: Version control for source code management.
- **GitHub**: A platform for hosting and collaborating on code, used to store the project repository.

---

## Known Bugs

### Issue with Allauth Signup Page

- **Description**: The password hint section in the Allauth signup page includes an `<ul>` tag nested inside a `<small>` tag. This structure does not pass HTML validation, as the `<ul>` element is not allowed as a child of the `<small>` element.
  
- **Impact**: While this does not break the functionality of the signup page, it does result in HTML validation errors.

- **Potential Solution**: A possible fix would involve overriding the Allauth signup template and adjusting the structure to ensure the `<ul>` tag is placed outside of the `<small>` tag or replaced with a semantically valid alternative.

- **Status**: This issue is currently under review and will be addressed in a future update.

If you encounter this bug, feel free to open an issue or suggest a solution in the repository.

---

## Credits

### Tutorials and Code Resources
- This project is inspired by the tutorial: [Build a Django Client Manager](https://www.youtube.com/watch?v=pqWyUAT38e0) by Traversy Media.

### Images
- Images used in the project were sourced from **[Pexels](https://www.pexels.com)** and **[Pixabay](https://pixabay.com)**.

### Facilitators and Support
- **David Calikes** - Facilitator. His guidance and support were essential throughout the project.
- **Stephen Bevan** - Coursemate. His support during development was crucial and highly appreciated.
- **Kevin Loughrey** - Program Coding Coach. His expertise greatly influenced the project’s success.
- **John Rearden** - Program Coding Coach. Assisted with technical issues, ensuring a smooth workflow. 

### Framework and Themes
- The project uses the **Superhero theme** from **[Bootswatch](https://bootswatch.com)**, providing a clean and professional design.

---