import pydot
import re

sample = '''
graph = pydot.Dot(graph_type='digraph')

node_a = pydot.Node("Node A")

node_b = pydot.Node("Node B")

graph.add_node(node_a)

graph.add_node(node_b)

graph.add_edge(pydot.Edge(node_a, node_b))

graph.write_png('example2_graph.png')

graph.write_svg('graph.svg')

'''

def list_to_graph(graph, tuple_list):
    tuple_table = {}
    seqAnode = None
    seqBnode = None
    for entries in tuple_list:
        seqA = entries[0]
        seqB = entries[1]
        if tuple_table.get(seqA, True):
            tuple_table[seqA] = pydot.Node(seqA)
            graph.add_node(tuple_table[seqA])

        if tuple_table.get(seqB, True):
            tuple_table[seqB] = pydot.Node(seqB)
            graph.add_node(tuple_table[seqB])
        
        graph.add_edge(pydot.Edge(tuple_table[seqA], tuple_table[seqB]))


if __name__ == '__main__':
    
    f = open('containmentcoincidencelist', 'r')
    data = eval(f.read())
    f.close()

    graph = pydot.Dot(graph_type='digraph')
    list_to_graph(graph, data)
#    graph.write_png('conjecture_grid.png')

    svg_data = str(graph.create_svg())
#    graph.write_svg('conjecture_grid.svg')  
    print(svg_data[160])
    print(type(svg_data))
    #print(svg_data.find('<!--'))
    match_array = [elements for elements in re.finditer(r'<!-- A\d\d\d\d\d\d -->', svg_data)]    
    
    #we do it in reverse order to avoid index tracking
    i = len(match_array)-1
    print(i)
    while i > -1:
        currentmatch = match_array[i] 
        match_data = svg_data[currentmatch.start(): currentmatch.end()].split()[1] #the A... content is split by whitespace 
        scan_j =  currentmatch.end()
        end_point = -1

        while scan_j < len(svg_data):
            if svg_data[scan_j:scan_j+4] == '</g>':
                end_point = scan_j+4
                break
            scan_j +=1
        
        #insert our </a> break
        svg_data = svg_data[:end_point] + '</a>' + svg_data[end_point:] 
        
        svg_data = svg_data[:currentmatch.end()] + '<a href="http://oeis.org/' + match_data + '" >' + svg_data[currentmatch.end():]

        #now we insert the break here 
        i-=1
    #at this point svg_data has trashed newlines so we need to repair it 
    
    svg_data = svg_data.replace("\\n", "\n")
    #strip off the 'b' tags 
    svg_data = svg_data[2:-1]

    f = open('altered_conjecture_map.svg', 'w')
    f.write(svg_data)
    f.close()
