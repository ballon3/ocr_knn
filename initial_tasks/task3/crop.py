from PIL import Image
import os

def crop_image(input_image, output_image, start_x, start_y, width, height):
    '''Crops an image given the x,y coordinates as well as width and height. Intended for the use of cropping camera temperatures'''
    input_img = Image.open(input_image)
    box = (start_x, start_y, start_x + width, start_y + height)
    output_img = input_img.crop(box)
    output_img.save(output_image)


def invert(image):
    pic = Image.open(image)
    inverted = Image.eval(pic, lambda (x): 255 - x)
    inverted.save(str(image))



# invert("output.jpg"

                                            ##CAMERA 4##
# crop_image("/home/andy/training/new_cam/MFDC0070.JPG", "output.jpg", 825, 1445, 145, 70)

                                            ##CAMERA 3##
# crop_image(os.getcwd() + "/testimages/windmill14_2327.JPG", "output.jpg", 790, 2355, 375, 70)


                                            ##CAMERA 1##
#crop_image(os.getcwd()+"/sample_images/BoneT_2014-06-04_17_56_53_1881.JPG","hunnid", 800, 2350, 100, 95)#<-- 100 F
#crop_image(os.getcwd()+"/sample_images/BoneT_2014-06-05_16_06_03_2009.JPG","outpu", 795 + 35, 2350 + 15, 35, 55)
#crop_image(os.getcwd() + "/sample_images/BoneT_2014-06-05_16_19_08_2016.JPG", "train_digits2/8", 795+35, 2350+15, 35, 55)<--right
#crop_image(os.getcwd()+"/sample_images/BoneT_2014-06-05_09_44_07_1911.JPG","output", 750, 2350, 115, 95)<--both
#crop_image(os.getcwd() + "/sample_images/BoneT_2014-06-05_16_19_08_2016.JPG", "train_digits2/output", 795, 2350+15, 38, 55)<left

                                            ##CAMERA 2##
#crop_image(os.getcwd()+"/sample_images/Main_2015-01-18_08_52_23_114.JPG","output", 1750, 0, 80, 30) -->  both digits
#crop_image(os.getcwd() + "/sample_images/Main_2015-01-18_08_52_23_114.JPG", "output", 1755, 0, 38, 30) -->  left digit
#crop_image(os.getcwd() + "/sample_images/Main_2015-01-18_08_52_23_114.JPG", "output", 1755 + 35, 0, 38, 30) --> right didit
                                           ##CAMERA 2.5##
# crop_image("/home/andy/images/windmill16_div0_0284.JPG","output.jpg", 1850, 0, 105, 30)

def crop_ratio(image, output):
    im = Image.open(image)
    width = im.size[0]
    height = im.size[1]
    crop_image(image, output, 0, 50, width, height-120)


def loop(folder):
    """recursively loops and crops through a directory of images"""
    for image in os.listdir(folder):
        crop_ratio(folder+image, "/home/andy/images/cropped/Empty/"+image)

def rename(folder,tick, tock, myclass):
    "loops through a folder to rename every item in it, tick = start, tock = stop"
    count = tick
    for item in range(tick, tock+1):
        os.rename("{}/{}.jpg".format(folder,count), "/home/andy/run1/{}/{}.jpg".format(myclass,str(count)))
        count +=1

# loop("/home/andy/training/ocr_knn/master_training/empty/")

