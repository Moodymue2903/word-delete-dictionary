# The Word You'd Delete From the Dictionary

[![make.fun](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/c/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/Moodymue2903/word-delete-dictionary/rank.svg)](https://make.fun/c/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/Moodymue2903/word-delete-dictionary/reward.svg)](https://make.fun/c/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

Entry for the make.fun bounty: https://make.fun/c/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2

## The word

**Tomorrow**

Delete "tomorrow" and everything is due today. There is no more
"I'll do it tomorrow", no more putting things off until a day that
never comes. The gap the word leaves is the joke itself: it lands
the moment the word is gone, the humour comes from the word and the
hole it leaves in the language, and it is not the field's first
thought.

## Why this word

A blind tournament over 20 original candidate words, judged by three
independent judges against the judge's exact five criteria, in order:
a real recognised word, funny at first sight, humour from the word
itself, fresh, exact. Tomorrow took 52 of a possible 60 Borda points,
ahead of Captcha on 51 and Actually on 49, then won the head-to-head
runoff against both with two of three runoff judges. The obvious
hate-words the field will flood — Moist, Literally, Monday — finished
at the bottom of every ranking on freshness, and byte-identical
entries share one rate, so a flooded pick cannot win big.

## How it runs

`main.py` validates the word against the gate (UTF-8, 1–77 characters,
not only whitespace, exactly one word) and writes it to
`/output/entry.txt`, then reads the file back and refuses to finish
unless the bytes match exactly.
