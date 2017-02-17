# NTLM-adapter

A small microservice to get data from NTLM source.

##### Example configuration:

```
{
  "_id": "ntlm-adapter",
  "type": "system:microservice",
  "docker": {
    "environment": {
      "pass": "thePassword",
      "url": "theURl",
      "user": "DOMAIN\\username"
    },
    "image": "sesambuild/ntlm-adapter:latest",
    "port": 5001
  }
}
```
