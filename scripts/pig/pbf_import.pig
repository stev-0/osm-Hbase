REGISTER osmpbf-1.3.3.jar; 
REGISTER osmpbfinputformat.jar;

/* The map should be converted to a chararray as when loading back from HBase, I think Pig automatically
assumes the map is the column family. Since we don't know the tag names this isn't what we want 
(or maybe this isn't a problem)*/

pbf_nodes = LOAD '$inputFile' USING io.github.gballet.pig.OSMPbfPigLoader('1') AS (id:long, lat:double, lon:double, nodeTags:map[]);
pbf_ways = LOAD '$inputFile' USING io.github.gballet.pig.OSMPbfPigLoader('2') AS (id:long, nodes:bag{(pos:int, nodeid:long)},wayTags:map[]);

STORE pbf_nodes INTO 'hbase://nodes' USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('nodeData:lat,nodeData:lon,nodeData:nodeTags');
STORE pbf_ways INTO 'hbase://ways' USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('wayData:nodes,wayData:wayTags');