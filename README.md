pathfinder
==========

Created by Christopher R. Harty @2014
Thoughts behind this project were to showcase my capabilities, but might actually have legs for a new type of search engine model.

Continuous content traceroute service 
(content used loosely regarding word related search terms driving the service)

Description: 
So the purpose of this django project is to host campaigns w/seed words, resulting content, and analysis of spider results from the seed words.  The mind set is to take some initial words, perhaps in a hierarchy with weights of some sort (perhaps nlp based), point it to some sources (local content/cache, other services, search engines, or sites directly), gather the appropriate content and store, analyize content and generate more seed words to put back in the mix.  The process keeps cycling indefinitely or until a threshold is reached.

user workflow:
1. user creates a campaign with seed words via pathfinder UI
2. creates source sites to crawl and adds to the campaign via pathfinder UI
3. activate campaign, which sends data and a start signal to the spider via pf_crawler service
   Note: currently can only handle one request at a time, but would either expand to a pool or the more appropriate approach would be to use a queue service
4. the spidered results are sent back to the pathfinder API
5. pathfinder strips the content and generates new seed words for the current sub-url
6. cycles through...
7. was thinking of an interesting notification push to the UI to show realtime results... too much for the first pass of this thing...


Thoughts on creation process (soft list):
1. create the interface for campaigns and sources (basic functionality is approximately 80% complete)
2. create a service that discovers content via seed (in the process of building a spider)
3. create storage (looking at Casandra at the moment (will use sqlite temporarily)
4. algorithm for generating the next step seed context
5. complete the cycle
6. caching for analysis and reporting (looking at Redis)


I believe i will be using:
 - solr for most list content (now thinking that elasticsearch might be usable for this, more research needed, ... might be overkill)
 - nose for testing
 - elasticsearch for autofill and search results 