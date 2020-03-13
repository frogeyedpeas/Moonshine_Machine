So the current plan:


1. Build a stable downloader for OEIS (this can be upgraded later to ArXiV)
2. We then define a parser that can store the sequences in some type of database
3. We then create a coincidence-type-library, and have a script that uses it to explore for a set of coincidences 
4. This get stored in a DB by coincidence type 
5. Now we host a website that allows you to see for each type, a list of all the coincidences, and people can go ahead and upvote and downvote coincidences

So which sequences are interesting? We probably want to filter them for strictly positive elements, and make sure they are growing at least at a pace of 2^n (a beyond exp-growth condition ensures that packing is "expected" to fail but testing that globally can be hard)

Some architecture notes:

SQL database containing "coincidence text", OEIS IDs and # of upvotes and # of downvotes 

When a user hits the URL they are served up a :wq

