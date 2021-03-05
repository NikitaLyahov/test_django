# Test Django


## Initialize project

To run the server up:
```bash
make run
```

You have to apply migrations to the database:
```bash
make migrate
```

You have to initialize data to the database:
```bash
make db-init
```

You have to collect static for django admin dashboard:
```bash
make collectstatic
```

You have to create super user for django admin dashboard:
```bash
make create-admin
```


## Additional commands

To get inside the container:
```bash
make shell
```

To check code by linters:
```bash
make run-linters
```


## Links

You could open the [django admin dashboard](http://127.0.0.1:8000/admin/) 
and [test view](http://127.0.0.1:8000/test_view/).
