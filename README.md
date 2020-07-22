## QuickStart

* A directory structure like:

```
.
├── app
│   └── main.py
└── Dockerfile
```
* Go to the project directory (in where your `Dockerfile` is, containing your `app` directory)
* Build your Flask image:

```bash
docker build -t test:testing .
```


* Run a container based on your image:

```bash
docker run -d --name test-cont -p 80:80 test:testing
```

* Now, when you go to your Docker container URL, for example: <http://localhost>, you will see your

```
curl http://localhost
{"Accept":"*/*","Client IP":"172.17.0.1","Host":"localhost","User-Agent":"curl/7.61.1"}
```

## Docker image
```
docker pull namcx/python-flask
```
