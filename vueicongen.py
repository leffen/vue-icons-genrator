#!/usr/local/bin/python3

from PIL import Image
import sys, getopt,pathlib,os.path


def gen_icons(srcImage,destDir):

  path = pathlib.Path(destDir)
  path.mkdir(parents=True, exist_ok=True)

  # img link
  img = Image.open(srcImage)
  dimensions = [192,512,192,512,60,76,120,152,180,16,32,144,150]
  names = ['android-chrome-','android-chrome-','android-chrome-maskable-','android-chrome-maskable-','apple-touch-icon-','apple-touch-icon-','apple-touch-icon-','apple-touch-icon-','apple-touch-icon-','favicon-','favicon-','msapplication-icon-','mstile-']

  for i in range(0,13):
    newsize = (dimensions[i],dimensions[i])
    img_resize = img.resize(newsize)
    img_resize.save(f'{destDir}/{names[i]}{dimensions[i]}x{dimensions[i]}.png')


  img = Image.open(srcImage)
  newsize = (60,60)
  img_resize = img.resize(newsize)
  img_resize.save(f'{destDir}/apple-touch-icon.png')

  img_converted = '%s/favicon.ico' % destDir
  img_resize = img.resize((48, 48))
  img_resize.save(img_converted)


def main(argv):
   inputfile = ''
   outputdir = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputdir>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputdir>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputdir = arg
   print('Input=', inputfile)
   print('OutputDir=', outputdir)

   if not os.path.exists(inputfile):
     print(f'Inputfile {inputfile} do not exist')
     os.sys.exit(-1)

   gen_icons(inputfile,outputdir)



if __name__ == "__main__":
   main(sys.argv[1:])