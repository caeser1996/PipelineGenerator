# PipelineGenerator
Pipeline Helper is a library that makes creating MongoDB aggregation pipelines in Python easier and more convenient. The library provides static methods for building pipeline stages, including $project, $match, $group, $sort, $skip & $limit, $first & $last, and $unwind.



Usage
Here is an example of how to use the library to build an aggregation pipeline:

```
from pipeline_helper import PipelineHelper
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]
collection = db["test_collection"]
pipeline = [
    PipelineHelper.match({"status": "A"}),
    PipelineHelper.group({"_id": "$status"}, {"count": {"$sum": 1}}),
    PipelineHelper.sort({"count": -1}),
    PipelineHelper.limit(1)
]
result = collection.aggregate(pipeline)
```




In this example, the pipeline will match documents with a status of "A", group the documents by the "status" field, calculate the number of documents in each group, sort the groups by the count in descending order, and limit the result to the first group.

The library provides a static method for each of the supported pipeline stages, making it easy to build complex aggregation pipelines.

# Contributions
Contributions to Pipeline Helper are welcome. If you would like to contribute, please fork the repository, make your changes, and submit a pull request.
