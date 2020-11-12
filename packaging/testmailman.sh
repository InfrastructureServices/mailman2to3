#!/bin/bash
pushd /usr/lib/mailman/
mkdir -p /run/lock/mailman
python3 tests/testall.py
popd
