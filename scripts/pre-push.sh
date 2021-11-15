#!/bin/bash

echo_failed_tests () {
  echo "Tests must pass before push."
  exit 1
}

echo "Running cdk synth"
cdk synth
status=$?
if [ $status -ne 0 ]; then
  echo_failed_tests
fi

