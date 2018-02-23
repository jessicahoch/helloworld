# helloworld

### Installation 
Clone the repo and use pip to install it. 
```bash
git clone https://github.com/programming-for-bio/helloworld.git
cd helloworld/
pip install .
```

### CLI Usage 
To use the executable helloworld command line program:
```
$ helloworld -h
usage: helloworld [-h] [-n NAME] [--howlong] [--countdown]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  optional name to say hello to
  --howlong             print days until Darwin's next birthday
  --countdown           print predicted days until end of the world
```


### API Usage
To use the helloworld Python API:
```python
import helloworld
helloworld.helloworld(name="Jess")
```

```
hello Jess
```
