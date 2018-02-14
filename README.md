(this README is a work in progress)

# Operation Make Love, Not War

Live demo: http://interactives.kycir.org/vday/play.html

The political scene can be ugly. But it doesn’t have to be.

That’s why KyCIR is bringing back *Operation Spread Love, Not War*. We invite you to flip the script on some well-known quotes from some of Kentucky’s most prominent politicians. Some are contentious; some are pleasant political platitudes. But none of them are spreading love. That’s where *Operation Make Love, Not War* comes in.

## How It Works (General)

You create a list of characters and quotes that those characters have said via social media or other outlets.

By substituting some of the words in the character quotes with asterisks (*), you can create a mad-lib style app that allows users to fill in the blanks.

What you'll need to do:

- Find images of your state politicians and create character cards out of the images
- Create base Valentine's Day cards that will be populated by the user's custom mad lib
- Create `csv` files for each the [characters](data/vday-characters.csv) and for the [character quotes](data/vday-quotes.csv). Make sure to associate characters with quotes through the `characterUID` field
- Add characters and quotes as json objects
- Set this up on a server that can run custom php files, like an AWS EC2
- Set up a Facebook Developer App


## Requirements

This app is best deployed on a server over which you have control, like an AWS EC2 server, as it requires a few server-side processes.


