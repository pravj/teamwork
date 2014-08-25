teamwork
========

> Organization's Contribution DashBoard : GitHub Data Challenge 3

####What

> Contributions activity Dashboard application for GitHub organizations

#### Demo

> for Demo, please wait for us to complete our monday classes :grin:

####current features

* contribution calendar for entire organization (as GitHub provides per user)
* leaderboard of organization members according to contributions
* contribution calendar for a member in an organization
* leaderboard of repositories according to number of commits

####How to setup

* clone the repository `git clone git@github.com:pravj/teamwork.git`
* use `pip` to install the denedencies `sudo pip install -r requirements.txt`
* edit your organization config at `config/teamwork.json`
* edit your bigquery config at `config/bigquery.json` [get help](#BigQuery-Help)
* setup `rethinkdb` [get help](#RethinkDB-Help)
* crawl the data for organization using `./crawl`
* analyse the data for organization using `./scan`
* start application using `python app.py`
* it should start working on `http://127.0.0.1:5000`

####How teamwork works
![How](https://raw.githubusercontent.com/pravj/teamwork/process/docs/architecture.png?token=3437250__eyJzY29wZSI6IlJhd0Jsb2I6cHJhdmovdGVhbXdvcmsvcHJvY2Vzcy9kb2NzL2FyY2hpdGVjdHVyZS5wbmciLCJleHBpcmVzIjoxNDA5NDIxOTg3fQ%3D%3D--4fe013cd04e2e29208aa128b2759b39a3d8bf419)

####Dependencies
* [Google BigQuery](https://developers.google.com/bigquery/)
  * for consumption of [GitHub Archive]() data
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
