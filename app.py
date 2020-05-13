from utils import Graph
from colorama import Fore
from PyInquirer import prompt


graph = Graph()
selection = ""

graph.add_vertex("A")
graph.add_vertex("A#/Bb")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("C#/Db")
graph.add_vertex("D")
graph.add_vertex("D#/Eb")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("F#/Gb")
graph.add_vertex("G")
graph.add_vertex("G#/Ab")

graph.add_edge("A", "A#/Bb")
graph.add_edge("A#/Bb", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "C#/Db")
graph.add_edge("C#/Db", "D")
graph.add_edge("D", "D#/Eb")
graph.add_edge("D#/Eb", "E")
graph.add_edge("E", "F")
graph.add_edge("F", "F#/Gb")
graph.add_edge("F#/Gb", "G")
graph.add_edge("G", "G#/Ab")
graph.add_edge("G#/Ab", "A")

root_note = [
    {
        "type": "list",
        "name": "root",
        "message": "Choose the root note of your scale:",
        "choices": [
            "A",
            "A#/Bb",
            "B",
            "C",
            "C#/Db",
            "D",
            "D#/Eb",
            "E",
            "F",
            "F#/Gb",
            "G",
            "G#/Ab",
            "Quit",
        ],
    }
]

musical_scale = [
    {
        "type": "list",
        "name": "scale",
        "message": "Choose the scale you would like to view:",
        "choices": [
            "Ionian",
            "Dorian",
            "Phrygian",
            "Lydian",
            "Mixolydian",
            "Aeolian",
            "Locrian",
            "Quit",
        ],
    }
]

while not selection == "Quit":
    selection = prompt(root_note)
    root = selection["root"]
    selection = prompt(musical_scale)
    scale = selection["scale"]
    graph.find_scale(root, scale)
    selection = "Quit"
