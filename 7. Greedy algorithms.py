def change_greedy(amount, coinage):
    """the greedy algorithm for the coin change problem"""
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

def print_shows(show_list):
    """prints the start times of the events in order"""
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
        
def fractional_knapsack(capacity, items):
    """returns the maximum achievable value ("benefit") obtainable with a 
    knapsack of the given capacity and a given list of items, each
    represented by a tuple (name, value, weight)."""
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

#--------------------------------------------------------------------------
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
        dfs = self.traverse()
        result = ""
        if len(dfs.keys()) == 0:
            return ""
        else:    
            for items in text:
                result += dfs[items]
            return result

    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        result = ""
        main_root = self.root

        for item in binary:
            if item == "0":
                
                if type(self.root.left) == Leaf:
                    result += self.root.left.char
                    self.root = main_root
                else:
                    self.root = self.root.left
                    
            else: # if the item is 1
                
                if type( self.root.right) == Leaf:
                    result +=  self.root.right.char
                    self.root = main_root
                    
                else:
                    self.root =  self.root.right                 
        return result
        
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
        """Define self to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        self.root = None
        holder = []
               
        for items in freqs:
            holder.append((items, freqs[items]))
       
        num = []
        for items in holder:
            num.append(items[1])
       
        self.tree = []
        done = []

        letter = None
        for i in sorted(num):
            for items in holder:
                if items[1] == i:
                    if items[0] not in done:
                        letter = items[0]
            self.tree.append(Leaf(i, letter))
            done.append(letter)

   
        while len(self.tree) > 1:

            smallest = math.inf
            for item in self.tree:  # left
                if item.count < smallest:  # if the count is smaller 
                    smallest = item.count
                    left = item
                else:
                    if item.count == smallest: # if the count is the same
                        if type(item) == Leaf:
                            if item.char < left.char:
                                left = item                            
                        else:
                            if item.min_char < left.char:
                                left = item
            self.tree.remove(left)

            smallest = math.inf
            for item in self.tree:  # right 
                if item.count < smallest:  # if the count is smaller 
                    smallest = item.count
                    right = item
                else:
                    if item.count == smallest: # if the count is the same
                        if type(item) == Leaf:
                            if item.char < right.char:
                                right = item                            
                        else:
                            if item.min_char < right.char:
                                right = item
            self.tree.remove(right)
            
            total = left.count + right.count
            self.tree.append(Node(left, right))
            
            
        for items in self.tree:  # to change the tree from a list
            self.root = items
            
    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)
#------------------------------------------------------------------------------


