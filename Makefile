deploy:
	mkdir tmp
	mkdir tmp/yakusoku
	cp -a yakusoku tmp/
	cp dotcloud_conf/* tmp/
	rm -f tmp/yakusoku/settings.py
	rm -f tmp/yakusoku/urls.py
	mv tmp/settings.py tmp/yakusoku/settings.py
	mv tmp/urls.py tmp/yakusoku/urls.py
	dotcloud push yaku tmp
	rm -rf tmp