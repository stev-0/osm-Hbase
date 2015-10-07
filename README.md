# osm-Hbase
Tools to import osm data into Hbase

Requirements
------------

 - HBase >= 0.98
 - Pig >= 0.14
 - Jython = 2.7 if you want to use the change import scripts
 - [osmpbfinputformat](https://github.com/gballet/osmpbfinputformat) - compiled file also available from .....
This has osmpbf as a dependency - this can be found in the lib directory of the above project

Installation
------------

Use hbase shell to setup HBase with two tables, nodes and ways with one column family each

`create ‘nodes’, ‘nodeData'`

`create ‘ways’, ‘wayData'`

You can then run the pig scripts to bulk load data into and out of HBase
