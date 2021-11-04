
```

docker build -t connor323 .

docker run -it -w /opt/code -v $PWD:/opt/code connor323 bash
cmake .
make 

python preprocess.py image.mhd testinput.mhd

bash download.sh
python preprocess.py image.nii.gz imageP.nii.gz
./vector_region_growing imageP.nii.gz fiss_enhanced.nii.gz
./region_growing fiss_enhanced.nii.gz fiss_enhanced_refined.nii.gz
```
```
./enhance_fiss image.nii.gz out_region_grow.nii.gz out_fiss.nii.gz
python isolate.py out_fiss.nii.gz out_region_grow.nii.gz iso_mask.nii.gz out_fiss_refined.nii.gz
```
```
ref.
https://gist.github.com/pangyuteng/e942648579ebfd3c6e07c50eb81f42ac
https://github.com/Connor323/Lung-Lobes-Segmentation-in-CT-Scans

http://www.lungworkshop.org/2009/proc2008/10-brown.pdf
https://doi.org/10.1111/resp.12253
```
