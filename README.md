# fiss-viz-tmp

+ build and go into the container
```
docker build -t test .
docker run -it -p 8888:8888 -w /workdir -v $PWD:/workdir test bash

```

+ start container

```
jupyter notebook --ip=* --allow-root
```





