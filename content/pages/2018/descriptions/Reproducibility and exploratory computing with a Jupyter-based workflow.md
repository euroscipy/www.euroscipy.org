Title:Reproducibility and exploratory computing with a Jupyter-based workflow
URL:2018/descriptions/Reproducibility and exploratory computing with a Jupyter-based workflow.html
save_as: 2018/descriptions/Reproducibility and exploratory computing with a Jupyter-based workflow.html



# Reproducibility and exploratory computing with a Jupyter-based workflow
Projects requirements are wildly varying across different lifetime stages. In a new project, we need to try a large number of ideas to find the correct approach. Conversely, a mature project may be used to drive decision-making in company or to produce scientific results in an academic lab. As a consequence, mature projects require stable and well-tested codebases. As projects grow, they oftentimes suffer from decisions made at earlier stages, accumulating so called “technical debt”.

In this talk I will present a Jupyter-based workflow for managing a project lifecycle, from the initial exploratory phase to a mature and stable codebase. I will show that combining basic tools such as git, Google Drive, conda environments, python packaging and batch notebook execution, it is possible to manage the complexity of a quickly growing project, with an eye on computational reproducibility.

To this end, we start with a data-first approach. Data needs to be extracted, cleaned and formatted in a form most appropriate for subsequent analysis. By relying on a appropriate data abstractions, we can simplify the code and make the analysis more understandable. 

Next, we illustrate how a young single-notebook project can gradually grow into a larger project using a few python modules and eventually full-blown python packages. As the project is applied more broadly, for example to different datasets, the notebook execution can be automated through batch analysis. Intermediate results and HTML reports should be saved at this point for keeping track of the analysis. Finally, a mature project will depend on custom python packages which employ continuous integration for testing and automated documentation. To improves reproducibility, conda environments can be used to take snapshots of the of dependencies throughout the project lifecycles.

Developing a project throughout its lifetime involves continuous trade-offs between exploratory data analysis and reproducibility, with a focus shifting from the former to the latter as the project matures. With a proper project organization and employing the right tools, it is possible to manage this transition effectively.