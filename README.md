# osm-Hbase
Tools to import osm data into Hbase

Use hbase shell to setup HBase with two tables, nodes and ways with one column family each

`create ‘nodes’, ‘nodeData'`

`create ‘ways’, ‘wayData'`

You can then run the pig scripts to bulk load data into and out of HBase
