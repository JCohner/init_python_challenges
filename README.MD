# Hackathon Day 2 Python Challenges

#### Josh Cohen's Attempts at the Northwestern Master's in Robotics Python Challenges

This was done pretty succesfully. I implemented a recursive solution for both adding elements to the board and checking diagonal victories. 
 
#

Future improvements can include expanding the recursive search to include column and row victories. I see this as a much cleaner solution. Currently we use pandas.iloc boolean features to detect if there are more than 3 of a given players pieces in a row or column and then check to see if at least 4 of those pieces are sequential. Additionally the diagonal recursive search could be improved, we do one for the positive slope diagonal case and one for the negative slope diagonal case, these could likely be combined into the same recursive function. However this should and could be done by making the overall victory check algorithim recursive itself. Finally, I would like to make a class that holds the positional arguments of the last placed piece, that would clean up the readability of the code significantly

#

All in all, great start to the MSR! (also i prefer python 3 to python 2 sorry)