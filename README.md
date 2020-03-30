# db-setup-mariadb-python
Using Python to set up tables on MariaDB server

This repo provides an example of how to create a table on a mariaDB server, using a python script.

### Prerequisites 
1. Python3 installed 

2. Relational Database Server (I'm using MySQL/MariaDB)

3. An existing Database on the server.

### Creating the table
1. Clone this repository
    ```
    cd /your/favourite/directory
    git clone https://github.com/Syab/db-setup-mariadb-python
    cd db-setup-mariadb-python
    ```

2. Create a file to hold your environment variables and secrets
    ```
    # Linux systems
    touch env.profile

    #add this to your env.profile file
    #!/bin/bash

    export DBHOST="localhost" <or a valid IP to your DB>
    export DBUSER="<your user name to the db>"
    export DBPW="<your password name to your db>"
    export DBPORT="3306"  <or any exisiting port you are using>
    export DBNAME="<your existing database>"

    ```

3. Source the environment file 
    ```
    source env.profile
    ```
4. Run the python script 
    ```
    python createtable.py
    ```

5. You should have 1 table created with 4 columns :

    - _id
    - long_url
    - short_url
    - time_created

