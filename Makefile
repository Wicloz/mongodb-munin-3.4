install:
	mkdir -p /usr/lib/mongostatus
	touch /usr/lib/mongostatus/__init__.py
	touch /usr/lib/mongostatus/init.py
	install -m 755 ./mongostatus/mongodb_server_status.py /usr/lib/mongostatus/mongodb_server_status.py
	install -m 755 ./mongostatus/mongodb_list_databases.py /usr/lib/mongostatus/mongodb_list_databases.py
	install -m 755 ./plugins/* /usr/share/munin/plugins/

enable:
	munin-node-configure --shell --families contrib | grep 'mongodb_' | sh

clean:
	rm -rf /usr/lib/mongostatus
	rm -f /etc/munin/plugins/mongodb_*
	rm -f /usr/share/munin/plugins/mongodb_*
