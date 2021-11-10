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

### 5. Apache2
```
# /etc/apache2
service apache2 start
```

### 6. isso comments
