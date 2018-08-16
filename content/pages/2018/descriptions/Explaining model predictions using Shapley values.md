Title:Explaining model predictions using Shapley values
URL:2018/descriptions/Explaining model predictions using Shapley values.html
save_as: 2018/descriptions/Explaining model predictions using Shapley values.html



# Explaining model predictions using Shapley values
Finding the contribution of each of our features towards predictions could have a lot of interesting applications. We can use it to reduce the dimensionality of our problem to deal with the curse of dimensionality. We can also use it for finding correlated features in our dataset. It can also be used in clustering applications[1].

The concept of Shapley values comes from cooperative game theory. Shapley value tries to find how important is each player in the overall cooperation, and what payoff can the player expect for the cooperation. This concept can be transferred to machine learning by assuming each feature as a player and the learning task to be a cooperative game[2]. 

Python has a great tool for working with Shapley values called shap (https://github.com/slundberg/shap). Shap[3] provides a unified framework for explaining the outputs of any kind of machine learning models.

This talk will focus on the following points:
1. Why we are interested in explaining our predictions
2. Introduction to Shapley values using Game Theory
3. Application of Shapley values in data science
4. Examples using shap (https://github.com/slundberg/shap)
5. Comparison with other similar methods.

__References:__
[1] Dhamal, Swapnil, et al. "Pattern clustering using cooperative game theory." arXiv preprint arXiv:1201.0461 (2012).
[2] Lundberg, Scott M., and Su-In Lee. "A unified approach to interpreting model predictions." Advances in Neural Information Processing Systems. 2017.
[3] https://github.com/slundberg/shap