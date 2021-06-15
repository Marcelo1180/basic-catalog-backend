# Project django base for examples

This project was tested in:
- Debian 10
- MacOSX Big Sur

## Requirements
  - pipenv

## Installation guide
* [Installing the project](INSTALL.md)
* [How use git](FAQ.md)

Setup config settings
```sh
cp settings.example.json settings.json 
```
__DEBUG=true__ is used for debugging mode, in this mode you can use:
- admin/ (Classic admin of django)
- apidoc/ (Swagger api documentation)
- logging with level DEBUG

Run development server
```sh
(env)$ python manage.py runserver
```

Run tests
```sh
(env)$ python manage.py test
```

## License

MIT License

    Copyright (c) 2021 Marcelo1180
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
