# NTLM-adapter  

A small microservice to get data from NTLM source.


[![Build Status](https://travis-ci.org/sesam-community/sesam-ntlm-adapter.svg?branch=master)](https://travis-ci.org/sesam-community/sesam-ntlm-adapter)

##### Example configuration:

```
{
  "_id": "ntlm-adapter",
  "type": "system:microservice",
  "docker": {
    "environment": {
      "url": "theURl",
      "username": "DOMAIN\\username",
      "password": "thePassword"
    },
    "image": "sesamcommunity/ntlm-adapter:latest",
    "port": 5001
  }
}
```
