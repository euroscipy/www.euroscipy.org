Title:Efficient Biomedical Named Entity Recognition in Python
URL:2018/descriptions/Efficient Biomedical Named Entity Recognition in Python.html
save_as: 2018/descriptions/Efficient Biomedical Named Entity Recognition in Python.html



# Efficient Biomedical Named Entity Recognition in Python
Systems that offer intelligent access to knowledge extracted from the scientific literature are typically based on a pipeline of extraction tools, which begin from targeted named entity recognition (NER) and linking. Entities such as diseases, genes, proteins, experimental methods, organs, tissues, cell lines, etc. play a fundamental role in conveying the essence of the results presented in a biomedical scientific paper. Their identification as entities of a given type, and the proper resolution of each mention of an entity to the corresponding unique concept in a reference database, is of essential importance in order to be able to capture the significance of scientific result. 
Therefore, efficient and accurate biomedical entity recognition has been at the center of text mining activities in the biomedical field. NER can be used by itself, with the goal of recognizing the mere presence of a term in a certain portion of the text, or as a preliminary stage for Concept Recognition (CR), also known as Entity Linking or Normalization, where the term is not only recognized but also linked to a terminological resource, such as an ontology, through the use of a unique identifier. 
In this presentation we will describe two tools for biomedical entity recognition and linking developed in Python:
- The Bio Term Hub, an aggregator of terminologies from reference databases
- OGER (OntoGene's Biomedical Entity Recognizer), an accurate, fast, efficient and robust NER solution for biomedical entities,  which has been shown to reach state-of-the-art accuracy in biomedical concept recognition