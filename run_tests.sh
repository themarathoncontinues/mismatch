#!/bin/bash

echo "Running tests for mismatch..."

pytest --cov=src/ -v tests/

echo "Finished running tests."