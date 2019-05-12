# python-graph-powering
Testing python programming.

* Create several Node class instances
  - Each node has:
    - an ID
    - a state (open / close). Closed means the power won't be transfered to children
    - a list of children Nodes
    - a "powered" information, false by default
* Link some random nodes
* Add power to random nodes and their children

Result is saved in a file

Possible evolutions:
  - Add multi-threading
  
  Example with :
    -     nodes_nbr = 900
    -     max_link_nbr = 800
    -     node_per_line = 30
    -     power_unit_nbr = 10
    
![Example](https://github.com/mlaffargue/test-python-graph/blob/master/example.png?raw=true)
