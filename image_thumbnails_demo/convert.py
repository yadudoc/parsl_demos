from parsl import *
import os
from os.path import abspath
import argparse

dfk = DataFlowKernel(ThreadPoolExecutor(max_workers=8))

@App('python', dfk)
def process_image(photo, outputdir):
    """ Process an image file.
    """
    import os
    import subprocess
    max_xdim = 260

    print("Photo : ", photo)
    photo_info = subprocess.Popen(["identify", photo], stdout=subprocess.PIPE)
    (myout, myerr) = photo_info.communicate()
    if myerr:
        print("error from the ImageMagick identify routine: %s" % (myerr.decode('ascii')))
    myidentify = myout.decode('ascii').split(' ')
    dims = myidentify[2]
    xdim, ydim = dims.split('x')
    xdim = int(xdim)
    ydim = int(ydim)

    while xdim > max_xdim:
        xdim /= 2
        ydim /= 2

    mygeom = str(xdim)+'x'+str(ydim)
    myoutputfile = outputdir + '/thumb.' + os.path.basename(photo)
    myconvert = subprocess.run(["convert", "-geometry", mygeom, photo, myoutputfile])
    return myconvert


if __name__ == '__main__':

    parser   = argparse.ArgumentParser()
    parser.add_argument("-s", "--sourcedir", default='./pics', help="Folder containing the full size images")
    parser.add_argument("-o", "--outdir", default='./pics', help="Folder to drop outputs into")
    args   = parser.parse_args()

    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    for foto in os.listdir(args.sourcedir):
        fotopath = abspath(args.sourcedir + '/' + foto)
        process_image(fotopath, args.outdir)
        print(fotopath)



