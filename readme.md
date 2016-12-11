
# Ox Keyboard Layout

```
^ 1 2 3 4 5 6 7 8 9 0 \ !
$ % @ [ ] ~ ` { } ( ) - =
   ; U L M W Z F R O " | + &
   : u l m w z f r o ' _ * #
    A I N T G B S H E P Y
    a i n t g b s h e p y
     J X D K Q V C < > ?
     j x d k q v c , . /
```

## Motivation
I type a lot, usually trying to type quickly. At high speed on the standard
QWERTY layout, I noticed that I lose speed and coordination through two major
factors: 1) hands jumping between distant key combinations, and 2) using the
same fingers to press multiple keys in succession (try typing `github` for
instance). I know that practically speaking QWERTY will always be my primary
layout, but I wanted to try something new anyway, for fun.

I tried Dvorak, Colemak, and Workman (a derivative of Colemak), but in each
instance I found either balancing problems or too many same-finger key
combinations. I liked workman the most; how this all started was *one teensy
little change* to that layout which then triggered my insatiable instinct to
tweak everything and now I have an entire new layout designed from the ground up
along with a whole suite of tools for analysing and developing keyboard layouts.

## Layout
And so the Ox layout was born. Its goal is to minimize 'finger collisions';
where two or more keys are (slowly) pressed by the same finger in succession. It
also aims to place most frequently used keys in strong positions and rearrage
punctuation in a way that minimizes jumping around when programming.

This is a highly personal layout, suited exactly for my purposes, and will
likely not work for everyone, at least without a little tweaking. For instance,
as most of my work is in python, the colon and semicolon have been swapped,
allowing the colon to be hit without shift. This might not sit well in other
languages.

## Usage
A common fear in learning a new keyboard layout is the idea of 'unlearning'
QWERTY and becoming too tightly coupled with a specific, esoteric layout. My
plan is to continue using QWERTY in most situations, only switching to Ox when
typing long passages. It might make the new layout more difficult to learn, but
ultimately it will be more important to use both.

## Methodology
When designing this layout, I discovered a need for good data; a way to analyze
how each iteration of the layout stacked up. So I wrote some python scripts. It
started as a loose set of counting functions and balooned into a big unorganized
mess, which I hope to clean up and reuse.

The primary metrics that I used to judge each layout were:

*Cost*, where the number of occurences of a letter was multiplied by a
difficulty level associated with the position where it was placed. Putting a
commonly used key like `e` in a hard-to-reach position would result in a higher
cost score.

*Collisions*, where all keys were grouped by the finger used to press them,
split into a list of all possible 2-wide permutations, and then compared against
a list of 2-wide pair frequencies within the test data. A pair like `th` has a
high frequency in test data, so putting the `t` and `h` keys under the same
finger will result in a costly collision.

*Balance*, where the keyboard was split into right and left hands (and
furthermore into ten separate fingers) and each key associated with a side based
on its position in the layout. Layouts where one finger or one hand were heavily
biased were considered inoptimal.

Ultimately, each of these metrics are tools, and the final decision was made
with personal judgement. The result is a layout that strikes a healty balance
between all metrics and makes trade-offs where they make sense.

## Data
I had a few sets of test data to work with: 1) a concatination of each python
file in my projects directory (collected by `cat **/*.py > keys/pydata`), 2)
a similar concat using normal english writing from my *Wistful Planet* novel,
and 3) the entire raw text of Moby Dick, taken from Project Gutenburg. In
retrospect, I could have used more varied code, in more than one language.
Future tweaks may take new data into account.

## Tools
The script `count.py` takes a set of commands:
    * `count`
    * `collisions`
    * `balance`
    * `fingers`
    * `cost`
    * `reactions`
More details to come on script usage. Features are likely to change anyway as I
refactor.

## Installation
`coming eventually`
