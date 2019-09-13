# Build
docker build --rm -t sqlserverdockerpython:latest .

# Run
docker run  -v $PWD/home:/home -i -t sqlserverdockerpython /bin/bash

---
# The Config.ini file
It should look like:
```ini
[db]
server =xxx.database.windows.net
database = xxx
username = xxx
password = xxx
```