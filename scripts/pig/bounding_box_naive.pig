nodes = LOAD 'hbase://nodes' using
  org.apache.pig.backend.hadoop.hbase.HBaseStorage('nodeData:id nodeData:lat nodeData:lon nodeData:nodeTags')  as (id:long, lat:float, lon:float, nodeTags:map[]);

 /* need a way to get map in HBase to a chararray (or probably store it as a chararray in the first place)
 at the moment the nodeTags aren't printed */

filtered_nodes = FILTER nodes BY (lon > $minLon) AND (lon < $maxLon) AND (lat > $minLat) AND (lat < $maxLat);
DUMP filtered_nodes;

/* then join those nodes with ways to see which ones join */

/* finally check that you have got all nodes in the way by doing another join */

/* relations ??*/

