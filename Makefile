####################
# Install psmem.py #
####################

PREFIX=/usr

install:
	cp -rf pmem.py $(PREFIX)/bin/pmem.py
	chmod +x $(PREFIX)/bin/pmem.py

uninstall:
	rm -rf $(PREFIX)/bin/pmem.py

