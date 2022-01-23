**SETUP**

To run services execute PowerShell script: ```compose_containers.ps1```

****
**AVAILABLE ENDPOINTS FOR API SERVICE**
* ```/docs/``` - API docs
* ```/shema/```- Open API Schema
* ```/api/``` 
  * ```GET```: list of ```datapoint```s data. Optional URL parameters to filter 
  ```timestamp``` ranges: ```from```, ```to```. 
  * ```POST```: create ```datapoint```s entries from array of JSON objects.
* ```/api/<datapoint_name>/``` - Get aggregated values for specific ```datapoint```. Optional URL parameters to filter 
```timestamp``` ranges: ```from```, ```to```.
* ```/api/check-api-status/``` - Check if API is working
* ****
**AVAILABLE ENDPOINTS FOR CALCULATION SERVICE**
* ```/docs/``` - API docs
* ```/shema/``` - Open API Schema
* ```/api/aggregate-data/``` 
  * ```POST``` Aggregate values into ```sum``` and ```avg```
