Title:From Zero to JupyterHub with Kubernetes
URL:2018/descriptions/From Zero to JupyterHub with Kubernetes.html
save_as: 2018/descriptions/From Zero to JupyterHub with Kubernetes.html



# From Zero to JupyterHub with Kubernetes
## From Zero to JupyterHub with Kubernetes

JupyterHub is a great way to provide a data analytics environment for a class, a research group or a team of data scientists.
In this talk, we will go through JupyterHub: what it is and how it works and how to setup a production ready deployment on a 
cloud provider using Kubernetes as the underlying infrastructure. During the course of this talk we will examine the internals
of a JupyterHub installation: the proxy, the hub and the individual user notebooks, briefly learn about Kubernetes and 
associated deployment tools such as Helm charts and how they can simplify managing a cloud based JupyterHub deployment and finally talk about
securing an installation: running JupyterHub with HTTPS and authenticating users. 

Abstract

The main aim of this talk is to introduce developers, data scientists and data team leads to the capabilities of 
JupyterHub (what problems can it solve) and how to best deploy and manage it in production on a cloud provider.
No previous knowledge or JupyterHub internals or experience in running it on cloud providers is required
so this talk is suitable for complete novices. 

The talk will be divided into four parts:

### Introduction to JupyterHub
In this section, I will give a brief overview of how Jupyterhub and how it can be used
to provision Jupyter notebooks for classroom or industry use. 

### A brief tour of JupyterHub internals
In this section, we will explore the components that make up a JupyterHub deployment:
the HTTP proxy, the Hub and the Jupyter notebook servers for individual users 
We will use the insight we gain in this section to understand how to run a 
production ready JupyterHub deployment on a cloud provider's infrastructure. 

### Running JupyterHub in the cloud with Kubernetes and Helm
Now that we understand the basics of how JupyterHub works, we can deploy it to a cloud provider (Google Cloud will be used
as an example throughout the talk) with Kubernetes. Never heard or Kubernetes or not sure what value it can add to a JupyterHub
deployment? Not to worry - before we a do a deep dive into the deployment demo, we will briefly
go over what problems Kubernetes helps to solve and how it does this. To wrap up this section, 
we will talk about making JupyterHub deployments easier with the help of Helm charts, what are some
known pitfalls in running JupyterHub in production and do a brief tour of BinderHub.

### Security and Cost
Last (but definitely by no means least ) is making sure that our JupyterHub deployment is secure.
This means ensuring that clients communicate with the Hub using HTTPS and that authentication 
is properly secured. Finally, I will compare the costs of hosting JupyterHub deployments on AWS, 
Google Cloud and Azure.