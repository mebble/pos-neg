echo "Downloading the dataset..."
wget http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz
echo "Extracting the dataset..."
mkdir dataset
tar -xzf review_polarity.tar.gz -C dataset
rm review_polarity.tar.gz
echo "Done"
