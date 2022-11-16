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

[https://github.com/getpelican/pelican-themes](https://github.com/getpelican/pelican-themes)
```
$ cd /blog/themes

$ git clone https://github.com/getpelican/pelican-themes.git

$ pelican-themes --install themes/pelican-bootstrap3 --verbose
```

#### download pelican plugins

[https://github.com/getpelican/pelican-plugins](https://github.com/getpelican/pelican-plugins)
```
$ cd blog

$ git clone git@github.com:getpelican/pelican-plugins.git

$ mv pelican-plugins plugins
```

### 4. Deploy Blog

```
$ mkdir output

# Binding  domain name.

$ touch output/CNAME

$ echo 'www.jerrylsu.net' >> output/CNAME

# Generate automatically deployment files into output directory
# and deploy blog to github.com:jerrylsu/jerrylsu.github.io.git.

$ ./cmder p
```

### 7. Jupyterlab server

Using my blog with jupyterlab server.

- start:`cd sh && ./start_jupyterlab.sh`

- stop: `cd sh && ./stop_jupyterlab.sh`

### 8. Terminal

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

1. pelican-jupyter could not process .ipynb file.

```
[NbConvertApp] WARNING | Config option `kernel_spec_manager_class` not recognized by `NbConvertApp`.                                                                                            Could not process articles/Programming/2021-08-05-Python-m.ipynb                                                                                                                                   
basic
```

pip install nbconvert==5.6.0

[https://github.com/danielfrg/pelican-jupyter/issues/126](https://github.com/danielfrg/pelican-jupyter/issues/126)


2. CRITICAL TypeError: object of type 'NoneType' has no len()

```
(dev)  ✘ sulei03@appledeMacBook-Pro: pelican -s pelicanconf.py content

[15:17:04] CRITICAL TypeError: object of type 'NoneType' has no len()
```

pelican_jerry/__init__.py
```
# cls = settings['PELICAN_CLASS']  # 'pelican.Pelican'
cls = 'pelican_jerry.Pelican'
```