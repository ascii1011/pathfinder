pathfinder
==========

Created by Christopher R. Harty @2014

Continuous content traceroute service

Description: 
So the purpose of this django project is to host campaigns w/seed words, resulting content, and analysis of spider results from the seed words.  The mind set is to take some initial words, perhaps in a hierarchy with weights of some sort (perhaps nlp based), point it to some sources (local content/cache, other services, search engines, or sites directly), gather the appropriate content and store, analyize content and generate more seed words to put back in the mix.  The process keeps cycling indefinitely or until a threshold is reached.

Thoughts on creation process (soft list):
1. create the interface for campaigns and sources
2. create a service that discovers content via seed
3. create storage (looking at Casandra at the moment
4. algorithm for generating the next step seed context
5. complete the cycle
6. caching for analysis and reporting (looking at Redis)


I believe i will be using:
 - solr for most list content,
 - nose for testing
 - elasticsearch for autofill and search results 