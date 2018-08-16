Title:How to not screw up with machine learning in production (and more about engineering in data science)
URL:2018/descriptions/How to not screw up with machine learning in production (and more about engineering in data science).html
save_as: 2018/descriptions/How to not screw up with machine learning in production (and more about engineering in data science).html



# How to not screw up with machine learning in production (and more about engineering in data science)
Machine learning is on a way to wide adoption, but getting it right is more of an art than a science yet. This is also true for the last part of data science pipeline - getting trained model with suitable performance out to the world to make valuable predictions.

Many of data science teams, being pressured by deadlines, follow the path of least resistance - wrapping their model into Flask web service and exposing it online. This results in strong coupling of machine learning models with other components and makes changes and experimentation costly.

There is need to allow small teams working on ML problems to easily try new ideas with reliable infrastructure.
To solve this I propose RefreshML - open source data science dashboard, powered by messaging and deployment infrastructure that makes managing machine learning models in production more flexible and provides tools for avoiding common pitfalls.

By treating ML model as a microservice, it's possible to apply best practices accumulated by software engineers.
This includes separation of clients requesting prediction from predictive models via a messaging system, which enables autoscaling models to meet the load and allows to perform A/B testing in relevant use cases, such as recommendation systems.
It also allows to detect dataset shift interactively, and maybe in future even detect adversarial attacks for deep learning models.

Data scientists have big problems to solve. As a community, we should help them with the right tools and best approaches, so ML projects will be safe, ethical and deliver value