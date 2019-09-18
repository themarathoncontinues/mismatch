#!/bin/bash

echo "Running tests for mismatch..."
export PYTHONPATH=$PWD

pytest --cov=src/ -vv tests/

echo "Finished running tests."