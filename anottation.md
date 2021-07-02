Because a dict uses a hash table internally, and hash tables must be sparse to work, they
are not space efficient. For example, if you are handling a large quantity of records, it
makes sense to store them in a list of tuples or named tuples instead of using a list of
dictionaries in JSON style, with one dict per record. Replacing dicts with tuples reduces
the memory usage in two ways: by removing the overhead of one hash table per record
and by not storing the field names again with each record.

which means that for a lot of datas, using a list of tuple is better than a list of dict