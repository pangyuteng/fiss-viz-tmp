# https://stackoverflow.com/questions/60024404/how-to-change-the-orientation-of-simpleitk-image-in-python

import os,sys
import SimpleITK as sitk

if __name__ == "__main__":

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    spacing = (1.,1.,1.)
    origin = (0.,0.,0.)
    direction = (1.,0.,0.,0.,1.,0.,0.,0.,1.)

    # consider resamling image to 1,1,1
    # then crop middle slab
    
    reader= sitk.ImageFileReader()
    reader.SetFileName(input_file)
    img = reader.Execute()
    img.SetSpacing(spacing)
    img.SetOrigin(origin)
    img.SetDirection(direction)
    writer = sitk.ImageFileWriter()
    
    writer.SetFileName(output_file)
    writer.Execute(img)