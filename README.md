# cluster-docs

## Initial Setup

We used the [lanyon theme](https://github.com/poole/lanyon).

```
# Install rubygems
pacman -S rubygems
sudo pacman -S ruby base-devel
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc  # or ~/.zshrc 

#Install poole dependencies
gem install jekyll jekyll-gist jekyll-sitemap jekyll-seo-tag bundler

# Install poole
cd cluster-docs
git clone https://github.com/poole/poole.git
rm poole/README.md
rm poole/LICENSE.md
mv poole/* .
rm -rf poole/
rm 404.html  # lanyon the next package comes with it.

# Install lanyon theme 
git clone https://github.com/poole/lanyon.git
rm lanyon/README.md
rm lanyon/LICENSE.md
mv lanyon/* .
mv lanyon/_includes/* _includes/
mv lanyon/_layouts/* _layouts/
mv lanyon/_posts/* _posts/
rm -rf lanyon/

# install the rest of the gem dependencies
bundle install

jekyll serve
```