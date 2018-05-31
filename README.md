# read-big-file-s3-select
How to read a file on S3 using standard SQL

Recently Amazon realeased their S3 Select product on General Availabilty. This is an exciting new tool for data engineers to use so
I thought I'd write up an example showing its use. AWS S3 Select is a way for users to query data in-place on Amazon S3. One of its 
main uses is being able to allow users to  get sub-sets of data from S3 without having to download whole - and potentially huge - 
data files. You should note that S3 Select is inteneded as a query tool not an analytic tool and as such the SQL statemnts 
allowed are limited to SELECT / FROM / WHERE / LIMIT although you can use aggregtaes such as SUM/MIN/MAX/COUNT/AVG and certain 
STRING,DATE, CONVERSION and CONDITIONALS functions. The file I'm querying is the same one I've used in the rest of my 
series on reading big data files that you can find in my other repositories. This is a 21 Gbyte pipe separated text file containing 
approx 335 million records. I used python to call the S3 Select API and tested it using AWS Lambda.
