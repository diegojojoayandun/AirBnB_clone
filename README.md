# 0x00. AirBnB clone - The console

![alt text](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220228T071425Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=eea69c21402bcc63dfb86b79f5af5b3609de17338942ede06aeceeb9c137cfc4)

## Description

Team Project as part of the second trimester cicle of foundations at Holberton School, the AirBnB project approachs to the first real web developer project, the console is the first step towards building our first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

## Resources
### Read or watch:

* [Python abstract classes](https://blog.teclado.com/python-abc-abstract-base-classes/)
* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* Packages concept page
* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

# More Info

## Execution

The AirBnb Shell runs in both interactive and non interactive mode:

### Interactive
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
### Non-Interactive
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Authors

[Cristian Sánchez](https://github.com/cristaker)

[Diego Fernando Jojoa Yandún](https://github.com/diegojojoayandun)