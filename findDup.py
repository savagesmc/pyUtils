import os
import fileUtils

def getHashes(rootPath):
   result = dict()
   files = fileUtils.recurse(rootPath)
   badFiles = []
   for f in files:
      try:
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
      except:
         badFiles.append(f)
   return result, badFiles

if __name__ == "__main__":
   hashes, badFiles = getHashes(os.getcwd())
   with open("dupResults.txt", "w") as of:
      for k in hashes:
         items = hashes[k]
         if len(items) > 1:
            print "{:s}:".format(k)
            print >>of,  "{:s}:".format(k)
            for i in items:
               print "     {:s}".format(i)
               print >>of, "     {:s}".format(i)
      if len(badFiles):
         print >>of, "Bad Files:"
         for f in badFiles:
            print >>of, "     {:s}".format(f)
