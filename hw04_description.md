# Homework No 4 - _From Notebooks to Research Packages, Part II_

* **Statistics 159/259, Spring 2022**
* **Due Friday 04/14/2023, 11:59PM PT**
* Prof. F. Pérez and GSI F. Sapienza, Department of Statistics, UC Berkeley.
* This assignment is worth a maximum of **50 points**.
* Assignment type: **group**.

For this assignment, we will start from the conclusion of HW02 and continue improving the structure of your repository as a Reproducible Research Package, using again the code from the [LIGO Gravitational Wave Detection Tutorial](https://github.com/losc-tutorial/LOSC_Event_tutorial).

In this assignment we are giving you as a starting point effectively the solution to HW02, and you will now add a bit more structure, tests, documentation, etc, to complete the picture.

## Deliverables

### [5 points] Repository structure

The repository starts with all the code and data with the same layout as LIGO created it. You will reorganize it, while checking that the code still runs, so that all data files live in a `data` directory, generated figures get saved to `figures`, and generated audio goes into `audio`.  

These directories should be present in the repository even before you run any code. Since Git will not let you add an empty directory to a repository, you will need to use a little hack by putting an empty `.gitkeep` file in those directories (as explained [here](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/gitkeep-push-empty-folders-git-commit)). 

### [ 5 points] Installable package

In HW05 you made `ligotools` usable as a local package that could be imported from the current directory. Now you will make it an actually installable package as discussed in class, with the appropriate `pyproj.toml`, `setup.py` and `setup.cfg` files. Use the [mytoy](https://github.com/fperez/mytoy) repository as guiding example for this and next part.  

Note: for the authorship, you should list as authors "Ligo Scientific Collaboration (LSC) and `<your group number and names>`".

### [ 5 points ] Add tests to `readligo.py`

You should add four separate small tests to the functions in `readligo.py` that are part of the `ligotools` package.  Make a subfolder called `tests` and put in there `tests_readligo.py` with your tests. 

The command `pytest ligotools` should run all those tests.

### [ 5 points ] Create `utils.py`

In the `ligotools` package, make a new module called `utils.py` and move the following functions from the notebook into `utils`: `whiten`, `write_wavfile`, `reqshift`. You will then need to update the notebook to use these functions imported from `ligotools.utils` instead.

### [ 5 points ] Make new plotting utility in `utils.py`

Find the notebook cell that begins with

```
# -- To calculate the PSD of the data, choose an overlap and a window (common to all detectors)
#   that minimizes "spectral leakage" https://en.wikipedia.org/wiki/Spectral_leakage
```

and move its plotting code into a separate utility function, then call that from the notebook.

### [ 5 points ] Add tests to `utils.py`

You should add four separate small tests to the functions in `utils.py`. These should test the three functions you moved from the notebook and the new plotting one you made above.

The command `pytest ligotools` should run all those tests.

### [ 5 points ] JupyterBook

Set up the repository to be a proper JupyterBook one that builds a page for the main notebook and includes a visible Binder link in the JupyterBook build.

Remember that on the Hub, in order to be able to view the book build without having to use the VNC desktop, we need to run sphinx manually. Follow the instruction about how to do this in the [JupyterBook lecture](https://ucb-stat-159-s23.github.io/site/lectures/documentation/jupyter-book.html).


### [ 5 points ] GitHub Pages and Actions

Configure your repository to have a public GitHub Pages URL and set up a GitHub Action that builds the JupyterBook build of the repository on all pushes to the main branch (like the class repo works). Remember we talked about continuous integration with JupyterBook at the end of the respective [Lab session](https://ucb-stat-159-s23.github.io/site/lab/lab07/lab07.html).

### [ 5 points ] Makefile

There should be a `Makefile` with the following targets

- `env`: creates and configures the environment.
- `html`: build the JupyterBook normally (calling `jupyterbook build .`). Note this build can only be viewed if the repository is cloned locally, or with the VNC desktop on the Hub.
- `clean`: clean up the `figures`, `audio`  and `_build` folders.

### [5 points] GitHub repository

In this homework we are going to evaluate the overall workflow using git a GitHub. Be sure that you repository includes:

- Your repository name has to be `hw04-GroupXX`, with `XX` the number of your group.
- Clear commit messages as you make progress on the homework.
- Your repository needs to include all the tags described in the previous items.
- The README.md should include a basic description of the project with the Binder badge on it so you can directly launch Binder from there.
- Not include any other file or folder that those needed for the project. For archiving this you can include a .gitignore file with the files you want git to ignore.
- Add the link to your JupyterBook to GitHub 
- Complete the contribution statement. 
