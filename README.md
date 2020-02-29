# AIVA-barcode-recognition
Interleaved 2of5 barcode recognizer.

## Installation
### Make installation
 - Clone the repository
 - Open terminal and type `make init` to install the pip dependencies

### Pip installation
 - Clone the repository
 - Open terminal and type `pip install -r requirements.txt`to install the pip dependencies
 
## Run all the tests

NOTE: Current code is only for mockup purposes, not all the tests will succeed, 
because there is no actual barcode recognizer implemented yet. Once the recognizer
is implemented it will be mandatory for the algorithm to succeed for all the test suite.

### Make
 - Open terminal and run `make test` 
 
### Nosetests
 - Open terminal and run `nosetests tests` 