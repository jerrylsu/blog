### 1. Clone Blog 

`$ git clone git@github.com:jerrylsu/blog.git`

### 2. Create virtual environment

```
$ conda create -n blog python=3.6.8

$ conda activate blog

$ pip install pelican -i https://pypi.doubanio.com/simple

$ pip install bs4 markdown webassets cssmin -i https://pypi.doubanio.com/simple
```

### 3. Install themes & plugins

The directory of themes and plugins can be pulled by pelican site.

#### download and install theme elegant

[github.com/getpelican/pelican-themes](github.com/getpelican/pelican-themes)
```
$ cd /blog/themes

$ git clone git@github.com:Pelican-Elegant/elegant.git

$ pelican-themes --install themes/elegant --verbose
```

#### download pelican plugins

[github.com/getpelican/pelican-plugins](github.com/getpelican/pelican-plugins)
```
$ cd blog

$ git clone git@github.com:getpelican/pelican-plugins.git

$ mv peliacn-plugins plugins
```

### 4. Deploy Blog

```
$ mkdir output

# Binding  domain name.

$ touch output/CNAME

$ echo 'www.jerrulsu.com' >> output/CNAME

# Generate automatically deployment files into output directory
# and deploy blog to github.com:jerrylsu/jerrylsu.github.io.git.
# if use windows conda environment on cygwin, you must use command
# source activate blog && python -i ./cmder p

$ ./cmder p
```

### 5. Apache2 web server
```
# /etc/apache2
service apache2 start
```

### 6. Isso comments server

### 7. Jupyterlab server

Using my blog with jupyterlab server.

- `./jupyterlab.sh`

```
#!/bin/sh

# enter docker

# pip install jupyterlab -i https://pypi.doubanio.com/simple

cd ~
jupyter lab --generate-config
echo 'Please input jupyter lab password'
jupyter lab password
echo 'Password input success!'

chmod 777 ~/.jupyter/jupyter_server_config.json
PASSWORD=$(cat ~/.jupyter/jupyter_server_config.json | grep password | awk -F '"' '{print $4}')
echo $PASSWORD
echo "c.NotebookApp.ip='*'" >> ~/.jupyter/jupyter_lab_config.py
echo "c.NotebookApp.password = '$PASSWORD'" >> ~/.jupyter/jupyter_lab_config.py
echo "c.NotebookApp.open_browser = False" >> ~/.jupyter/jupyter_lab_config.py
echo "c.NotebookApp.port = 8888" >> ~/.jupyter/jupyter_lab_config.py
echo "c.NotebookApp.notebook_dir = '/'" >> ~/.jupyter/jupyter_lab_config.py

# need install oh-my-zsh!!!
echo "c.ServerApp.terminado_settings = {'shell_command': ['/bin/zsh']}" >> ~/.jupyter/jupyter_lab_config.py

nohup jupyter lab --ip=0.0.0.0 --no-browser --allow-root --port 8888 > jupyter.log 2>&1 &

# conda install nb_conda
```

- `Terminal`

[oh-my-zsh](https://ohmyz.sh/)

vim ~/.zshrc

```
ZSH_THEME="agnoster"
```

[powerline](https://powerline.readthedocs.io/en/latest/index.html)

Settings > Advanced Settings Editor > Terminal > User Preferences

```
{
    // Terminal
    // @jupyterlab/terminal-extension:plugin
    // Terminal settings.
    // *************************************

    // Theme
    // The theme for the terminal.
    "theme": "dark",
    
    // Font family
    // The font family used to render text.
    "fontFamily": "Meslo LG s for PowerLine",
    
    // Font size
    // The font size used to render text.
    "fontSize": 15,
}
```

### FAQ

[1](1). pelican-jupyter could not process .ipynb file.

```
[NbConvertApp] WARNING | Config option `kernel_spec_manager_class` not recognized by `NbConvertApp`.                                                                                            Could not process articles/Programming/2021-08-05-Python-m.ipynb                                                                                                                                   
basic
```

pip install nbconvert==5.6.0

[https://github.com/danielfrg/pelican-jupyter/issues/126](https://github.com/danielfrg/pelican-jupyter/issues/126)
