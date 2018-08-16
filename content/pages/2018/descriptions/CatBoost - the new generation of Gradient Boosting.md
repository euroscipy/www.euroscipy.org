Title:CatBoost - the new generation of Gradient Boosting
URL:2018/descriptions/CatBoost - the new generation of Gradient Boosting.html
save_as: 2018/descriptions/CatBoost - the new generation of Gradient Boosting.html



# CatBoost - the new generation of Gradient Boosting
Gradient boosting is a powerful machine-learning technique that achieves state-of-the-art results
in a variety of practical tasks. For a number of years, it has remained the primary method for
learning problems with heterogeneous features, noisy data, and complex dependencies: web search,
recommendation systems, weather forecasting, and many others.
CatBoost (http://catboost.yandex) is a new open-source gradient boosting library, that outperforms existing publicly available implementations of gradient boosting in terms of quality. It has a set of addional advantages.
1. CatBoost is able to incorporate categorical features in your data (like music genre, URL, search query, etc.) in predictive models with no additional preprocessing. For more details on our approach please refer to our NIPS 2017 ML Systems Workshop paper (http://learningsys.org/nips17/assets/papers/paper_11.pdf).
2. CatBoost inference is 20-60 times faster then in other open-source gradient boosting libraries, which makes it possible to use CatBoost for latency-critical tasks.
3. CatBoost has the fastest GPU and multi GPU training implementations of all the openly available gradient boosting libraries.
4. CatBoost requires no hyperparameter tunning in order to get a model with good quality.
5. CatBoost is highly scalable and can be efficiently trained on hundreds of machines

The talk will cover a broad description of gradient boosting and its areas of usage and the differences between CatBoost and other gradient boosting libraries. We will also briefly explain the details of the proprietary algorithm that leads to a boost in quality.