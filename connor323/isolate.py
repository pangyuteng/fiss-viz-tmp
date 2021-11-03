# https://stackoverflow.com/questions/60024404/how-to-change-the-orientation-of-simpleitk-image-in-python

import argparse
import os,sys
import numpy as np
import SimpleITK as sitk
import pydicom
from scipy import ndimage
from skimage import measure


if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str,help='input file path hello')
    parser.add_argument('mask_file',type=str)
    parser.add_argument('output_file', type=str,help='out file path')    
    args = parser.parse_args()
    
    reader= sitk.ImageFileReader()
    reader.SetFileName(args.input_file)


    origin = (0.,0.,0.)
    direction = (1.,0.,0.,0.,1.,0.,0.,0.,-1.)
    spacing = (1.,1.,1.)

    img = reader.Execute()
    print('original:')
    print('GetSize',img.GetSize())
    print('GetSpacing',img.GetSpacing())
    print('GetOrigin',img.GetOrigin())
    print('GetDirection',img.GetDirection())
    
    reader= sitk.ImageFileReader()
    reader.SetFileName(args.mask_file)

    writer = sitk.ImageFileWriter()
    writer.SetFileName(args.input_file)
    writer.Execute(img)

    mask_obj = reader.Execute()
    mask = sitk.GetArrayFromImage(mask_obj)

    arr = sitk.GetArrayFromImage(img).astype(float) > 0.8
    arr[mask==0]=0

    mylist = [
        ('lof',1,2),
        ('rof',[3,5],4),
        ('rhf',3,5),
    ]
    apprx_fiss=np.zeros(arr.shape)
    print(np.unique(mask))
    for name,ind0,ind1 in mylist:
        if isinstance(ind0,list):
            mask0 = np.logical_or(mask==ind0[0],mask==ind0[1])
        else:
            mask0 = mask == ind0
        mask1 = mask == ind1

        iteration = 10
        mask0 = ndimage.binary_dilation(mask0,iterations=iteration)
        mask1 = ndimage.binary_dilation(mask1,iterations=iteration)
        overlay = np.logical_and(mask0,mask1)
        print(np.sum(overlay))
        apprx_fiss[overlay==1]=1
        print(name,ind0,ind1)
        print('--') 
    
    apprx_fiss[mask==0]=0
    print(np.sum(apprx_fiss))

    print(np.sum(arr))
    arr = arr.astype(np.uint8)
    arr[apprx_fiss==0]=0
    print(np.sum(arr))
    img = sitk.GetImageFromArray(arr)


    img.SetSpacing(spacing)
    img.SetOrigin(origin)
    img.SetDirection(direction)

    print('after:')
    print('GetSize',img.GetSize())
    print('GetSpacing',img.GetSpacing())
    print('GetOrigin',img.GetOrigin())
    print('GetDirection',img.GetDirection())

    writer = sitk.ImageFileWriter()
    writer.SetFileName(args.output_file)
    writer.Execute(img)

    print('done')
