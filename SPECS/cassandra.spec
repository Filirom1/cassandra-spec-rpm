BuildArch:	noarch
Name:		cassandra
Version:	2.0.14
Release:	2%{?dist}
Summary:	Cassandra is a highly scalable, distributed key-value store.

Group:		Development/Libraries
License:	Apache Software License
URL:		http://cassandra.apache.org/
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Source0:	http://downloads.datastax.com/community/dsc-cassandra-%{version}-bin.tar.gz
Source1:	cassandra-default
Source2:	cassandra-initd
Source3:	cassandra-limits
Source4:	README.asc
Source5:	cassandra-logrotate

Conflicts:	cassandra
Conflicts:	apache-cassandra11
Conflicts:	apache-cassandra12
Conflicts:	apache-cassandra1
Obsoletes:	cassandra07
Obsoletes:	cassandra08
Provides:	user(cassandra)
Provides:	group(cassandra)
Requires:	python(abi) >= 2.6
Requires:	user(cassandra)
Requires:	group(cassandra)
Requires:	shadow-utils

Requires(post): chkconfig initscripts
Requires(pre): chkconfig initscripts


%description
Cassandra brings together the distributed systems technologies from Dynamo
and the data model from Google's BigTable. Like Dynamo, Cassandra is
eventually consistent. Like BigTable, Cassandra provides a ColumnFamily-based
data model richer than typical key/value systems.

For more information see http://cassandra.apache.org/

%prep
%setup -n dsc-cassandra-%{version}
rm bin/*.bat
rm tools/bin/*.bat
rm -fr pylib/cqlshlib/test

cd lib
unzip snappy-java-1.0.4.1.jar.zip

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/cassandra/default.conf
mkdir -p %{buildroot}/etc/default
mkdir -p %{buildroot}/etc/rc.d/init.d
mkdir -p %{buildroot}/etc/security/limits.d
mkdir -p %{buildroot}/etc/logrotate.d
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/lib/python2.6/site-packages/cqlshlib
mkdir -p %{buildroot}/usr/share/cassandra/default.conf
mkdir -p %{buildroot}/usr/share/cassandra/lib
mkdir -p %{buildroot}/usr/share/doc/%{name}-%{version}
mkdir -p %{buildroot}/var/lib/cassandra/{commitlog,data,saved_caches}
mkdir -p %{buildroot}/var/log/cassandra
mkdir -p %{buildroot}/var/run/cassandra

cp %{SOURCE1} %{buildroot}/etc/default/cassandra
cp %{SOURCE2} %{buildroot}/etc/rc.d/init.d/cassandra
cp %{SOURCE3} %{buildroot}/etc/security/limits.d/cassandra.conf
cp %{SOURCE4} %{buildroot}/usr/share/doc/%{name}-%{version}/README.asc
cp %{SOURCE5} %{buildroot}/etc/logrotate.d/%{name}

mv bin/cassandra %{buildroot}/usr/sbin
cp bin/cassandra.in.sh %{buildroot}/etc/cassandra/default.conf
cp bin/cassandra.in.sh %{buildroot}/usr/share/cassandra
mv bin/cassandra.in.sh %{buildroot}/usr/share/cassandra/default.conf
mv bin/* %{buildroot}/usr/bin
mv lib/* %{buildroot}/usr/share/cassandra/lib
mv pylib/* %{buildroot}/usr/lib/python2.6/site-packages
cp -r conf/* %{buildroot}/usr/share/cassandra/default.conf
mv conf/* %{buildroot}/etc/cassandra/default.conf
mv tools/bin/{cassandra-stress,token-generator} %{buildroot}/usr/bin
mv tools/lib/* %{buildroot}/usr/share/cassandra/lib
mv {CHANGES.txt,LICENSE.txt,NEWS.txt,NOTICE.txt} %{buildroot}/usr/share/doc/%{name}-%{version}/
mv switch_snappy %{buildroot}/usr/share/cassandra/switch_snappy


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %config(noreplace) %attr(0755, cassandra, cassandra) "/etc/cassandra"
%dir %config(noreplace) %attr(0755, cassandra, cassandra) "/etc/cassandra/default.conf"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/README.txt"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/cassandra-env.sh"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/cassandra-rackdc.properties"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/cassandra-topology.properties"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/cassandra-topology.yaml"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/cassandra.in.sh"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/cassandra.yaml"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/commitlog_archiving.properties"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/cqlshrc.sample"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/log4j-server.properties"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/log4j-tools.properties"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/metrics-reporter-config-sample.yaml"
%dir %config(noreplace) %attr(0755, cassandra, cassandra) "/etc/cassandra/default.conf/triggers"
%config(noreplace) %attr(0644, cassandra, cassandra) "/etc/cassandra/default.conf/triggers/README.txt"
%attr(0755, root, root) "/etc/rc.d/init.d/cassandra"
%config(noreplace) %attr(0644, root, root) "/etc/default/cassandra"
%config(noreplace) %attr(0644, root, root) "/etc/security/limits.d/cassandra.conf"
%config(noreplace) %attr(0644, root, root) "/etc/logrotate.d/%{name}"
%attr(0755, root, root) "/usr/bin/cassandra-cli"
%attr(0755, root, root) "/usr/bin/cassandra-stress"
%attr(0755, root, root) "/usr/bin/cqlsh"
%attr(0755, root, root) "/usr/bin/debug-cql"
%attr(0755, root, root) "/usr/bin/json2sstable"
%attr(0755, root, root) "/usr/bin/nodetool"
%attr(0755, root, root) "/usr/bin/sstable2json"
%attr(0755, root, root) "/usr/bin/sstablekeys"
%attr(0755, root, root) "/usr/bin/sstableloader"
%attr(0755, root, root) "/usr/bin/sstablescrub"
%attr(0755, root, root) "/usr/bin/sstablesplit"
%attr(0755, root, root) "/usr/bin/sstableupgrade"
%attr(0755, root, root) "/usr/bin/stop-server"
%attr(0755, root, root) "/usr/bin/token-generator"
#%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cassandra_pylib-0.0.0-py2.6.egg-info"
%dir %attr(0755, root, root) "/usr/lib/python2.6/site-packages/cqlshlib"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/__init__.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/__init__.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/__init__.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/cql3handling.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/cql3handling.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/cql3handling.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/cqlhandling.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/cqlhandling.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/cqlhandling.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/displaying.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/displaying.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/displaying.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/formatting.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/formatting.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/formatting.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/helptopics.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/helptopics.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/helptopics.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/pylexotron.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/pylexotron.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/pylexotron.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/saferscanner.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/saferscanner.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/saferscanner.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/ssl.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/ssl.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/ssl.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/tfactory.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/tfactory.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/tfactory.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/tracing.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/tracing.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/tracing.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/util.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/util.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/util.pyo"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/wcwidth.py"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/wcwidth.pyc"
%attr(0644, root, root) "/usr/lib/python2.6/site-packages/cqlshlib/wcwidth.pyo"
%attr(0755, root, root) "/usr/sbin/cassandra"
%dir %attr(0755, cassandra, cassandra) "/usr/share/cassandra"
%attr(0755, cassandra, cassandra) "/usr/share/cassandra/cassandra.in.sh"
%dir %attr(0755, cassandra, cassandra) "/usr/share/cassandra/default.conf"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/README.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/cassandra-env.sh"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/cassandra-rackdc.properties"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/cassandra-topology.properties"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/cassandra-topology.yaml"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/cassandra.in.sh"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/cassandra.yaml"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/commitlog_archiving.properties"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/cqlshrc.sample"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/log4j-server.properties"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/log4j-tools.properties"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/metrics-reporter-config-sample.yaml"
%dir %attr(0755, cassandra, cassandra) "/usr/share/cassandra/default.conf/triggers"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/default.conf/triggers/README.txt"
%dir %attr(0755, cassandra, cassandra) "/usr/share/cassandra/lib"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/antlr-3.2.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/apache-cassandra-2.0.14.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/apache-cassandra-clientutil-2.0.14.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/apache-cassandra-thrift-2.0.14.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/commons-cli-1.1.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/commons-codec-1.2.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/commons-lang3-3.1.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/compress-lzf-0.8.4.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/concurrentlinkedhashmap-lru-1.3.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/cql-internal-only-1.4.1.zip"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/disruptor-3.0.1.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/guava-15.0.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/high-scale-lib-1.1.2.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/jackson-core-asl-1.9.2.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/jackson-mapper-asl-1.9.2.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/jamm-0.2.5.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/jbcrypt-0.3m.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/jline-1.0.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/json-simple-1.1.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/libthrift-0.9.1.jar"
%dir %attr(0755, cassandra, cassandra) "/usr/share/cassandra/lib/licenses"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/antlr-3.2.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/commons-cli-1.1.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/commons-codec-1.2.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/commons-lang3-3.1.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/compress-lzf-0.8.4.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/concurrentlinkedhashmap-lru-1.3.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/cql-1.4.0.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/disruptor-3.0.1.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/guava-15.0.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/high-scale-lib-1.1.2.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/jackson-core-asl-1.9.2.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/jackson-mapper-asl-1.9.2.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/jamm-0.2.5.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/jbcrypt-0.3m.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/jline-1.0.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/json-simple-1.1.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/libthrift-0.9.1.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/log4j-1.2.16.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/lz4-1.2.0.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/metrics-core-2.2.0.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/netty-3.5.9.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/netty-3.6.6.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/reporter-config-2.1.0.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/servlet-api-2.5-20081211.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/slf4j-api-1.7.2.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/slf4j-log4j12-1.7.2.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/snakeyaml-1.11.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/snappy-java-1.0.5.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/snaptree-0.1.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/super-csv-2.1.0.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/thrift-python-0.9.1.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/licenses/thrift-server-0.3.3.txt"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/log4j-1.2.16.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/lz4-1.2.0.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/metrics-core-2.2.0.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/netty-3.6.6.Final.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/reporter-config-2.1.0.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/servlet-api-2.5-20081211.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/slf4j-api-1.7.2.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/slf4j-log4j12-1.7.2.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/snakeyaml-1.11.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/snappy-java-1.0.4.1.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/snappy-java-1.0.4.1.jar.zip"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/snappy-java-1.0.5.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/snappy-java-1.0.5.jar.zip"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/snaptree-0.1.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/stress.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/super-csv-2.1.0.jar"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/thrift-python-internal-only-0.9.1.zip"
%attr(0644, cassandra, cassandra) "/usr/share/cassandra/lib/thrift-server-0.3.7.jar"
%attr(0755, cassandra, cassandra) "/usr/share/cassandra/switch_snappy"
%dir %attr(0755, root, root) "/usr/share/doc/%{name}-2.0.14"
%doc %attr(0644, root, root) "/usr/share/doc/%{name}-2.0.14/CHANGES.txt"
%doc %attr(0644, root, root) "/usr/share/doc/%{name}-2.0.14/LICENSE.txt"
%doc %attr(0644, root, root) "/usr/share/doc/%{name}-2.0.14/NEWS.txt"
%doc %attr(0644, root, root) "/usr/share/doc/%{name}-2.0.14/NOTICE.txt"
%doc %attr(0644, root, root) "/usr/share/doc/%{name}-2.0.14/README.asc"
%dir %config(noreplace) %attr(0755, cassandra, cassandra) "/var/lib/cassandra/commitlog"
%dir %config(noreplace) %attr(0755, cassandra, cassandra) "/var/lib/cassandra/data"
%dir %config(noreplace) %attr(0755, cassandra, cassandra) "/var/lib/cassandra/saved_caches"
%dir %attr(0755, cassandra, cassandra) "/var/log/cassandra"
%dir %attr(0755, cassandra, cassandra) "/var/run/cassandra"
%ghost %attr(0644, root, root) %verify(not md5 size link mtime) "/var/log/cassandra/cassandra.log"
%ghost %attr(0644, cassandra, cassandra) %verify(not md5 size link mtime) "/var/log/cassandra/system.log"
%ghost %attr(0644, cassandra, cassandra) %verify(not md5 size link mtime) "/var/run/cassandra/cassandra.pid"
%exclude /usr/lib/python2.6/site-packages/setup.py*

%pre -p /bin/sh
getent group cassandra >/dev/null || groupadd -r cassandra
getent passwd cassandra >/dev/null || \
useradd -d /usr/share/cassandra -g cassandra -M -r cassandra
exit 0

%post -p /bin/sh
chkconfig --add cassandra
alternatives --install /etc/cassandra/conf cassandra /etc/cassandra/default.conf/ 0
# alternatives --install /etc/default/cassandra cassandra /etc/cassandra/default.conf/cassandra.default 0
cd /usr/share/cassandra/lib
grep "release 5" /etc/redhat-release > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then
  # Put old snappy file in place for old Linux distros. Basically
  # rename the newer version out of the way.
  if [ -f snappy-java-1.0.5.jar ]; then
    if [ -f snappy-java-1.0.5.jar.backup ]; then
      /bin/rm -f snappy-java-1.0.5.jar.backup
    fi
    /bin/mv snappy-java-1.0.5.jar snappy-java-1.0.5.jar.backup
  fi
else
  # Move old version of snappy out of the way on modern Linux versions
  if [ -f snappy-java-1.0.5.jar ]; then
    if [ -f snappy-java-1.0.4.1.jar ]; then
      if [ -f snappy-java-1.0.4.1.jar.backup ]; then
        /bin/rm -f snappy-java-1.0.4.1.jar.backup
      fi
      /bin/mv snappy-java-1.0.4.1.jar snappy-java-1.0.4.1.jar.backup
    fi
  fi
fi
exit 0

%preun -p /bin/sh
if [ "$1" = "0" ]; then
  /sbin/service cassandra stop
  chkconfig --del cassandra
fi
# only delete alternative on removal, not upgrade
if [ "$1" = "0" ]; then
    alternatives --remove cassandra /etc/cassandra/default.conf/
fi
if [ "$1" = "0" ]; then
  # restore original snappy files so package management is happy on removal
  cd /usr/share/cassandra/lib
  if [ -f snappy-java-1.0.5.jar.backup ]; then
    if [ -f snappy-java-1.0.5.jar ]; then
      /bin/rm -f snappy-java-1.0.5.jar
    fi
    /bin/mv snappy-java-1.0.5.jar.backup snappy-java-1.0.5.jar
  fi
  if [ -f snappy-java-1.0.4.1.jar.backup ]; then
    if [ -f snappy-java-1.0.4.1.jar ]; then
      /bin/rm -f snappy-java-1.0.4.1.jar
    fi
    /bin/mv snappy-java-1.0.4.1.jar.backup snappy-java-1.0.4.1.jar
  fi
fi
exit 0

%changelog
* Tue May 12 2015 Romain Philibert <romain.philibert@worldlinet.com> - 2.0.14-2
- Rename cassandra20 to cassandra
- Fix rpmlint issues
- Flag every files in /etc with %config(noreplace) 
- Add ghost files
- Logs in /var/log/cassandra/cassandra.log are not erased on restart
- Add log rotation on /var/log/cassandra/cassandra.log

* Tue May 12 2015 Romain Philibert <romain.philibert@worldlinet.com> - 2.0.14-1
- Create SRPMs using rpmrebuild

* Thu Dec 16 2010 Nate McCall <nate@riptano.com> - 0.7.0-rc2
- Version numbering change
- Added macro definition for build paths
- Fix license declaration to use ASF

* Wed Aug 04 2010 Nick Bailey <nicholas.bailey@rackpace.com> - 0.7.0-1
- Updated to make configuration easier and changed package name.

* Tue Jul 06 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.3-1
- Initial package
