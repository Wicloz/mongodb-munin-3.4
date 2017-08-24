install:
	mkdir -p /usr/lib/mongopython
	touch /usr/lib/mongopython/__init__.py
	touch /usr/lib/mongopython/init.py
	install -m 755 ./mongopython/mongodb_commands.py /usr/lib/mongopython/mongodb_commands.py
	install -m 755 ./plugins/* /usr/share/munin/plugins/

enable:
	munin-node-configure --shell --families contrib | grep 'mongodb_' | sh

clean:
	rm -f /etc/munin/plugins/mongodb_*
	rm -f /usr/share/munin/plugins/mongodb_*
	rm -rf /usr/lib/mongopython
