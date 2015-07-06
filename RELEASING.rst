============================
How to release pyranid_yards
============================


 * Ensure you are on git master and up to date
 * Increase version number in pyramid_yards/__init__.py
 * Fill the changelog (CHANGES.rst)
 * Fill the debian/changelog
 * run `python setup.py develop`
 * run `python setup.py extract_messages`
 * run `python setup.py update_catalog`
 * ensure there is no missing translations in locales
 * run `git add -u`
 *

