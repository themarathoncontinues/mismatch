#!/bin/bash

echo "Running tests for mismatch..."
export PYTHONPATH=$PWD

pytest --cov=src/ -v tests/

echo "Finished running tests."