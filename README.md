#Udacity Full Stack Nanodegree

##Project: Tournament Results
This project focuses on the functionality of a website backed by a Postgres database.

### PROJECT SPECIFICATIONS
as of April 2016


Functionality

| CRITERIA | MEETS SPECIFICATIONS |
|----------|----------------------|
| Does the module pass the included unit tests? | The module passes the included unit tests. |

Table Design

| CRITERIA | MEETS SPECIFICATIONS |
|----------|----------------------|
| Do the tables have meaningful names? | Tables have meaningful names. |
| Are the tables normalized? | Tables are normalized (no redundant data, data dependancies are properly defined). |

Column Design

| CRITERIA | MEETS SPECIFICATIONS |
|----------|----------------------|
| Are the columns defined with proper data types? | Table columns have proper data types. |
| Do the columns have meaningful names? | Table columns have meaningful names. |
| Are primary and secondary keys properly defined? | Primary and secondary keys are properly defined. |

Code Quality

| CRITERIA | MEETS SPECIFICATIONS |
|----------|----------------------|
| Does the code make use of query parameters to protect against SQL injection? | Code makes use of query parameters to protect against SQL injection. |
| Is the code ready for personal review and is neatly formatted? | Code is ready for personal review and is neatly formatted. |

Comments

| CRITERIA | MEETS SPECIFICATIONS |
|----------|----------------------|
| Are comments present and effectively explain longer code procedures? | Comments are present and effectively explain longer code procedures. |

Documentation

| CRITERIA | MEETS SPECIFICATIONS |
|----------|----------------------|
| Is a README file included, detailing all steps required to successfully run the application? | A README file is included detailing all steps required to successfully run the application. |

Suggestions to Make Your Project Stand Out!

Support more than one tournament in the database, so matches do not have to be deleted between tournaments. This will require distinguishing between “a registered player” and “a player who has entered in tournament #123”, so it will require changes to the database schema.
Prevent rematches between players.

Don’t assume an even number of players. If there is an odd number of players, assign one player a “bye” (skipped round). A bye counts as a free win. A player should not receive more than one bye in a tournament.
 English 

