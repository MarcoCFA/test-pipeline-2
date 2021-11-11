#!/bin/bash

echo "Call run_tests.sh"

if cdk synth; then
    printf 'cdk synth succeeded\n'
else
    printf 'cdk synth failed\n'
fi

