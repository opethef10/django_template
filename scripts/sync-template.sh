#!/usr/bin/env bash
# sync-template.sh <from-tag> <to-tag>
set -euo pipefail

FROM=$1
TO=$2
REMOTE=template

git fetch "$REMOTE"

PATCH=$(mktemp)
trap 'rm -f "$PATCH"' EXIT

git diff "refs/${REMOTE}-tags/${FROM}" "refs/${REMOTE}-tags/${TO}" -- . > "$PATCH"

if [ ! -s "$PATCH" ]; then
  echo "No changes between $FROM and $TO"
  exit 0
fi

git apply --3way "$PATCH"
