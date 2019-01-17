import argparse
import tarfile
import zipfile

parser=argparse.ArgumentParser()
parser.add_argument('--f', '--sourcefilePath', required=True, dest='filePath', type=str, help="file path to be extracted ")
parser.add_argument('destination',type= str )
args=parser.parse_args()
filePath=args.filePath

destPath = args.destination

if (filePath.endswith("tar.gz")):
    tar = tarfile.open(filePath, "r:gz")
    tar.extractall(destPath)
    tar.close()
elif (filePath.endswith("tar")):
    tar = tarfile.open(filePath, "r:")
    tar.extractall(destPath)
    tar.close()
else:
    zip = zipfile.ZipFile(filePath)
    zip.extractall(destPath)
