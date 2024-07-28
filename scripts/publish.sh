echo "Building..."
python setup.py sdist bdist_wheel

echo "Uploading..."
twine upload dist/*

echo "Cleaning up..."
python setup.py clean --all

# clean build artifacts
rm -rf *.egg-info

echo "Done."
