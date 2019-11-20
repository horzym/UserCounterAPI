# UserCounterAPI
Docker + Django + RestAPI
_____________________
To run this app You should have Docker and Docker-Compose on Machine. 
After install Docker && Docker-Compose You can run app by using the following command:
  ```
  cd UserCounterAPI/
  docker-compose up
  ```
  
  
 Next go to fallowing URL:
  ```
  localhost:8000/api/user/id/counter
  ```
 * where 'id' is number between 1 and 65535
 
 Rate Limiter: 5 request / second
 
 
 To run test use:
 ```
 docker-compose run app sh -c "python manage.py test && flake8"
 ```
 
 
