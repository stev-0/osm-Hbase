from xml.sax import make_parser, handler 
from xml.sax.handler import ContentHandler 
import sys

import java.lang 
from org.apache.hadoop.hbase import HBaseConfiguration, HTableDescriptor, HColumnDescriptor, HConstants
from org.apache.hadoop.hbase.client import HBaseAdmin, HTable
from org.apache.hadoop.hbase.client import Get,Put,Delete

class CountingHandler(ContentHandler):
    def __init__(self):
        self.isModify = False
        self.isCreate = False
        self.isDelete = False
	self.isWay = False
	self.nodeId = 0
	self.wayId = 0
	self.nodeUser = ''
	self.wayUser = ''
	self.nodeTags = []
	self.wayTags = []
	self.wayNodes = []
	self.nodeLat = 0.0
	self.nodeLon = 0.0

    def processElement(self,name,attrs):
    	if name == 'node':
	   self.isNode = True
	   self.nodeId = attrs.getValue('id')
           self.nodeLat = attrs.getValue('lat')
	   self.nodeLon = attrs.getValue('lon')
	   self.nodeUser = attrs.getValue('user')
        if name == 'way':
	   self.isWay = True
	   self.wayId = attrs.getValue('id')
	   self.wayUser = attrs.getValue('user')
        if name == 'nd':
	   self.wayNodes.append(attrs.getValue('ref'))
	if name == 'tag':
	   tag = (attrs.getValue('k'),attrs.getValue('v'))
	   if self.isWay and not self.isNode:
	      self.wayTags.append(tag)
	   else:
	      self.nodeTags.append(tag)
	
    def startElement(self, name, attrs):
        if name == 'modify':
        	self.isModify = True
        if name =='create':
        	self.isCreate = True
        if name == 'delete':
        	self.isDelete = True
        self.processElement(name,attrs)

    def endElement(self, name):
    	if name == 'modify':
        	self.isModify = False
        if name =='create':
        	self.isCreate = False
        if name == 'delete':
        	self.isDelete = False 
	if name == 'node':
		row = Put(self.nodeId)
		row.add('nodeData','user',self.nodeUser)
		row.add('nodeData','lat',self.nodeLat)
		row.add('nodeData','lon',self.nodeLon)
		if len(self.nodeTags) > 0:
		   row.add('nodeData','tags',",".join("(%s,%s)" % tup for tup in self.nodeTags))
		   self.nodeTags = []
		table.put(row)
		self.nodeId = 0
		self.nodeLat = 0.0
		self.nodeLon = 0.0
		self.isNode = False
	if name == 'way':
		print self.wayId
		print self.wayUser
		if len(self.wayNodes) > 0:
		   print self.wayNodes
		   self.wayNodes = []
		if len(self.wayTags) > 0:
		   print self.wayTags
		   self.wayTags = []
		self.isWay = False		

def setupHbase(): 
   admin = HBaseAdmin(conf) 
   desc = HTableDescriptor(tablename) 
   desc.addFamily(HColumnDescriptor("nodeData")) 

   if admin.tableExists(tablename):
      admin.disableTable(tablename) 
      admin.deleteTable(tablename)
   admin.createTable(desc)
   global table 
   table = HTable(conf, tablename)

def main(argv=sys.argv):
   parser = make_parser()
   h = CountingHandler()
   parser.setContentHandler(h)
   with open(argv[1], "r") as input:
      parser.parse(input)

if __name__ =='__main__':
    conf = HBaseConfiguration()
    tablename = "nodesTest"    
    setupHbase()
    main()
