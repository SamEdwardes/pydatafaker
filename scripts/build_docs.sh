echo "-----------------------------------"
echo "Convert .ipynb to markdown"
echo "-----------------------------------"
echo "-------------"
jupyter nbconvert --to markdown --execute README.ipynb
echo "-------------"
jupyter nbconvert --to markdown --execute docs/source/usage.ipynb

echo "-----------------------------------"
echo "Build sphinx docs"
echo "-----------------------------------"
cd docs;
make html;