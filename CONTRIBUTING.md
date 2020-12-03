# Code Style Guidelines

Please read the following code style guidelines before committing code to
this repository.  We do our best to adhere to them.

Python

Pep 8: https://www.python.org/dev/peps/pep-0008/
Google Style: http://google.github.io/styleguide/pyguide.html

JavaScript:
https://google.github.io/styleguide/javascriptguide.xml

Line Wrapping
We follow the PEP8 standard of 79 characters which makes it easier to view 
files in split panes.  Please set any linting utilities and IDE settings for 
line length to 79 characters.  We have automated tests to validate lines do 
not exceed this length.Python Imports

Wildcard Imports
We have a strict no wildcard import policy.  We don't want to accidentally 
import any classes/modules as they are added.  This also simplifies 
refactoring, as it's easy to identify every python file that is importing a 
particular class with a full import search.

One Import Per Line Preference
Every python import should be broken up into a single line.  Do not combine 
multiple imports into a single line.  This helps prevent merge conflicts.  

We recommend setting up your IDE to automatically use single line imports 
(see Pycharm Settings for example: 
https://www.jetbrains.com/pycharm/guide/tips/one-import-per-line/).  

Do:
```
from my.module import ClassOne
from my.module import ClassTwo
```

Don't:
```
from my.module import ClassOne, ClassTwo
```



# Unit Test Policy

The policy is simple, all your code should be accompanied by new tests
or modifications to existing tests.

All new python and javascript code must have tests. All bug fixes must
have a test that verifies the implemented fix. When modifying code that
does not have a unit test, at a minimum add tests for the code you are
adding.


# Git Commit Messages

Informative clear commit messages are important and have
proven critical in tracking down changes in the past.

To write a more detailed commit message than a one liner
use: `git commit`. In general, one liners are rarely helpful.

Here is a template for a commit message:

```
Use Capitalized Short (72 Chars or Less) Summary

Add detailed explanatory text to explain commit. Wrap it
it to about 72 characters or so. Seperate the details
from the summary by one blank line so git commands & tools
that use the commit message can easily parse the summary
from the details.

Use impertive mood and simple present tense, like this template
is. Make summary and paragraphs sound like commands.
"Fix API Throwing 500s On Large Input" is an example summary
written using the imperitive mood. A statement in the details
may look something like this: "Change the custom domain
verification algorithm to use the authoritative name servers.
The authoritative name servers hold the actual DNS records for
a domain and are the only servers that can actually verify that
the DNS is setup correctly."

Use asterisks to make an unordered & bulleted list. Indent the
entire list by 2 spaces from the left margin.

  * Seperate the first bullet from the preceding text and
    each item in the list with a single blank line.

  * For the longer items, wrap the text at 72 characters from
    the left margin and left indent to align the item text.

  * Use an asterisk for the bullet (i.e. unordered list),
    preceded by a single space, with blank lines in between.

Use increasing numbers followed by a period and a space for
numbered lists.

  1. Follow the same formatting & indentation convention for
     bullets.

  2. Use a linear sequence starting at 1 increasing by 1 -
     not all consumers of the message treat the text as markdown
     so numbers will not get auto-generated.

```

# Pull Request Guidelines
> Code review is the discipline of discussing your code with your peers. - Derek Prior
> [Implementing a Strong Code-Review Culture](https://www.youtube.com/watch?v=PJjmw9TRB7s)

A code review is an opportunity for discussion and education about a piece of
code. To get the most out of the code review process the author and
reviewer both have a set of best practices.

## Author
 * Provide Context - The more context a review has, the better the reviewer will
   be able to understand the change.
   * Verbose commit messages are important.  Linking to the Jira/Sentry item is
     important but providing the context so the reviewer doesn't need to
     reference those items is ideal.
   * Some very small PRs have hours or days of research involved in them.  Use
     the commit message to show your research and why you came to land on this
     solution.
   * For code that includes changes to HAML or HTML include a screenshot as a
     comment in the first line of the corresponding HAML file. For complex or
     nested HAML use your discretion as to add a cropped screenshot for each
     file, or to include an overview in the containing file. Update these
     screenshots with the most recent copy change. For complicated interactions,
     include an animated gif or movie in place of a standard screenshot.
 * Keep it Manageable - Large reviews are tough.
   * Try to keep your reviews as small as possible.  Large reviews can be
     overwhelming to the reviewer.
   * If you are committing a large change try to break it up into logical
     commits and suggest the reviewer review each commit in order.
 * Data Migrations - Be wary when migrating large amounts of data.
   * Run all migrations locally or on a mirror of the production database.
   * Provide testing context to reviewer.
   * For financial or other critical data consider writing an audit task to
     verify changes after deployment.


## Reviewer
 * Ask Don't Tell - To foster discussion and education try not to use commands
   in reviews.
   * Instead of "This is wrong" try "Did you consider...?"
 * Not My Code - Try to recognize the difference between incorrect code and "not
   the way I would have done it."
   * If you see code you don't like reflect on why.
 * Things to look For
   * Clarity is Key - Think about your future self.
     * If code is hard to understand within the context of the review it will
       be even harder to reason about in the future.
     * Heavily optimized code can be hard to reason about.  If optimizations
       are needed, make sure they are well commented(along with the context of
       why they are needed).
   * [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle) -
     Look for ways to refactor code that is showing multiple responsiblities.
   * Test Coverage - Tests are important.
     * When reviewing make a mental list(or written!) of what kinds of tests you
       expect to see and then double check that they exist.
   * Schema Changes
     * MySQL has to rewrite the entire table if indexes change, so be wary of
       this when changing large tables.
  * Unfamiliar Code Reviews - Doing your best
    * Reduce Risk
      * Focus on areas of the review you do understand.
      * Discuss deployment/test plans and fallback plans.
    * Focus on Tests
      * Tests can be a great entryway to a confusing review.
    * State Assumptions
      * Start a discussion on what your assumptions are about the review are.
    * Review at your understanding
      * You may not understand the entire review, but make sure you provide
        feedback on the areas you understand.
    * Cribbed from: [How to Review Code You Don't Understand](https://blog.sentry.io/2018/01/24/review-code-you-dont-understand)
