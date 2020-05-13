class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def find_scale(self, root_note, scale):
        s = Stack()
        s.push(root_note)
        notes_arr = []

        while s.size() > 0:
            cur_note = s.pop()

            if cur_note not in notes_arr:
                notes_arr.append(cur_note)

            for next_note in self.get_neighbors(cur_note):
                if next_note not in notes_arr:
                    s.push(next_note)

        if scale == "Ionian":
            result = []
            shape = [0, 2, 4, 5, 7, 9, 11]
            for key, note in enumerate(notes_arr):
                if key in shape:
                    result.append(note)
            print(result)
        elif scale == "Dorian":
            result = []
            shape = [0, 2, 3, 5, 7, 9, 10]
            for key, note in enumerate(notes_arr):
                if key in shape:
                    result.append(note)
            print(result)

        elif scale == "Phrygian":
            result = []
            shape = [0, 1, 3, 5, 7, 8, 10]
            for key, note in enumerate(notes_arr):
                if key in shape:
                    result.append(note)
            print(result)

        elif scale == "Lydian":
            result = []
            shape = [0, 2, 4, 6, 7, 9, 11]
            for key, note in enumerate(notes_arr):
                if key in shape:
                    result.append(note)
            print(result)

        elif scale == "Mixolydian":
            result = []
            shape = [0, 2, 4, 5, 7, 9, 10]
            for key, note in enumerate(notes_arr):
                if key in shape:
                    result.append(note)
            print(result)

        elif scale == "Aeolian":
            result = []
            shape = [0, 2, 3, 5, 7, 8, 10]
            for key, note in enumerate(notes_arr):
                if key in shape:
                    result.append(note)
            print(result)

        elif scale == "Locrian":
            result = []
            shape = [0, 1, 3, 5, 6, 8, 10]
            for key, note in enumerate(notes_arr):
                if key in shape:
                    result.append(note)
            print(result)
