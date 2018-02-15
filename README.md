# Sorensen Compression

The basic idea is that you can generate your own data without really inflating anything. Just by knowing the following information:

1. Total size of the data
2. Hash of the data
3. Number of each unique data group occurance in your data

For example, say you have the data bytes "abc"

You know the length of the file is 3 bytes

You know the hash (in this example I'll use sha256) is `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`

Finally, for the unique data groups, I'll use the example of group of {1} and find the total number of binary 1's in the data. I believe this would be the most difficult to regenerate.

To do this we take our data "abc"

which in binary would be `01100001 01100010 01100011`

So there will be 10 uinique groups of {1}

Now we generate possible combinations untilt the hash of it is correct and we have our data! :D

So the the total number of possible combinations would be 24 choose 10 which == 1961256 combinations. Out of the total combinations of 2^24 == 16777216 the 1961256 brings the number of hashes to try to only 11.69% of all possible.

![LaTex Image](http://mathurl.com/ycgnob6r.png "quick mafs")

With more bits in a group, the data needed would increase but the computations required would decrease.
