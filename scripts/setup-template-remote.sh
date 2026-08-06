#!/usr/bin/env bash
# setup-template-remote.sh
set -euo pipefail

URL="${1:-https://github.com/opethef10/django_template.git}"

git remote add template "$URL" 2>/dev/null || git remote set-url template "$URL"
git config remote.template.tagOpt --no-tags
git config --add remote.template.fetch '+refs/tags/*:refs/template-tags/*'
git fetch template
echo "Template remote configured. Run ./sync-template.sh <from-tag> <to-tag> to sync."
