============================
How to release pyramid_yards
============================


 * Ensure you are on git master and up to date
 * Increase version number in pyramid_yards/__init__.py
 * Fill the changelog (CHANGES.rst)
 * Fill the debian/changelog
 * run `python setup.py develop`
 * run `python setup.py extract_messages update_catalog`
 * ensure there is no missing translations in locales
 * run `python setup.py compile_catalog`
 * run `git add -u`
 * run `git commit -m "Release X.Y" where X.Y is the version numer
 * run `git push origin master:master"
 * run `python setup.py sdist upload`  # NOT WORKING FOR ME ACTUALY
 * run `git tag X.Y`
 * run `git push origin X.Y`
 