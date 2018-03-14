<H1>Web server using python sockets</H1>

**The goal of this project:**

Create a simple python socket based web server <br>
Render DN.html if the url is correct, else return a 404 error


**Running the server:**

Run server.py using python 2.7 <br>
Open 127.0.0.1:8080/DN.html on the browser

# Setup steps for transfers project
Install following softwares:
1. [Python3](http://docs.python-guide.org/en/latest/starting/install3/osx/)
2. pip
3. [Pycharm](https://www.jetbrains.com/pycharm/)
4. [VScode](https://code.visualstudio.com/download)
5. [Postgres app](https://postgresapp.com/)
6. [datagrip](https://www.jetbrains.com/datagrip/)
7. [node.js v6.5.0](http://nodejs.org/dist/v6.5.0/node-v6.5.0.pkg)
7. [paw](https://paw.cloud/)/[postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en)
8. [git](https://git-scm.com/downloads)
9. browsers (firefox and chrome)

## Install Virtual Environment
`pip3 install virtualenv`

## Set up Database
Open postgres in terminal and run following commands
`drop database if exists transfer;`<br/>
`drop user if exists transfer;`<br/>
`create user transfer with login password 'transfer';`<br/>
`create database transfer with encoding 'UTF8' lc_ctype 'en_US.UTF-8' lc_collate 'en_US.UTF-8' template template0;`<br/>
`grant all privileges on database transfer to transfer;`<br/>
`\connect transfer;`<br/>
`create extension if not exists hstore schema pg_catalog;`<br/>
`create extension if not exists pg_trgm schema pg_catalog;`<br/>
`\connect template1;`<br/>
`create extension if not exists hstore schema pg_catalog;`<br/>
`create extension if not exists pg_trgm schema pg_catalog;`<br/>
`alter user transfer createdb;`<br/>
`\c transfer`<br/>
`create extension if not exists fuzzystrmatch schema pg_catalog;`<br/>
download files: [wichita_exam_articulations.sql](https://eab.box.com/s/qtxk4669lv0p02p40x6rlv45sr325ar6) [wichita_course_articulations.sql](https://eab.box.com/s/opaffnbt8w3mnosi9lgbtoqbarmv4qec)<br/>
`psql $DATABASE_URL < ~/Downloads/wichita_exam_articulations.sql`<br/>
`psql $DATABASE_URL < ~/Downloads/wichita_course_articulations.sql`<br/>

## Set up Janus
`git clone https://github.com/advisory/janus`<br/>
`python3 -m venv ~/venvs/janus`<br/>
`source ~/venvs/janus/bin/activate`<br/>
`pip install -r requirements/local.txt`<br/>
[Add ssh keys](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) (if not done previously)<br/>
After setting up database and Barabar, run the following command<br/>
`python manage.py dev_init`<br/>

## Set up Barabar
`git clone https://github.com/advisory/barabar`<br/>
`cd barabar/`<br/>
`python3 -m venv ~/venvs/barabar`<br/>
`source ~/venvs/barabar/bin/activate`<br/>
`pip install -r requirements.txt`<br/>
Add lines to ~/.bashrc ([link](https://eab.box.com/s/halxcj3l2h8kadi3axskn77iw5y7ru9d))<br/>
`python manage.py db create_schema wichita_10096`<br/>

## Set up [Janus-UI](https://repo.advisory.com/projects/EAB/repos/janus-ui/browse/web)
To get the clone url, open above link and click on download icon<br/>
`git clone` *url*<br/>
`cd janus-ui/web/`<br/>
`npm install -g n`<br/>
`sudo n 6.5.0`<br/>
`npm run build-preflight`<br/>
`PATH=./node_modules/.bin/:$PATH gulp watch --target local`<br/>

## Run the project
Add following line to /etc/hosts<br/>
`127.0.0.1       planet-express`<br/>
Open Janus and barabar in PyCharm<br/>
##### for janus:
click on 'Edit configuration'
* add environment variables ([link](https://eab.box.com/s/trvehdiw31di6nx47165ctwd9ca5f6ub))
* click on Pycharm
* Select Preferences
* select Project: janus
* select Project Interpreter
* click drop down menu and select "show all"
* click on add symbol in the bottom
* select existing environment
* select browse next to interpreter
* navigate to venvs/janus/bin/python3
* click on run
##### For barabar:
click on 'Edit configuration'
* add environment variables ([link](https://eab.box.com/s/z2z7bzlzway1ai2i5awlyo5r1lisqf22))
* click on Pycharm
* Select Preferences
* select Project: janus
* select Project Interpreter
* click drop down menu and select "show all"
* click on add symbol in the bottom
* select existing environment
* select browse next to interpreter
* navigate to venvs/janus/bin/python3
* click on run
