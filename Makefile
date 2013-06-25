all:
	python gokien_welcome.py
	rm -f ~/.config/gokien/welcome-lock
install:
	install -D -m 755 gokien_welcome.py \
			$(DESTDIR)/share/gokien-welcome/gokien_welcome.py
	install -D -m 755 -d $(DESTDIR)/share/gokien-welcome/templates
	install -D -m 755 -t $(DESTDIR)/share/gokien-welcome/templates/ \
		templates/logo.jpg \
		templates/script.js \
		templates/style.css \
		templates/welcome.html \
		templates/welcome.jade

	install -D -m 755 gokien-welcome $(DESTDIR)/bin/gokien-welcome
