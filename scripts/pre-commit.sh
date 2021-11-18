#!/bin/bash

echo "Running pre-commit.sh"

echo_failed_tests () {
  echo "Tests must pass before commit."
  exit 1
}

echo "Running iSort"
isort .
status=$?
if [ $status -ne 0 ]; then
  echo_failed_tests
fi

echo "Running black formatting"
# 1 - Go to the git root directory using pushd to navigate the directory stack
# 2 - Run black formatting on root directory
# 3 - Remove the root directory from the directory stack

pushd "$(git rev-parse --show-toplevel)" || return 1
black .
popd || return 1

echo "Running flake8 linter"
flake8 .
status=$?
if [ $status -ne 0 ]; then
  echo_failed_tests
fi

echo "Running mypy static linter"
mypy .
status=$?
if [ $status -ne 0 ]; then
  echo_failed_tests
fi





echo "Exiting pre-commit.sh"