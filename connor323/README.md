
```

docker build -t connor323 .

docker run -it -w /opt/code -v $PWD:/opt/code connor323 bash
cmake .
make 

python scrub_loc.py image.mhd testinput.mhd

wip: need to use gdb.

./vector_region_growing testinput.mhd fiss_enhanced.mhd
./region_growing fiss_enhanced.mhd fiss_enhanced_refined.mhd

```


```
ref.
https://gist.github.com/pangyuteng/e942648579ebfd3c6e07c50eb81f42ac
https://github.com/Connor323/Lung-Lobes-Segmentation-in-CT-Scans
```
