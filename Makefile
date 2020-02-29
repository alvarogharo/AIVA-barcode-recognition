init:
	pip install -r requirements.txt
setup:
    setup.py develop
test:
    nosetests tests