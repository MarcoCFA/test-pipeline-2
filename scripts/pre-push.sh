#!/bin/bash


echo "Running pre-push.sh"

echo_failed_tests () {
  echo "Tests must pass before push."
  exit 1
}

echo "Running cdk synth"
cdk synth --output cdk.out/cdk.out
status=$?
if [ $status -ne 0 ]; then
  echo_failed_tests
fi

echo "Running bandit scan"
bandit -r . -x env
status=$?
if [ $status -ne 0 ]; then
  echo_failed_tests
fi

echo "Exiting pre-push.sh"