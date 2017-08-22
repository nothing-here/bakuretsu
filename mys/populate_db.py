import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mys.settings")

import django
django.setup()

from l.models import ImageDetails, ImageTag
from django.utils import timezone

#---------------------------------------------------------------
# MAIN
#---------------------------------------------------------------

def main():

    img_base_path = r'/home/michael/Desktop/site_test/mys/static/l/'
    cfg_path = r'/home/michael/Desktop/site_test/mys/scripts/lcfg.csv'
    cfg_file = open(cfg_path,'r');
    attributes = []
    entries = []
    
    attributes_str = cfg_file.readline()
    
    d = ImageDetails.objects.all()
    d.delete()
    
    for line in cfg_file:
        tags = []
    
        parsed_csv = line.split(',')
        for value in parsed_csv:
            value = value.strip()
    
        pad_array(parsed_csv,3)
    
        tags = parsed_csv[2].split('|')
        for tag in tags:
            tag = tag.strip()

        # create ImageDetails entry
        ImageDetails_entry = ImageDetails(image_name = parsed_csv[0],
                                           char_names = parsed_csv[1],
                                           time_added = timezone.now(),
                                           path = parsed_csv[0])
        ImageDetails_entry.save()

        # create Associated ImageTag
        for tag in tags:
            ImageTag_entry = ImageTag(image_id = ImageDetails_entry,
                                       tag = tag)
            ImageTag_entry.save()
        
    print(ImageDetails.objects.all())
    print(ImageTag.objects.all())
    
    sys.exit(0)
    
#----------------------------------------------------------------
# HELPER FUNCTIONS
#----------------------------------------------------------------

def pad_array(array, padded_array_len):
    """
    Description: Takes an array and pads it to padded_array_len with empty strings.
                 If array is already has more elements than padded_array_len, function throws error.
    
    Arg Defs:
        - array                targetted array
        - padded_array_len     length to pad targetted array up to
    """

    array_len = len(array)
    
    # check length
    if(array_len > padded_array_len):
        raise ErrorName("InvalidArraySize")

    pad_len = padded_array_len - array_len

    for i in range(pad_len):
        array.append("")

    return(array)

#------------------------------------------------------------------
# RUN
#------------------------------------------------------------------

if __name__ == "__main__":
    main()
