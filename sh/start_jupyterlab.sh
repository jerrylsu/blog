#!/bin/sh

# pip install jupyterlab -i https://pypi.doubanio.com/simple

jupyter lab --generate-config
echo 'Please input jupyter lab password'
jupyter lab password
echo 'Password input success!'

chmod 777 ~/.jupyter/jupyter_server_config.json
PASSWORD=$(cat ~/.jupyter/jupyter_server_config.json | grep password | awk -F '"' '{print $4}')

# need install oh-my-zsh!!!
echo "c.ServerApp.terminado_settings = {'shell_command': ['/bin/zsh']}" >> ~/.jupyter/jupyter_lab_config.py
echo "c.NotebookApp.ip='*'" >> ~/.jupyter/jupyter_lab_config.py
echo "c.NotebookApp.password = '$PASSWORD'" >> ~/.jupyter/jupyter_lab_config.py
echo "c.NotebookApp.open_browser = False" >> ~/.jupyter/jupyter_lab_config.py
echo "c.NotebookApp.port = 8888" >> ~/.jupyter/jupyter_lab_config.py
cd ~
echo "c.NotebookApp.notebook_dir = 'Documents/blog'" >> ~/.jupyter/jupyter_lab_config.py

nohup jupyter lab --ip=0.0.0.0 --no-browser --allow-root --port 8888 > ./jupyter.log 2>&1 &

# conda install nb_conda
