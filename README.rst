=====
About
=====

CLI Translator provides Google Translate functionality in your terminal.
For now it only translates English to Lithuanian.

Usage::

    $ en2lt works
    "works" to LT:
            statiniai
            kūryba
            gamykla
            statybos darbai
            mechanizmas

Dependencies
============

* Python
* `Splash <https://github.com/scrapinghub/splash>`_

Installation
============

1. Get the splash docker container running::

    $ docker pull scrapinghub/splash
    $ docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash

2. Create `en2lt` script in `/usr/local/bin/en2lt`::

    #! /bin/bash

    project_dir=/home/povilas/projects/cli-translator
    $project_dir/pyenv/bin/python $project_dir/src/main.py $@

3. Make the script executable::

    $ chmod +x /usr/local/bin/en2lt
