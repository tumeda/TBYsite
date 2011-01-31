README

More instructions to follow.
This assumes you are working on a unix-based system.

install python2.7
install PIL
	verify installed correctly:
	$ python
		>>> import PIL
		>>> import _imaging
	No errors should appear
install pip
	verify installed correctly:
	$ pip --version
		pip 0.8.1
		
install git
	verify installed correctly:
	$ git --version
		git version 1.7.3.2
		
Create a directory for all this:
	$ mkdir pony
	$ cd pony
	$ pip install django cms-django django-appmedia south
	$ git clone git@github.com:frankm/TBYsite.git
	
Runserver
	$ cd example
	$ ls 
		__init__.py  __init__.pyc cms.sqlite   manage.py    media        sampleapp    sampleblog   settings.py  settings.pyc templates    urls.py      urls.pyc
	$ ./manage.py runserver
	
		Validating models...
		0 errors found

		Django version 1.2.4, using settings 'example.settings'
		Development server is running at http://127.0.0.1:8000/
		Quit the server with CONTROL-C.

Open browser
	http://127.0.0.1:8000/
	
	login as admin:
		http://127.0.0.1:8000/admin
		
		
