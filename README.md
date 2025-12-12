# A Demo Web App With Subpages


This project consists of two Flask applications: a **main app** and a **pages app**. Both are containerized using Docker, allowing you to easily spin up the apps without worrying about your local environment.

### Prerequisites

- [Docker](https://www.docker.com/) must be installed and running on your machine.

### Docker Setup for Main App

The main app runs on port `5500` and has routes for role-based access (`/it` and `/hr`). Follow these steps to spin it up:

1. Clone the repository and navigate to the project directory.
2. Run this in your terminal:

```bash
  docker-compose up --build -d
```

3. Once you're done or there is an update to the code:

```bash
   docker-compose down
   docker-compose up --build -d
```

4. Re-run the app:

```bash
   docker-compose up -d
```

   This command does the following:
   - **`-d`** runs the container in detached mode.
   - **`-p 80:5500`** maps port http 80 of the container to port 5500 on your host machine.

5. Access the app in your browser at `http://localhost`  You will see a homepage with links to the `/it`, `/hr`, and `/gamers` spaces.

6. More pages can be added by simple expanding the files below:
* `main.py`
* `pages.py`
* `docker-compose.yml` - add a new role to it. 
