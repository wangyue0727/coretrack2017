# coretrack2017
The method used for Core Track 2017 (TREC)

Documentation of the code for the core track 2017.

1. Crawl the snippets from Google, Yahoo, and Bing!
   The crawler is ready in the snippets_crawl folder. There are three functions within that folder:
   
   * snippets crawler
   
   A python package to crawl and parse the snippets. It takes two parameters, the input file which contains the queries to crawl, and the sources to crawl from (`g` for Google, `b` for Bing!, and `y` for Yahoo, or `all` for all three). Example input file is web_topics_all.
   
   `python crawler.py -i INPUT_FILE -s [all|g|b|y]`
   
   * snippets checker
   
   A python script to check if 100 snippets have been crawled for each query from every source. If not, a re-do list for the certain resource will be generated. 
   
   `python check_snippets.py -a ALL_QUERY_FILE`
   
   * Convert json snippets to trec format
   
   A python script convert snippets from json format to trec doc format. Note the duplicate snippets for each topic will be removed. 
   
   `python json2trec.py -i JSON_FOLDER -o TREC_FOLDER`
   
2. Build the Indri
   
   Since we need to include f2exp and f2log as the basic retrieval function, it is better to build a new Indri especially for this project. 
   
2. Build the index
   
   For the NYT collection, porter stemmer is applied, stop words is NOT removed from the collection. We did not extract the content from the xml. It is directly built by using indri build index, with the file format set to xml. 
   
   For the snippets collection, the snippets from different resources are merged to form one snippets index. Porter stemmer is applied, stop words is NOT removed from the collection.
   
3. Axiomatic query expansion

   Link the axiomatic query expansion tool to the indri you created for this package. Make sure the f2log and f2exp method is callable. 
   
   To train the axiomatic query expansion method, take the following steps:
   
   * Make the initial run using a basic retrieval method with the original query file (original_query_file.txt)
   * Save the result from previsou step as original result file (original_result_file.txt)
   * Save the absolute path to the same index as the one used in first step to index_list (index_list.txt)
   * Generate expansion terms:
   
   `trec_query_expansion -oqf=original_query_file.txt -index_list=index_list.txt -orf=original_result_file.txt -M=20 -R=20 -L=20 -K=1000 -beta=0.5 -output=OUTPUTFILE`
   
   The M, R, L, K, and beta are parameters need to be tuned, while L is always set to 1000.
   
   This would generate the query file with expansion terms. Make sure the index field in this generated file is pointing to the correct one, then run this query to see the performance. 
   
   
