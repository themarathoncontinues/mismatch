#!/bin/bash

echo "Running tests for mismatch..."
export PYTHONPATH=$PWD

pytest --cov-report term-missing --cov=src/ --cov-report html:cov_html -vv tests/

echo "Finished running tests."