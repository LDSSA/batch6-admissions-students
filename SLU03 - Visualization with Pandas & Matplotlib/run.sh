#!/usr/bin/env bash
set -x
set -e

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

echo Copying notebook...
curl $NOTEBOOK_URL -H "Authorization: Token $LDSA_TOKEN" -o $NOTEBOOK_PATH

echo Grading
ldsagrader portal grade --notebook_path="$NOTEBOOK_PATH" --grading_url=$PORTAL_GRANDING_URL --checksum_url=$PORTAL_CHECKSUM_URL --token=$PORTAL_TOKEN

