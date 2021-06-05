"""In python when we intend to make something attribute private
we use underscore, it is just a convention, it does not make 
the attribute private per si.
"""
class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60

conn = Connector("postgresql://localhost")
print(conn.source)
#'postgresql://localhost'
print(conn._timeout)
#60
print(conn.__dict__)
#{'source': 'postgresql://localhost', '_timeout': 60}

"""
Some developers use this method to hide some attributes, thinking, like in this example,
that timeout is now private and that no other object can modify it. Now, take a look at
the exception that is raised when trying to access __timeout . It's AttributeError , saying
that it doesn't exist. It doesn't say something like "this is private" or "this can't
be accessed" and so on. It says it does not exist. This should give us a clue that, in fact,
something different is happening and that this behavior is instead just a side effect, but not
the real effect we want.
"""
class Connector2:
    def __init__(self, source):
        self.source = source
        self.__timeout = 60

conn = Connector2("postgresql://localhost")
print(conn.source)
#'postgresql://localhost'
print(conn._timeout)
#60
print(conn.__dict__)
#{'source': 'postgresql://localhost', '_timeout': 60}
"""
What's actually happening is that with the double underscores, Python creates a different
name for the attribute (this is called name mangling). What it does is create the attribute
with the following name instead: "_<class-name>__<attribute-name>" . In this case,
an attribute named '_Connector__timeout' , will be created, and such an attribute can be
accessed (and modified) as follows:
"""
print(conn._Connector2__timeout)