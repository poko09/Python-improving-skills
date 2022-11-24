class AhoCorasickAutomaton:

    def __init__(self, trie_with_failure_links):
        self.trie_with_failure_links = trie_with_failure_links

    def __repr__(self) -> str:
        return repr(self.trie_with_failure_links)

    @classmethod
    def build(cls, dictionary):
        trie = cls.build_trie(dictionary)
        trie_with_failure_links = TrieWithFailureLinks.from_trie(trie)

        return AhoCorasickAutomaton(trie_with_failure_links)

    @classmethod
    def build_trie(cls, dictionary):
        node_id = 0
        root = Node(node_id)
        trie = Trie(root, [root], {node_id: []})

        for word in dictionary:
            node_id = trie.add_word(word, node_id)

        return trie

    def search(self, text):
        current = self.trie_with_failure_links.trie.root
        found = list()

        letter_index = 0
        while letter_index < len(text):
            if current.word is not None:
                found.append((current.word, letter_index - len(current.word)))

            letter = text[letter_index]

            next_ = self.trie_with_failure_links.trie.out_edge_with_letter(current.id, letter)
            if next_ is None:  # follow failure link
                next_ = self.trie_with_failure_links.failure_links[current.id]

                # back at the root, letter does not exist in the trie
                if next_ == current:
                    letter_index += 1
            else:
                letter_index += 1

            current = next_

        if current.word is not None:
            found.append((current.word, letter_index - len(current.word)))

        return found


class Node:

    def __init__(self, id, word=None):
        self.id = id
        self.word = word

    def __repr__(self):
        return f"id={self.id}, word={self.word}"


class Edge:
    def __init__(self, start, end, letter):
        self.start = start
        self.end = end
        self.letter = letter

    def __repr__(self):
        return f"start={self.start}, end={self.end}, letter={self.letter}"


class Trie:

    def __init__(self, root, nodes, edges):
        self.root = root
        self.nodes = nodes
        self.edges = edges

    def __repr__(self):
        return f"root={self.root}, nodes={self.nodes}, edges={self.edges}"

    def contains_string(self, string):
        current = self.root
        for letter in string:
            next_ = self.out_edge_with_letter(current.id, letter)
            if next_ is None:
                return None
            current = next_

        return current

    def add_edge(self, node_id, edge):
        self.nodes.append(edge.end)
        self.edges[node_id].append(edge)
        self.edges[edge.end.id] = []

    def add_word(self, word, node_id):
        current = self.root
        for letter in word:
            end = self.out_edge_with_letter(current.id, letter)

            if end is not None:  # letter is already in Trie
                current = end
            else:  # letter is not in Trie
                node_id += 1

                new_node = Node(node_id)
                new_edge = Edge(current, new_node, letter)
                self.add_edge(current.id, new_edge)

                current = new_node
        current.word = word

        return node_id

    def out_edge_with_letter(self, node_id, letter):

        edges = list()
        for edge in self.edges[node_id]:
            if edge.letter == letter:
                edges.append(edge)

        if len(edges) == 1:
            return edges[0].end


class TrieWithFailureLinks:

    def __init__(self, trie, failure_links):
        self.trie = trie
        self.failure_links = failure_links

    def __repr__(self):
        return f"trie={repr(self.trie)}, failure_links={repr(self.failure_links)}"

    @classmethod
    def from_trie(cls, trie):
        failure_links = dict()

        def traverse(node, substring):
            if len(substring) == 0:
                failure_links[node.id] = node
            else:
                i = 1
                node_end = trie.contains_string(substring[i:])
                while i <= len(substring) and node_end is None:
                    node_end = trie.contains_string(substring[i:])
                    i += 1
                failure_links[node.id] = node_end

            for e in trie.edges[node.id]:
                traverse(e.end, substring + e.letter)

        traverse(trie.root, "")

        return TrieWithFailureLinks(trie, failure_links)


if __name__ == '__main__':
    automaton = AhoCorasickAutomaton.build(["AMC", "MCA", "MDE", "CMA", "MNMS"])
    print(automaton.search("MCAADMDENMMNMSCMA"))
    automaton = AhoCorasickAutomaton.build(["abc", "aab", "cba"])
    print(automaton.search("aaabc"))
    print(repr(automaton))
