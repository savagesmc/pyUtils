import os
import fileUtils

def getHashes(rootPath):
   result = dict()
   files = fileUtils.recurse(rootPath)
   for f in files:
      md5 = fileUtils.md5(f)
      print "{:25s} : {:s}".format(md5, f)
      if md5 in result:
         # replace
         l = result[md5]
         l.append(f)
         result[md5] = l
      else:
         l = []
         l.append(f)
         result[md5] = l
   return result

if __name__ == "__main__":
   hashes = getHashes(os.getcwd())
   with open("dupResults.txt", "w") as of:
      for k in hashes:
         items = hashes[k]
         if len(items) > 1:
            print "{:s}:".format(k)
            print >>of,  "{:s}:".format(k)
            for i in items:
               print "     {:s}".format(i)
               print >>of, "     {:s}".format(i)
