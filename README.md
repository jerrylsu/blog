### 1. Clone Blog 

`git clone git@github.com:jerrylsu/blog.git`

### 2. Create virtual environment

- `conda create -n blog python=3.6.8`

- `conda activate blog`

- `pip install pelican -i https://pypi.doubanio.com/simple`

- `pip install bs4 markdown webassets cssmin -i https://pypi.doubanio.com/simple`

### 3. Install themes & plugins

The dir of themes and plugins can be pulled by pelican site.

#### download theme elegant

https://github.com/getpelican/pelican-themes

- `cd /blog/themes`

- `git clone git@github.com:Pelican-Elegant/elegant.git`

- `pelican-themes --install themes/elegant --verbose`

https://github.com/getpelican/pelican-plugins

### 4. Clone Deployment

- `mkdir output`

- `git clone git@github.com:jerrylsu/jerrylsu.github.io.git`

