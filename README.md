HI All,

This site is created with Python's Flask, SK learn, Pandas, and we are using an album API online to get pictures of the albums, etc. 
Basically, from the entry point you can put in an album name(case sensitive), and it will send out a list of 10 similiar albums.
The recommendations are content based, so I have a CSV that has 5000 album names and their descriptions. I put all of the descriptor words into
a "word soup", and I call an SK learn algorithm to compare those word soups with other albums' word soups. So it's not a popularity based algorithm.
Additionally there is an API that you can call which will perform the same function, the endpoint is http://<site_name>:<port_number>/recommendations/<album_name>.
If you perform a get request on this endpoint with the album name it will perform the same function as if you entered the website and did it manually; however,
it will return the content in a json format. Anyways have fun, this was my 2nd project or probably first full project with flask. Flask is very lightweight which made it fun.

-Tyler
