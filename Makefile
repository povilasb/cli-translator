python ?= python
virtualenv_dir := pyenv
pip := $(virtualenv_dir)/bin/pip

$(virtualenv_dir): $(py_requirements)
	virtualenv $@ -p $(python)
	$(pip) install -r requirements.txt
