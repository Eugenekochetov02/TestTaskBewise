# TestTaskBewise

This is a test task, the meaning of which is to access one REST service and save the result in the database.

## Stack

 - Python3
 - FastAPI
 - SQLAlchemy
 - PostgreSQL
 - AIOHTTP
 ## Major changes
 I used Unix Timestamp time instead of UTC. 
 ## Preparation
 ### apt
 ```bash
sudo apt-get install docker docker-compose
```
### pacman
 ```bash
sudo pacman -S docker docker-compose
```
 ## Examples of using
```bash
git clone git@github.com:Eugenekochetov02/TestTaskBewise.git
cd TestTaskBewise
sudo docker-compose up
```
## Result
![POST request](/readme/post.png)
![Pgadmin](/readme/pg4.png)