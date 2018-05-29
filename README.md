

# Anaconda

This tutorial is split into three sections. The first part, for installing Anaconda. The second part, for testing your installation (making sure conda works, dealing with path issues etc). Finally, the last part of the tutorial goes over installing packages, and environment management.

### Installing Anaconda

- Download and install Anaconda (windows version) from  https://www.anaconda.com/download/ (install the one for Python 2.7)

- Select the default options when prompted during the installation of Anaconda.

- After you finished installing, open the Anaconda Prompt. Type the command below to check if you can use a Jupyter (IPython) Notebook. It should open a page called Home in your browser. If this is the case, you are good just close the browser and go on with the toturial.

```
jupyter notebook
```

### Finalizing the installation

- Now we have to add python and conda to your environment variables. To verify that these things are not working right now open the normal command prompt (type cmd from the start menu) and type `jupyter` or `conda`. You should get something like:

```
'jupyter' is not recognized as an internal or external command, operable program or batch file
```

```
'conda' is not recognized as an internal or external command, operable program or batch file
```

- Copy and paste the next line into Notepad

```
;C:\Users\YOUR_LOGIN_HERE\AppData\Local\Continuum\anaconda2\Scripts;C:\Users\YOUR_LOGIN_HERE\AppData\Local\Continuum\anaconda2\;
```

- Modify the string changing YOUR_LOGIN_HERE with your user login (the name of your UMD directory).
If you are not sure what this is, open the cmd prompt and look at the name of the directory you find yourself in. (In my case `C:\Users\iurif` so my name is `iurif`)

- Open Start menu and type `variables`. Click on `Edit enviroment variables for your account`.

- Select the variable PATH and click on Edit (WARNING!!!!! do not delete the string written there. This will affect many other programs in your account)

- Copy and past the string modified from Notepad into this variable. Append it at the end of the current variable PATH.

- Open a new cmd prompt and check that everything is working by typing `conda` or `jupyter notebook`. Now you should get different behaviors.

### Playing with the environments

Once of the good feature of Anaconda is that of providing an easy way for creating Environments for working with your python libraries.

- Open Anaconda Navigator and click on environments

- Click on Create

- Set a new Environment name, for example `Py3` and select Python 3.6 as default package set. It will take few seconds but now you will be working in a full environment providing all the features of Python 3.6 even if in the default system we have Python 2.7 running.

- Now we can add a set of libraries that we will need for our next exercise.

- From the same view, go on the Search Packages text field and type Numpy. If nothing shows up click on Installed and change it with Not Installed.

- Now numpy should be in the list of Packages that we can install. Click on it and click on Apply

- Do the same thing with Matplotlib

- Look at the Home menu. I suggest you to install `spyder` for having a nice IDE to work with.

- Now you are all set. You can proceed with the actual lab.

# Numpy

- Follow the instructions in compute_neighbors.py and complete the script. For each instruction you can use a limited amount of lines of code.

- In neighbor_graph.py use what implemented in compute_neighbors.py for extracting the nearest neighbors of each point.
