# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import sys

from PIL import Image, ImageCms


def convert(source_dir='.', target_dir='.', available_formats=['jpg']):
    print("converting...")
    filenames = os.listdir(source_dir)
    filenames = [filename for filename in filenames if filename.split('.')[-1] in available_formats]
    total = len(filenames)
    print("total {} files".format(total))
    for i in range(total):
        sys.stdout.write("\r%4d/%d" % (i + 1, total))
        sys.stdout.flush()
        image = Image.open(filenames[i])
        if image.mode == 'CMYK':
            image = ImageCms.profileToProfile(image, 'USWebCoatedSWOP.icc', 'sRGB Color Space Profile.icm', renderingIntent=0, outputMode='RGB')
        image.save(open(os.path.join(target_dir, filename), 'wb'))
    print("done")
