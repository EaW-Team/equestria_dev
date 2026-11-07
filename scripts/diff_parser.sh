#!/bin/sh

# Author : EaW Team
# diff_parser.sh [number_of_commit|commit_hash]
# Concatenate the differences from the english localisation into a more readable format
# Take as parameter either a number or a commit hash, default to the number one
# Will output the difference from the current HEAD to the either the number of past commit from their
# Or to the specified commit hash

# Information header
echo "!info"
echo "Grabbed differences in the localisation/english folder from the commit:"
git log HEAD -n 1

echo -e "\n\nTo the commit:"

# Sanity check for the argument
# Either a number of commit before the current head, or a hash
COMMIT_LIMIT="HEAD~1"
RE_ARG="^[0-9]{1,3}$"
if ! [[ -z $1 ]]; then
    if [[ $1 =~ $RE_ARG ]]; then
        COMMIT_LIMIT="HEAD~$1"
        git log HEAD~$1 -n 1
    else
        COMMIT_LIMIT="$1..HEAD"
        git log $1 -n 1
    fi
fi

echo "info-!"

# Parsing the output of the git diff
RE_FILE="^\+{3} b/(.*)$"
RE_NB_LINE="^@@ -([0-9]*)"
RE_EXCLUDED_LINE="^(diff --git.*)?(index.*)?(-{3}.*)?([ ]*)$"
RE_NEW_LINE="^~$"
RE_ADD_LINE="^\+(.*)"
RE_RMV_LINE="^-(.*)"
DISPLAYED_LINE=false
while IFS= read -r line; do
    if [[ $line =~ $RE_FILE ]]; then
        echo ""
        echo "file ${BASH_REMATCH[1]}"

    elif [[ $line =~ $RE_NB_LINE ]]; then
        LINE_NB=$((${BASH_REMATCH[1]}))
        DISPLAYED_LINE=false

    elif [[ $line =~ $RE_NEW_LINE ]]; then
        LINE_NB=$(($LINE_NB+1))
        DISPLAYED_LINE=false

    elif ! [[ $line =~ $RE_EXCLUDED_LINE ]]; then
        if [[ $DISPLAYED_LINE = false ]]; then
            echo -n -e "$LINE_NB: "
            DISPLAYED_LINE=true
        else
            echo -n -e "\t"
        fi

        if [[ $line =~ $RE_ADD_LINE ]]; then
            echo -e -n "\t+|"
            echo ${BASH_REMATCH[1]}

        elif [[ $line =~ $RE_RMV_LINE ]]; then
            echo -e -n "\t-|"
            echo ${BASH_REMATCH[1]}

        elif ! [[ $line =~ "^$" ]]; then
            echo -e -n '\t |'
            echo $line
        fi
    fi
done <  <(git diff -b --patience --word-diff=porcelain --no-color -U0 $COMMIT_LIMIT localisation/english)
