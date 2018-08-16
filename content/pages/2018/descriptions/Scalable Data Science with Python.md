Title:Scalable Data Science with Python
URL:2018/descriptions/Scalable Data Science with Python.html
save_as: 2018/descriptions/Scalable Data Science with Python.html



# Scalable Data Science with Python
This talk will provide key insights on the learnings I have obtained throughout my career building & deploying machine learning systems in critical environments across several sectors - more specifically, key lessons on building, scaling and maintaining complex data pipelines that consist of large number of algorithms and pre/post-processing tasks that run on data across multiple nodes.

## Motivations
As your data science project grows in complexity, you tend run into multiple data-ops challenges:

* There is a growing need to pull data from different sources
* There is a growing need to pre- and post-process data
* As complexity increases tasks depending on others (if a task fails we wouldn't want to run the children tasks)
* Some tasks need to be triggered every X minutes/hours
* Having just python tasks ran by Linux chronjob gets messy
* Testing of pipelines becomes increasingly hard
* Introduced complexity executing tasks in a distributed architecture

# Introducing Airflow 
In this talk I will introduce what I call the Swiss army knife of data science / data pipelines - Airflow. A fast growing apache incubation project written in Python that contains most of the key features you would have dreamed of for managing data pipelines. I will provide a deep dive on how to build scalable and distributed machine learning data pipelines using Airflow, and how it can help address several of the issues you will encounter as you scale your DataOps.

# Alternative technologies
I will provide a brief comparison between Airflow and other technologies available out there, together with its key differentiators. This includes technologies such as Luigi, Chronos, Pinball, etc. 

# Objectives of the talk
If you attend the talk, you will obtain an understanding on the solid fundamentals of Airflow, together with its caveats and walk-arounds for more complex use-cases. As we proceed with the examples, I will cover the challenges that you will run into when scaling Machine Learning systems, and how Airflow can be used to address these using a manager-worker-queue architecture for distributed processing with Celery.  By the end of this talk you will have the knowledge required to build your own industry-ready machine learning pipelines to process data at scale, and I will provide further reading resources so people are able to implement the knowledge obtained almost right away.