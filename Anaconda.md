### Managing Environments
conda create -n env_name
conda activate my_env
### Saving and loading environments
conda env export > environment.yaml
### Create an environment
conda env create -f environment.yaml
### Listing environments
conda env list
## Jupyter Notebooks
### Math expressions
You can create math expressions in Markdown cells using LaTeX symbols. Notebooks use MathJax to render the LaTeX symbols as math symbols. To start math mode, wrap the LaTeX in dollar signs `$y = mx + b$` for inline math. For a math block, use double dollar signs,
```
$$
y = \frac{a}{b+c}
$$
```
This is a really useful feature, so if you don't have experience with LaTeX, [here is a tutorial](https://latex-tutorial.com/) on using it to create math expressions.
