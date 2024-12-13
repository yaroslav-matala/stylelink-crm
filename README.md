# Stylelink - Simple Client Manager

![Am I Responsive Design]()

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

#### As an administrator:
- I want to ensure only authenticated users can access sensitive features like adding clients.
- I want to paginate results for better performance and usability.

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
![Dashboard Screenshot](#)  
*Screenshot showing the main dashboard with the client table.*

#### Add Client Page
![Add Client Screenshot](#)  
*Screenshot of the form used to add a new client.*

---

## Agile Development

### Project Board
The development process followed Agile methodologies. The [Project Board](#) on GitHub was used to track tasks, progress, and deliverables.  
(*Insert link to your GitHub project board here.*)

---

## Testing

### Manual Testing
#### Features Tested:
- Authentication: Successful registration, login, and logout flows.
- Client Management: Adding, editing, and deleting clients works as expected.
- Search Functionality: Accurate results for valid searches and appropriate feedback for no results.
- Responsive Design: Tested on Chrome DevTools, mobile devices, and desktop screens.

### Screenshots
#### Successful Client Addition
![Test Add Client Screenshot](#)  
*Screenshot of a successful client addition test.*

#### Mobile Responsiveness
![Responsive Test Screenshot](#)  
*Screenshot showing proper layout adjustments on mobile.*

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

For live deployment, the project is hosted on **Heroku** at: [Live Site.](#)

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