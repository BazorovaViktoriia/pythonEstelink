## Installation Steps

Download or clone this repository:

```bash
git clone https://.../PageObjectPlaywright
cd PageObjectPlaywright
```

Create a virtual environment for this project/directory and Install the requirements     
```
make init
```

Run the tests
```
make tests
```

Run the tests + allure

Notice:
$JAVA_HOME must be declared to launch an Allure report server

install java first:
```bash
sudo apt install default-jdk # or default-jre
```

If you do not know the JAVA_HOME path, you can type:
```bash
update-alternatives --config java
```` 
And you should find the full java path from output but use it without /bin/java posix as <PATH> in next commands.
Set the JAVA_HOME variable in file /etc/environment by command:
```bash
sudoedit /etc/environment
```
Add single new line at the bottom of the file:
```code
 JAVA_HOME="<PATH>"
 ```` 
Example (generic): JAVA_HOME="/lib/jvm/default-java"
Notice there's no space when declaring the variable, double quotes and NO `/bin/java` at the end of <PATH>

Restart your shell for changes to take effect for all future sessions.
Or run `. /etc/environment` (This only works for the current session where you run it, not the others currently running)
To check if the variable is stored, type to verify:
```bash
echo $JAVA_HOME
```

Run tests with an Allure report:

```bash
make tests_allure or 
sh scripts/start_tests_allure.sh
```

## Docker
Build

Use the Docker command line
In the command, the -t flag tags your image with a name and the `.` lets Docker knows where it can find the Dockerfile.
```bash
  docker build -t page_object_playwright:1.0 .
  docker run --name autotests page_object_playwright:1.0
```

Build containers
```bash
docker-compose up --build -d
```

Docker images:
```bash
docker images -a
docker rmi -f <image>
```

Docker containers:
```bash
docker ps -a
docker rm -f <ID_or_NAME>
```

Prune docker system:
```bash
docker system prune -a
```