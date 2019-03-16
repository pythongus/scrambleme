# Text Scrambler - A Teaser For Your Brain

## Abstract
This is a simple application to demonstrate the micro-framework Flask. It helps demonstrate how the human brain can easily read a text with scrambled words, as long as the first and last letters of the words are kept in place.

The application has three pages:
* The home page, where you can input the test text
* The results page, where you can see the scrambled test text
* And the *Would you like to know more about your brain?* page, which you give you ten links to articles in the Wikipedia about the brain.


Each of these page is redirected to routers in the file

> web/app.py

The *Would you like to know more about your brain?* page is built after a request to the Wikipedia RESTFUL API, with the search set on brain as the keyword. The first ten results are shown.

## Application Stack And Modules

* Flask
* requests
* scramble

## Host

* [Heroku.com][2]

[2]: https://www.heroku.com

### Active URL

* https://scrambleme.herokuapp.com/

## Installing And Running

Expanding the package

* On Linux

```
tar zxvf scrambleme-1.0.0.tgz
```

* On Windows

    Double-click on the `tgz` file and use the `Extract` option.

To install the modules
```
pip install -r requirements.txt
pip install -é scrambleme-1.0.0/ # on Windows, the path separator is `\`.
```

To run the flask app

* On Linux
```
export FLASK_ENV=development
FLASK_APP=./scrambleme-1.0.0/wsgi.py flask run
```
* On Windows
```
set FLASK_ENV=development
set FLASK_APP=.\scrambleme-1.0.0\wsgi.py
flask run
```


## Contact

I am Gus Garcia. Feel free to drop an email on [pythongus@gmail.com][1]

[1]: mailto:pythongus@gmail.com
