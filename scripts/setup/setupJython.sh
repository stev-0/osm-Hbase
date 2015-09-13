export HBASE_HOME=/usr/hdp/current/hbase-client
export JYTHON_HOME=/home/ubuntu/jython
alias pyhbase='HBASE_OPTS="-Dpython.path=$JYTHON_HOME" HBASE_CLASSPATH=$JYTHON_HOME/jython.jar $HBASE_HOME/bin/hbase org.python.util.jython'