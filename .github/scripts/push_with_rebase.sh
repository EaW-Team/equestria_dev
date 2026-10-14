#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 BRANCH" >&2
  exit 2
fi

branch="$1"
git check-ref-format --branch "$branch" >/dev/null
remote_ref="refs/remotes/origin/$branch"

for attempt in 1 2 3; do
  git fetch --no-tags origin \
    "+refs/heads/$branch:$remote_ref"
  git rebase "$remote_ref"

  if git push origin "HEAD:$branch"; then
    exit 0
  fi
  if [[ "$attempt" -lt 3 ]]; then
    echo "::warning::Push raced with another update; retrying ($attempt/3)."
  fi
done

echo "::error::Push was rejected after three fetch/rebase attempts."
exit 1
