REGISTER osmpbf-1.3.3.jar; 
REGISTER osmpbfinputformat.jar;

pbf_nodes = LOAD '$inputFile' USING io.github.gballet.pig.OSMPbfPigLoader('1') AS (id:long, lat:double, lon:double, nodeTags:map[]);
/*pbf_ways = LOAD '$inputFile' USING io.github.gballet.pig.OSMPbfPigLoader('2') AS (id:long, nodes:bag{(pos:int, nodeid:long)},
tags:map[]);*/

STORE pbf_nodes INTO 'hbase://nodes' USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('nodeData:lat,nodeData:lon,nodeData:nodeTags');