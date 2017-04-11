API assignment
==============

For this assignment, you'll be replicating a small piece of what one of our scripts does at the Times: downloading a recent list of Congressional votes and saving it as a CSV. We run a very similar script every few minutes so that our own behind-the-scenes database of votes stays up-to-date.

Specifically, you'll be using the ProPublica Congress API to extract and organize the top-line information we used in [this interactive](https://www.nytimes.com/interactive/2017/04/06/us/politics/gorsuch-supreme-court-vote.html), which details how the Senate voted on the nomination of Neil Gorsuch to the Supreme Court, during which they abolished the 60-vote threshold for judicial nominees.

You'll be implementing two functions for this assignment:

  - The first, `get_votes_by_date`, should issue a request to the ProPublica API and return a Python object representing the data that comes back. The request will be to [this endpoint](https://propublica.github.io/congress-api-docs/#get-votes-by-date), and instructions on how to form the URL are included in the code.

  - The second, `format_nomination_votes`, should take that data and re-organize it into a list format that can be easily saved as as CSV. Further instructions are in the code.

Authentication information and the code to apply are included, so you won't have to worry about that.

Questions? Let me know. This assignment is due **next Wednesday, April 19**.