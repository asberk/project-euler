##############
## Problem 15:
## 

def traverse( node, node_dict={(0,0) : 0, (1,0): 1, (0,1): 1, (1,1): 2 } ):
    if node not in node_dict:
        nbr_u = ( node[0]-1, node[1] )
        nbr_l = ( node[0], node[1]-1 )
        if -1 in nbr_u: 
            node_dict[node] = traverse(nbr_l, node_dict)
        elif -1 in nbr_l:
            node_dict[node] = traverse(nbr_u, node_dict)
        else:
            node_dict[node] = traverse(nbr_u, node_dict) + traverse(nbr_l, node_dict)
    return node_dict[node]

print traverse( (20,20) ) ## 137846528820

