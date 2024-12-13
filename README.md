# Stylelink - Simple Client Manager

![Am I Responsive Design](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/amiresponsive.png)

## Table of Contents
1. [User Experience Design](#user-experience-design)
2. [Features](#features)
3. [Agile Development](#agile-development)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)

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

---

## Features

### Core Features
1. **Authentication System**  
   - Users can register, log in, and log out securely.
2. **Client Management**  
   - Add, edit, and delete client records.
3. **Responsive Design**  
   - Fully functional across all screen sizes, built using Bootstrap's Superhero theme from Bootswatch.
4. **Search Functionality**  
   - Search for clients by name for quick access.
5. **Pagination**  
   - Ensures smooth navigation even with large data sets.

### Screenshots
#### Dashboard Page
![Dashboard Screenshot](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/dashboard.png)

#### Add Client Page
![Add Client Screenshot](https://github.com/yaroslav-matala/stylelink-crm/blob/main/static/readme_images/add-client.png)  

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

### HOME PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure the home page loads correctly without errors.    | Pass   |
| Verify that unauthenticated users see the correct UI.   | Pass   |
| Confirm redirection to the dashboard for logged-in users. | Pass   |

### DASHBOARD PAGE

| Test Description                                         | Result |
|----------------------------------------------------------|--------|
| Ensure the dashboard page loads correctly for logged-in users. | Pass   |
| Verify pagination works as expected.                    | Pass   |
| Test search functionality filters results accurately.   | Pass   |
| Confirm unauthorized access redirects to the login page. | Pass   |

### ADD CLIENT PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure the add client form renders correctly.           | Pass   |
| Verify a valid form submission saves the client.        | Pass   |
| Test that unauthorized users are redirected to the login page. | Pass   |
| Check form validation works for invalid input.          | Pass   |

### UPDATE CLIENT PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure the update client form loads with prefilled data. | Pass   |
| Verify updates are saved correctly.                     | Pass   |
| Test that unauthorized users cannot access this page.   | Pass   |
| Confirm error handling for invalid client IDs.          | Pass   |

### VIEW CLIENT PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure client details are displayed accurately.         | Pass   |
| Test that unauthorized users cannot access this page.   | Pass   |
| Verify error handling for non-existent client IDs.      | Pass   |

### DELETE CLIENT FUNCTIONALITY

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure a client is deleted successfully upon confirmation. | Pass   |
| Verify unauthorized users cannot delete clients.        | Pass   |
| Confirm proper redirection to the dashboard after deletion. | Pass   |

### LOGIN PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure the login page renders correctly.                | Pass   |
| Verify valid user credentials successfully log in the user. | Pass   |
| Test invalid credentials display an error message.      | Pass   |
| Confirm authenticated users are redirected to the dashboard. | Pass   |

### REGISTRATION PAGE

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure the registration form renders correctly.         | Pass   |
| Verify valid form submissions create a new user account. | Pass   |
| Test invalid inputs display appropriate error messages. | Pass   |
| Confirm new users can log in immediately after registration. | Pass   |

### LOGOUT FUNCTIONALITY

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Ensure users are logged out successfully.               | Pass   |
| Verify logged-out users are redirected to the home page. | Pass   |
| Test that logged-out users cannot access restricted pages. | Pass   |

### SECURITY

| Test Description                                        | Result |
|---------------------------------------------------------|--------|
| Verify all pages requiring authentication redirect unauthorized users to the login page. | Pass   |
| Ensure sensitive actions (e.g., adding, updating, or deleting clients) are protected. | Pass   |
| Test error handling for unexpected inputs or actions.   | Pass   |
| Confirm no sensitive information is exposed to unauthorized users. | Pass   |

### Screenshots
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