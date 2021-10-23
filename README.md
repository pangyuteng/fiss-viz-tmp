# fiss-viz-tmp

+ build and go into the container
```
docker build -t fiss .
docker run -it -p 8888:8888 -w /workdir -v $PWD:/workdir fiss bash

```

+ start container

```
jupyter notebook --ip=* --allow-root
```





