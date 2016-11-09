import uuid
import os
import sys, getopt

def standardPath(line):
	line = line.replace('\\', '/').replace(projectName + '/Content', 'Game').replace('Engine/Content', 'Engine')
	lastSplit = line.rindex('/')
	assetDir = line[:lastSplit + 1]
	assetName = line[lastSplit + 1:].split('.')[0]
	index = assetDir.find('/Game')
	if index != -1:
		assetDir = assetDir[index:]
		return assetDir + assetName + '.' + assetName
	index = assetDir.find('/Engine')
	if index != -1:
		assetDir = assetDir[index:]
		return assetDir + assetName + '.' + assetName
	return ''

def writeCollectionFile(fileName, assetList):
	with open(fileName, 'w') as collectionFile:
		collectionFile.write('FileVersion:2\n')
		collectionFile.write('Type:Static\n')
		collectionFile.write('Guid:' + str(uuid.uuid1()) + '\n')
		collectionFile.write('ParentGuid:00000000-0000-0000-0000-000000000000\n')
		collectionFile.write('\n')
		for asset in assetList:
			collectionFile.write(asset + '\n')

projectName = ''
cookLogPath = ''
opts, args = getopt.getopt(sys.argv[1:], '', ['projectPath=', 'cookLogPath='])
for o, a in opts:
	if o == '--projectPath':
		projectPath = os.path.abspath(a)
		if not os.path.isdir(projectPath):
			print('project path not exist', projectPath)
			exit()
		projectName = os.path.basename(projectPath)
		projectContentPath = projectPath + '\\Content'
		projectCollectionPath = projectContentPath + '\\Collections'
	elif o == '--cookLogPath':
		cookLogPath = os.path.abspath(a)
		if not os.path.exists(cookLogPath):
			print('cook log file not exist', cookLogPath)
			exit()

if projectPath == '' or cookLogPath == '':
	text = """
	--projectPath: 
	--cookLogPath: CookerOpenOrder.log
	"""
	print(text)
	exit()

# used assets
usedAssets = set()
with open(cookLogPath, 'r') as cookLog:
	for line in cookLog:
		asset = standardPath(line.split(' ')[0][1:-1])
		if asset != '' and asset.startswith('/Game'):
			usedAssets.add(asset)

writeCollectionFile(projectCollectionPath + '\\used.collection', usedAssets)

# unUsed assets
allAssets = set()
for root, dirs, files in os.walk(projectContentPath):
	for line in files:
		asset = standardPath(os.path.join(root, line))
		if asset != '' and asset.startswith('/Game'):
			allAssets.add(asset)

unUsedAssets = allAssets.difference(usedAssets)

writeCollectionFile(projectCollectionPath + '\\unUsed.collection', unUsedAssets)

