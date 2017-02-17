# NTLM-adapter

A small microservice to get data from NTLM source.

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
    "image": "sesambuild/ntlm-adapter:latest",
    "port": 5001
  }
}
```
