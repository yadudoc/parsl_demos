Image thumbnails demo
=====================

A quick demo to demonstating Parsl converting images to thumbnails in a directory.

Requirements:
-------------

* Python3.5
* Parsl::

    pip3 install parsl

* ImageMagick::

    apt-get install imagemagick


How to run
----------

* First make sure to download the images listed in image_sources.txt to the pics folder::

    mkdir pics
    cd pics
    cat ../image_sources.txt | xargs wget

* Run the script::

    python3 convert.py
