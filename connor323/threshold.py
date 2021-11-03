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

    img = reader.Execute()
    print('original:')
    print('GetSize',img.GetSize())
    print('GetSpacing',img.GetSpacing())
    print('GetOrigin',img.GetOrigin())
    print('GetDirection',img.GetDirection())
    
    reader= sitk.ImageFileReader()
    reader.SetFileName(args.mask_file)
    mask_obj = reader.Execute()
    mask = sitk.GetArrayFromImage(mask_obj)

    arr = sitk.GetArrayFromImage(img).astype(float) > 0.8
    arr[mask==0]=0
    print(np.sum(arr))
    arr = arr.astype(np.uint8)
    print(np.sum(arr))
    img = sitk.GetImageFromArray(arr)

    origin = (0.,0.,0.)
    direction = (1.,0.,0.,0.,1.,0.,0.,0.,-1.)
    spacing = (1.,1.,1.)

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
