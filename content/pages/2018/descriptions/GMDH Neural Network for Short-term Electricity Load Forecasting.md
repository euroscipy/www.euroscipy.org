Title:GMDH Neural Network for Short-term Electricity Load Forecasting
URL:2018/descriptions/GMDH Neural Network for Short-term Electricity Load Forecasting.html
save_as: 2018/descriptions/GMDH Neural Network for Short-term Electricity Load Forecasting.html



# GMDH Neural Network for Short-term Electricity Load Forecasting
The GMDH family of learning algorithms was introduced (Ivakhnenko) for modelling complex non-linear relationships between a set of input features and one or more outputs. 
To construction of a GMDH neural network starts by considering all pairwise combinations of the input features. The first layer of the neural network consists of nodes, or neurons, where each neuron receives the input signal from a specific pairwise combination. Hence, the size of the first layer is determined by the number of input features. Each node independently constructs a second order polynomial, the coefficients of which are determined via a supervised learning algorithms. 
The training proceeds by using an external criterion to rank the nodes of the layer. A standard criterion for "good" approximation is that which minimises the expected loss, also known a generalisation risk. This criterion constitutes a mechanism through which a number of neurons will be eliminated from he network. 
The outputs of the remaining neurons constitute the inputs for the next layer. This process is continued for as long as a subsequent layer produces better results than the previous layer. In the case where performance in a subsequent layer is inferior the training process is completed and the last layer is the output layer.
The final model is the optimal path from the input layer to the output layer, and can be expressed mathematically in terms of higher order polynomials.
Thus, the GMDH is able to identify the most relevant variables through the training procedure and the optimal structure is determined automatically giving self-organising characteristics to the network.

**GMDH application**

Scheduling processes of electricity power systems such as unit commitment and economic dispatch involve decisions that depend on the future values of electricity load demand. 
In broad terms, electricity load forecasting can be categorised into long-term, medium-term and short-term. The short-term aims to forecast demand from 1 hour up to a few weeks ahead, and will be the focus of our example. 
There are genarally two types of forecasting models, time series and explanatory models.  Explanatory models make the assumption that the variable to be forecasted (electricity load in our example) depends on one or more input variables i.e. there exists an explanatory relationship which governs how a change in inputs affects the output. GMDH falls into the second category and the training of the model yields a functional form that approximates this relationship.
At this last part of the presentation we will train a GMDH model using historical information and use it to make short-term electricity load forecasts.