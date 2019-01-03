Changelog
=========

0.15 (2019-01-03)
-----------------

 * Remove deprecation warning for pyramid >= 1.9

0.14 (2017-09-12)
-----------------

 * Add i18n support for colander message base on locale of pyramid request,
   requires the locale negociator.

0.13 (2016-10-28)
-----------------

 * Fix the DISABLE_CSRF_CHECK attribute

0.12 (2016-10-27)
-----------------

 * Fix DISABLE_CSRF_CHECK attribute for schema per http verb

0.11 (2016-07-25)
-----------------

 * Fix sequence deserialization


0.10 (2016-01-05)
-----------------

 * Add a schema per http verb


0.9 (2015-09-23)
----------------

 * Fix sequence validator


0.8 (2015-09-21)
----------------

 * Fix colander.drop deserialization in sequence member


0.7 (2015-07-06)
----------------

 * Fix packaging for locales


0.6 (2015-07-06)
----------------

 * Check the CSRF (active by default!)
 
  You can use the settings `pyramid_yards.check_csrf_token` to disable it
  globally (while writing json API), or locally by adding the attribute
  DISABLE_CSRF_CHECK = False in the `request_schema`


0.5 (2015-06-02)
----------------

 * Ensure request.yards dict contains every described fields


0.4 (2014-12-24)
----------------

 * Use request.yards as a dict mapping


0.3 (2014-12-15)
----------------

 * Fix support for sequence

0.2 (2014-12-04)
----------------

 * Fix usage of colander.drop

0.1 (2014-12-03)
----------------

 * Initial Release

 
