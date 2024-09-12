# Role-Based Redirect Web App (Sample)


This project consists of two Flask applications: a **main app** and a **pages app**. Both are containerized using Docker, allowing you to easily spin up the apps without worrying about your local environment.

### Prerequisites

- [Docker](https://www.docker.com/) must be installed and running on your machine.

### Docker Setup for Main App

The main app runs on port `5500` and has routes for role-based access (`/it` and `/hr`). Follow these steps to spin it up:

1. Clone the repository and navigate to the project directory.
2. Build the Docker image:

   ```bash
   docker build -t main-app .
   ```

3. Run the Docker container:

   ```bash
   docker run -d -p 80:5500 --name main-app -e URL='localhost' main-app
   ```

   This command does the following:
   - **`-d`** runs the container in detached mode.
   - **`-p 80:5500`** maps port http 80 of the container to port 5500 on your host machine.
   - **`-e URL='localhost'`** sets the `URL` environment variable (you can modify this as needed). Use a public URL if the application's DNS is exposed on the Internet

4. Access the app in your browser at `http://localhost` or `https://app.your-domain.com`. You will see a homepage with links to the `/it` and `/hr` spaces.

### Docker Setup for Page App

The sub app serves pages based on roles (`IT` or `HR`) and runs on port `5600`.

1. Navigate to the sub-app directory (if separate), or use the same project directory.
2. Build the Docker image for the sub app:

   ```bash
   docker build -t page-app .
   ```

3. Run the Docker container for the IT app:

   ```bash
   docker run -d -p 5600:5600 -e ROLE='IT' --name it-app -e PORT=5600 page-app
   ```
4. Run the Docker container for the HR app:

    ```bash
   docker run -d -p 5700:5600 -e ROLE='HR' -e --name hr-app PORT=5700 page-app
   ```

   This command:
   - **`-d`** runs the container in detached mode.
   - **`-p 5600:5600`** maps port 5600 of the container to port 5600 on your host machine.
   - **`-e ROLE='IT'`** sets the `ROLE` environment variable (change it to `'HR'` for the HR page). And runs 2 apps simultaneously based on the same docker image.  
   - **`-e PORT=5600`** sets the port (you can modify this if necessary).

4. Access the sub apps in your browser at `http://localhost:5600` or `https://app.your-domain.com/IT`. It will display content based on the role set in the environment variable.

