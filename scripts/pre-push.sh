#!/bin/bash


echo "Running pre-push.sh"

echo_failed_tests () {
  echo "Tests must pass before push."
  exit 1
}

echo "Running cdk synth"
rm -rf cdk.out/cdk.out
cdk synth --output cdk.out/cdk.out
status=$?
if [ $status -ne 0 ]; then
  echo_failed_tests
fi

echo "Running bandit scan-1"
bandit -r . -x env
status=$?
if [ $status -ne 0 ]; then
  echo_failed_tests
fi

echo "Exiting pre-push.sh"