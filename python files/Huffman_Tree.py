def change_greedy(amount, coinage):
    
    coinage = sorted(coinage)
    
    holder = []
    
    imax = -1
    
    while amount > 0: # gets the amounts of each coin in a list 
        while coinage[imax] > amount:
            imax -= 1
        holder.append(coinage[imax])
        amount -= coinage[imax]
        if amount < min(coinage)-1:
            return None
    
    result= [] #reformats the coins with a count of each of the coins 
    for coin in coinage[::-1]:
        count = 0
        for item in holder:
            if item == coin:
                count +=1
        if count > 0:
            result.append((count, coin))
        
    return result

#print(change_greedy(82, [1, 10, 25, 5]))
#print(change_greedy(80, [1, 10, 25]))
#print(change_greedy(82, [10, 25, 5]))

#-------------------------------------------------------------------------------


def print_shows(show_list):
    
    end_time = []
    t_current = 0
    result = set()
    
    # finds the end time of each interval    
    for item in show_list: 
        finish_time = item[1] + item[2]
        end_time.append([finish_time, item[1], item[0]])
        
    # finds the greedy path 
    for j in sorted(end_time): 
        if j[1] >= t_current:
            result.add((j[1], j[0], j[2]))
            t_current = j[0]
    #  reorginizes to print out in format of title, start and end times on per
    #  line
    for items in sorted(result):
        print(items[2], items[0], items[1])
    
#print_shows([
    #(27,675,17),
    #(3,551,25),
    #(11,678,44),
    #(19,560,10),
    #(6,804,6),
    #(103,662,20),
    #(24,762,110), 
    #(81,629,54),
    #(93,724,32),
    #(159,880,16),
    #(77,915,9),
    #(92,718,31),
    #(15,890,23),
    #(16,571,15),
    #(5,934,20),
    #(205,762,7),
    #(100,629,77),
    #(99,876,43),
    #(1,891,22)])

#-------------------------------------------------------------------------------

def fractional_knapsack(capacity, items):
    
    in_order = []
    #sorts the list in the format of "profit/weight, name, profit, weight"
    for item in items: 
        devision = item[1] / item[2]
        in_order.append((devision, item[0], item[1], item[2]))
    in_order = sorted(in_order)[::-1] #puts the list in highest to lowest order

    count = 0
    weight = 0
    #uses one of each item until the weight equals the capacity 
    for each in in_order:
    
        if weight <= capacity:
    
            if each[3] > (capacity-weight): #for when fractions are needed
                test = 0
                item_weight =each[3] 
                # if the weight of the item is too big to fit this will
                # fractionizes it
                while item_weight !=(capacity-weight):
                    test +=1
                    item_weight -= 1
                weight += item_weight
                count += (each[2] / each[3])*item_weight 
                break
    
            weight += each[3]
            count += each[2]
        else: break
    
    return count
    

## The example from the lecture notes
#items = [
    #("Chocolate cookies", 20, 5),
    #("Potato chips", 15, 3),
    #("Pizza", 14, 2),
    #("Popcorn", 12, 4)]
#print(fractional_knapsack(9, items))
#------------------------------------------------------------------------------


"""An incomplete Huffman Coding module, for use in COSC262.
   Richard Lobb, April 2021.
"""
import re

HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)

    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__repr__(level + 1) + ',\n' +
            self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False

    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count)) # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')


class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label) # Add this leaf to the graph


class HuffmanTree:
    """Operations on an entire Huffman coding tree.
    """
    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root
        
    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.
        """
        raise NotImplementedError  # *** TO BE IMPLEMENTED
        
    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        raise NotImplementedError  # *** TO BE IMPLEMENTED

    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)

    def build_from_freqs(self, freqs):
        """Define self.root to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        self.root = None          # *** FIXME ***
        raise NotImplementedError # *** TO BE IMPLEMENTED

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)


def main():
    """ Demonstrate defining a Huffman tree from its string representation and
        printing and plotting it (if plotting is enabled on your machine).
    """
    tree = HuffmanTree()
    tree_string = """Node(42,
      Node(17,
        Leaf(8, 'b'),
        Leaf(9, 'a')),
      Node(25,
        Node(10,
          Node(5,
            Leaf(2, 'f'),
            Leaf(3, 'd')),
          Leaf(5, 'e')),
        Leaf(15, 'c')))
    """
    tree.build_from_string(tree_string)
    print(tree)
    tree.plot()
    
    # Or you can build the tree directly
    tree2 = HuffmanTree(Node(
      Node(
        Leaf(8, 'b'),
        Leaf(9, 'a')),
      Node(
        Node(
          Node(
            Leaf(2, 'f'),
            Leaf(3, 'd')),
          Leaf(5, 'e')),
        Leaf(15, 'c'))))
    print(tree2)
    tree2.plot()
    
main()
