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
    
    attributes_str = cfg_file.readline()
    
    d = ImageDetails.objects.all()
    d.delete()
    
    for line in cfg_file:
        tags = []
    
        parsed_csv = line.split(',')
        for i in range(0,len(parsed_csv)):
            parsed_csv[i] = parsed_csv[i].strip()
    
        tags = parsed_csv[4].split('|')
        for i in range(0,len(tags)):
            tags[i] = tags[i].strip()

        # create ImageDetails entry
        ImageDetails_entry = ImageDetails(title = parsed_csv[0],
                                          author = parsed_csv[1],
                                          description = parsed_csv[2],
                                          char_names = parsed_csv[3],
                                          time_added = timezone.now(),
                                          path = parsed_csv[0] + '.png')
        ImageDetails_entry.save()

        # create Associated ImageTag
        for tag in tags:
            print('adding tag to db: ' + tag)
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
