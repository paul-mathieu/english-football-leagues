# English-football-leagues-API
 Unofficial updated English leagues and players API

### Prerequisites

You first need to install the prerequisites

```
pip3 install -r requirements.txt
```
### To run the project

Run first the file **flask-api.py** and then run the file **recherche.php** on a php server.

### Context

Many websites allow football fans to consult data on teams, players or any other type of data revolving around the world of football. However, the data present on the sites is not simply usable and rarely importable in data formats suitable for analyzes. In addition, the simple creation of a data set did not suit us because some of the data is useless and is not updated regularly, which can be problematic for performing analyzes. The goal of our program is to create a specific query to retrieve the most recent data from sites and to format it so that the user can analyze it. The main site from which we have collected data is Soccerway, a site belonging to DAZN Group. The program allows you to return data concerning teams, matches, players or leagues.
To carry out this project we formed a group of three made up of **Noah Razafindrabe**, **Paul Mathieu** and **Loïc Vieu**.

## Doing stuff in Python

The program consists of a package called footballAPI. The role of this package is to return data of type json or to import the result into a PostgreSQL database. The user enters the information they are looking for in a dictionary before making a request.
You can see sample requests in the **setup.py** file.
