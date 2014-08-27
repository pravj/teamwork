teamwork
========

> Organization's Contribution DashBoard : GitHub Data Challenge 3

####What

> Contributions activity Dashboard application for GitHub organizations

####inspiration

> teamwork is inspired by Twitter's Open Source Dashboard : [Twitter &hearts; Open Source](http://twitter.github.io/)

#### Demo

* you can have a look on screenshots of teamwork for [GitHub](https://github.com/github) organization (from Aug. 24, 2013 to Aug. 24, 2014)

* organization contributions
![org](https://raw.githubusercontent.com/pravj/teamwork/process/docs/org.png)

* member contributions
![member](https://raw.githubusercontent.com/pravj/teamwork/process/docs/member.png)

* members leaderboard, according to number of contributions
![members](https://raw.githubusercontent.com/pravj/teamwork/process/docs/members.png)

* repository leaderboard, according to number of contributions
![repos](https://raw.githubusercontent.com/pravj/teamwork/process/docs/repos.png)


####current features

* contribution calendar for entire organization (as GitHub provides per user)
* leaderboard of organization members according to contributions
* contribution calendar for a member in an organization
* leaderboard of repositories according to number of commits

####How to setup

* clone the repository `git clone git@github.com:pravj/teamwork.git`
* use `pip` to install the denedencies `sudo pip install -r requirements.txt`
* copy `config/teamwork.sample.json` to `config/teamwork.json` and edit it.
* copy `config/bigquery.sample.json` as `config/bigquery.json` and edit it [see help section](#bigquery-help)
* setup `rethinkdb` [see help section](#rethinkdb-help)
* crawl the data for organization using `./crawl`
* analyse the data for organization using `./scan`
* start application using `python app.py`
* it should start working on `http://127.0.0.1:5000`
* **setup cronjob** *(optional)*
  * *till synchronization using GitHub webhook API is being developed, cronjob can be used for daily change*
  * *if you are choosing to do this, setup ./crawl and ./scan on cron*

####How teamwork works
![How](https://raw.githubusercontent.com/pravj/teamwork/process/docs/architecture.png?token=3437250__eyJzY29wZSI6IlJhd0Jsb2I6cHJhdmovdGVhbXdvcmsvcHJvY2Vzcy9kb2NzL2FyY2hpdGVjdHVyZS5wbmciLCJleHBpcmVzIjoxNDA5NDIxOTg3fQ%3D%3D--4fe013cd04e2e29208aa128b2759b39a3d8bf419)

####Dependencies
* [Google BigQuery](https://developers.google.com/bigquery/)
  * for consumption of [GitHub Archive](http://www.githubarchive.org/) data
* [BigQuery-Python](https://github.com/tylertreat/BigQuery-Python)
  * Python client for interacting with Google BigQuery
* [Requests](https://github.com/kennethreitz/requests)
  * because, *we love it*
* [RethinkDB](rethinkdb.com)
  * Database, powering the application
* [Flask](http://flask.pocoo.org/)
  * you know, for *one drop at a time*
* [Octicons](https://octicons.github.com/)
  * Project for GitHub, with GitHub's icons.
* [Hint.css](http://kushagragour.in/lab/hint/)
  * An awesome tooltip library in CSS.
* [GitHub Webhook API](https://developer.github.com/v3/repos/hooks/) (*proposed*)
  * synchronization of new activity's data
* [Retask](https://github.com/kushaldas/retask) (*proposed*)
  * Task Queue management
* *some bottles of Appy Fizz and a lot of coffee cups*

####BigQuery-Help
* create a new project on [Google Developer Console](https://console.developers.google.com/project)
* BigQuery API will be ON by default for any new project.
* Create a new Client ID for your project
  * go in `API & Auth -> APIs` section of project
  * select `Service Account` as `Application Type`
* use generated JSON to edit your bigquery config.

####RethinkDB-Help
* you need to install RethinkDB to use `teamwork`
  * get it from [here](http://rethinkdb.com/docs/install/)
* start the server
  * start RethinkDB server by running `$ rethinkdb`
* to setup RethinkDB as a cluster on system startup
  * [Create a cluster on system startup](http://rethinkdb.com/docs/cluster-on-startup/)
