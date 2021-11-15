#!/bin/bash

echo "Starting pre-commit.sh"

echo_failed_tests () {
  echo "Tests must pass before commit."
  exit 1
}


echo "Running black formatting test"
# 1 - Go to the git root directory using pushd to navigate the directory stack
# 2 - Run black formatting on root directory
# 3 - Remove the root directory from the directory stack

pushd "$(git rev-parse --show-toplevel)" || return 1
black .
popd || return 1

# Test 1
