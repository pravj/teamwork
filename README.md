teamwork
========

> Organization's Contribution DashBoard : GitHub Data Challenge 3

####What

> Contributions activity Dashboard application for GitHub organizations

####current features

* contribution calendar for entire organization (as GitHub provides per user)
* leaderboard of organization members according to contributions
* contribution calendar for a member in an organization
* leaderboard of repositories according to number of commits

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
* [GitHub Webhook API](https://developer.github.com/v3/repos/hooks/) (*proposed*)
  * synchronization of new activity's data
* [Retask](https://github.com/kushaldas/retask) (*proposed*)
  * Task Queue management
* *some bottles of Appy Fizz and a lot of coffee cups*
